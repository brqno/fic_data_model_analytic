USE [VENDAS];
    
    

    

    USE [VENDAS];
    EXEC('
        CREATE OR ALTER VIEW "dbo"."intermediate_estados" AS SELECT DISTINCT
    sigla_estado,
    nome_estado,
    regiao,
    ordem_regiao
FROM "VENDAS"."dbo"."intermediate_vendas_enriquecidas";
    ')

