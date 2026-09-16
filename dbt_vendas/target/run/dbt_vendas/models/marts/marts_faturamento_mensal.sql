USE [VENDAS];
    
    

    

    USE [VENDAS];
    EXEC('
        CREATE OR ALTER VIEW "dbo"."marts_faturamento_mensal" AS SELECT
    ano_venda,
    mes_venda,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total
FROM "VENDAS"."dbo"."intermediate_datas"
GROUP BY
    ano_venda,
    mes_venda;
    ')

