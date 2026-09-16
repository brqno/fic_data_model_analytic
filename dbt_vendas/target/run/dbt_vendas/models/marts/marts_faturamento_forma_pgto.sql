USE [VENDAS];
    
    

    

    USE [VENDAS];
    EXEC('
        CREATE OR ALTER VIEW "dbo"."marts_faturamento_forma_pgto" AS SELECT
    forma_pagto,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total
FROM "VENDAS"."dbo"."intermediate_vendas_enriquecidas"
GROUP BY forma_pagto;
    ')

