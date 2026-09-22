import os
import urllib
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text


def load_to_sql(csv_path: str | Path | None = None) -> None:
    project_root = Path(__file__).resolve().parent.parent
    load_dotenv(project_root / ".env")

    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    driver = os.getenv("DB_DRIVER")
    encrypt = os.getenv("DB_ENCRYPT", "no")
    trust_server_certificate = os.getenv("DB_TRUST_SERVER_CERTIFICATE", "yes")

    if not all([server, database, driver]):
        raise ValueError("Variáveis DB_SERVER, DB_DATABASE e DB_DRIVER não foram configuradas no arquivo .env")

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    if os.getenv("AIRFLOW_CTX_DAG_ID") and not (user and password):
        raise ValueError(
            "DB_USER e DB_PASSWORD são obrigatórios para executar a carga no Airflow."
        )

    authentication = (
        f"UID={user};PWD={password};"
        if user and password
        else "Trusted_Connection=yes;"
    )

    params = urllib.parse.quote_plus(
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Encrypt={encrypt};"
        f"TrustServerCertificate={trust_server_certificate};"
        f"{authentication}"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    csv_path = Path(csv_path) if csv_path else project_root / "dataset" / "compras.csv"
    df = pd.read_csv(csv_path, decimal=",", sep=";")

    try:
        tabela = "Vendas"
        coluna_id = "Id_Compra"
        maior_id = -1

        if inspect(engine).has_table(tabela):
            with engine.connect() as conexao:
                maior_id = conexao.execute(
                    text(f"SELECT COALESCE(MAX([{coluna_id}]), -1) FROM [{tabela}]")
                ).scalar_one()

        df[coluna_id] = df[coluna_id].astype(int) + int(maior_id) + 1

        df.to_sql(
            tabela,
            con=engine,
            if_exists="append",
            index=False,
        )
        print("Dados importados para o banco.")

    except Exception as e:
        print(f"Erro ao inserir dados no banco: {e}")
        raise


if __name__ == "__main__":
    load_to_sql()
