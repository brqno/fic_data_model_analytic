SELECT
    B.[Id_Compra] AS id_compra,
    B.[Data] AS data_hora,
    CAST(B.[Data] AS DATE) AS data_venda,
    YEAR(B.[Data]) AS ano_venda,
    MONTH(B.[Data]) AS mes_venda,
    DATENAME(MONTH, B.[Data]) AS nome_mes,
    DATEPART(QUARTER, B.[Data]) AS trimestre,
    B.[Loja] AS loja,
    C.[Cidade] AS cidade,
    C.[Estado] AS sigla_estado,
    R.[estado] AS nome_estado,
    R.[regiao] AS regiao,
    R.[ordem_regiao] AS ordem_regiao,
    B.[Vendedor] AS vendedor,
    B.[Produto] AS produto,
    P.[ID] AS produto_id,
    P.[Preço] AS preco,
    B.[Cliente_Nome] AS cliente_nome,
    B.[Cliente_Genero] AS cliente_genero,
    B.[Forma_Pagto] AS forma_pagto
FROM {{ ref('staging_vendas') }} AS B
LEFT JOIN {{ ref('lojas') }} AS C
    ON B.[Loja] = C.[Cidade]
LEFT JOIN {{ ref('seed_regioes_estados') }} AS R
    ON C.[Estado] = R.[sigla]
LEFT JOIN {{ ref('produtos') }} AS P
    ON B.[Produto] = P.[Produto]
