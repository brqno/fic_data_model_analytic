USE [VENDAS];
    
    

    

    USE [VENDAS];
    EXEC('
        CREATE OR ALTER VIEW "dbo"."marts_vendas_vendedor" AS SELECT
    vendedor,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total
FROM "VENDAS"."dbo"."intermediate_faturamento"
GROUP BY vendedor;
    ')

