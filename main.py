from extract.fic_data import extract_fic_data
from load.to_sql import load_to_sql

# main feito para teste, podendo ser feita a extração e carregamento de dados a partir daqui, sem utilizar o Airflow

def main() -> None:
    print("Iniciando extração dos dados...")
    extract_fic_data()

    print("\nIniciando carga no banco de dados...")
    load_to_sql()

    print("\nPipeline finalizado com sucesso.")


if __name__ == "__main__":
    main()