SELECT
    regiao,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total,
    AVG(preco) AS ticket_medio
FROM "VENDAS"."dbo"."intermediate_vendas_enriquecidas"
GROUP BY regiao