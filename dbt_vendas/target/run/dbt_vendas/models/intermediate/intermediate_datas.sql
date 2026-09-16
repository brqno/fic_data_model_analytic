USE [VENDAS];
    
    

    

    USE [VENDAS];
    EXEC('
        CREATE OR ALTER VIEW "dbo"."intermediate_datas" AS SELECT
	id_compra,
	data_hora,
	data_venda,
	ano_venda,
	mes_venda,
	nome_mes,
	trimestre,
	preco
FROM "VENDAS"."dbo"."intermediate_vendas_enriquecidas";
    ')

