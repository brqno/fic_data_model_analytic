SELECT DISTINCT
    sigla_estado,
    nome_estado,
    regiao,
    ordem_regiao
FROM {{ ref('intermediate_vendas_enriquecidas') }}