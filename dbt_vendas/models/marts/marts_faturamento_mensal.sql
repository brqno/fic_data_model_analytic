SELECT
    ano_venda,
    mes_venda,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total
FROM {{ ref('intermediate_datas') }}
GROUP BY
    ano_venda,
    mes_venda