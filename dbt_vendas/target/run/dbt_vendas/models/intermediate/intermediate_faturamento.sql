USE [VENDAS];
    
    

    

    USE [VENDAS];
    EXEC('
        CREATE OR ALTER VIEW "dbo"."intermediate_faturamento" AS SELECT
    id_compra,
    produto,
    preco,
    forma_pagto,
    data_hora,
    vendedor,
    loja
FROM "VENDAS"."dbo"."intermediate_vendas_enriquecidas";
    ')

