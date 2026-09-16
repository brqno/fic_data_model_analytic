SELECT
    vendedor,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total
FROM {{ ref('intermediate_faturamento') }}
GROUP BY vendedor