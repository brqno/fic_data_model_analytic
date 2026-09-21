
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

from airflow.decorators import dag, task


PROJECT_ROOT = Path(
    os.getenv("PROJECT_ROOT", "/opt/airflow/project")
).resolve()

sys.path.insert(0, str(PROJECT_ROOT))


@dag(
    dag_id="pipeline_vendas",
    schedule="0 6 * * *",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    default_args={
        "owner": "engenharia-dados",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["vendas", "python", "dbt", "sql-server"],
)
def pipeline_vendas():

    @task
    def extrair_dados():
        from extract.fic_data import extract_fic_data

        return str(extract_fic_data())

    @task
    def carregar_sql(csv_path: str):
        from load.to_sql import load_to_sql

        load_to_sql(csv_path)

    @task
    def executar_dbt_seed():
        subprocess.run(
            [
                "dbt",
                "seed",
                "--project-dir",
                str(PROJECT_ROOT / "dbt_vendas"),
            ],
            check=True,
        )

    @task
    def executar_dbt_run():
        subprocess.run(
            [
                "dbt",
                "run",
                "--project-dir",
                str(PROJECT_ROOT / "dbt_vendas"),
            ],
            check=True,
        )

    @task
    def executar_dbt_test():
        subprocess.run(
            [
                "dbt",
                "test",
                "--project-dir",
                str(PROJECT_ROOT / "dbt_vendas"),
            ],
            check=True,
        )

    csv_path = extrair_dados()
    carga = carregar_sql(csv_path)
    seed = executar_dbt_seed()
    run = executar_dbt_run()
    test = executar_dbt_test()

    csv_path >> carga >> seed >> run >> test


pipeline_vendas()