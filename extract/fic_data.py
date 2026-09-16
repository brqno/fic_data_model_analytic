import random
from datetime import datetime, timedelta
from pathlib import Path

import names
import pandas as pd


def extract_fic_data() -> Path:
    pasta_dataset = Path(__file__).parent.parent / "dataset"
    pasta_dataset.mkdir(parents=True, exist_ok=True)

    pasta_seeds = Path(__file__).parent.parent / "dbt_vendas" / "seeds"
    pasta_seeds.mkdir(parents=True, exist_ok=True)

    lojas = [
        {
            "Estado": "SP",
            "Cidade": "São Paulo",
            "Vendedores": ["João Marcos", "Maria Antonia", "Pedro Almeida"],
        },
        {
            "Estado": "MG",
            "Cidade": "Belo Horizonte",
            "Vendedores": ["Lucas Bernardo", "Eduardo Silva", "Paola Luz"],
        },
        {
            "Estado": "RJ",
            "Cidade": "Rio de Janeiro",
            "Vendedores": ["Stephanie Riga", "Ricardo Bonfim", "Juliana Bonde"],
        },
        {
            "Estado": "RS",
            "Cidade": "Porto Alegre",
            "Vendedores": ["Diego Costa", "André Lima", "Breno Antônio"],
        },
        {
            "Estado": "SC",
            "Cidade": "Florianópolis",
            "Vendedores": ["Rafaela Alves", "Paulo André", "José Elias"],
        },
        {
            "Estado": "BA",
            "Cidade": "Salvador",
            "Vendedores": ["Pedro Alves", "Viviane Souza", "Elias Damasco"],
        },
    ]

    produtos = [
        {"ID": 1, "Produto": "Notebook", "Preço": 3500.00},
        {"ID": 2, "Produto": "Celular", "Preço": 2500.00},
        {"ID": 3, "Produto": "Monitor", "Preço": 500.00},
        {"ID": 4, "Produto": "Cadeira", "Preço": 1100.00},
        {"ID": 5, "Produto": "Mouse", "Preço": 150.00},
        {"ID": 6, "Produto": "Teclado", "Preço": 200.00},
    ]

    forma_pagto = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix", "Boleto"]
    genero_clientes = ["male", "female"]

    compras = []
    for _ in range(2000):
        loja = random.choice(lojas)
        vendedor = random.choice(loja["Vendedores"])
        produto = random.choice(produtos)
        hora_compra = datetime.now() - timedelta(
            days=random.randint(1, 365),
            hours=random.randint(-5, 5),
            minutes=random.randint(-30, 30),
        )
        genero_cliente = random.choice(genero_clientes)
        nome_cliente = names.get_full_name(genero_cliente)
        forma = random.choice(forma_pagto)

        compras.append(
            {
                "Data": hora_compra,
                "Id_Compra": 0,
                "Loja": loja["Cidade"],
                "Vendedor": vendedor,
                "Produto": produto["Produto"],
                "Cliente_Nome": nome_cliente,
                "Cliente_Genero": genero_cliente.replace("female", "feminino").replace("male", "masculino"),
                "Forma_Pagto": forma,
            }
        )

    df_compras = pd.DataFrame(compras).set_index("Data").sort_index()
    df_compras["Id_Compra"] = [i for i in range(len(df_compras))]

    df_lojas = pd.DataFrame(lojas)
    df_produtos = pd.DataFrame(produtos)

    csv_path = pasta_dataset / "compras.csv"
    df_compras.to_csv(csv_path, index=True, decimal=",", sep=";")
    df_lojas.to_csv(pasta_seeds / "lojas.csv", index=False)
    df_produtos.to_csv(pasta_seeds / "produtos.csv", index=False)

    print(f"Arquivo gerado em: {csv_path}")
    return csv_path


if __name__ == "__main__":
    extract_fic_data()

