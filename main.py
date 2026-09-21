from extract.fic_data import extract_fic_data
from load.to_sql import load_to_sql

# main utilizado como teste

def main() -> None:
    print("Iniciando extração dos dados...")
    extract_fic_data()

    print("\nIniciando carga no banco de dados...")
    load_to_sql()

    print("\nPipeline finalizado com sucesso.")


if __name__ == "__main__":
    main()
