SELECT
    produto,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total,
    AVG(preco) AS preco_medio
FROM {{ ref('intermediate_vendas_enriquecidas') }}
GROUP BY produto