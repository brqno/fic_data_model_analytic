SELECT
    vendedor,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total
FROM "VENDAS"."dbo"."intermediate_faturamento"
GROUP BY vendedor