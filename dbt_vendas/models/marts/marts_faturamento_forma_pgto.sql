SELECT
    forma_pagto,
    COUNT(*) AS quantidade_vendas,
    SUM(preco) AS faturamento_total
FROM {{ ref('intermediate_vendas_enriquecidas') }}
GROUP BY forma_pagto