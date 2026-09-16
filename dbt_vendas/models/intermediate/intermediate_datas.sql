SELECT
	id_compra,
	data_hora,
	data_venda,
	ano_venda,
	mes_venda,
	nome_mes,
	trimestre,
	preco
FROM {{ ref('intermediate_vendas_enriquecidas') }}