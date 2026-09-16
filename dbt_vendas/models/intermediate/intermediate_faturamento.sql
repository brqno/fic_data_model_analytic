SELECT
    id_compra,
    produto,
    preco,
    forma_pagto,
    data_hora,
    vendedor,
    loja
FROM {{ ref('intermediate_vendas_enriquecidas') }}