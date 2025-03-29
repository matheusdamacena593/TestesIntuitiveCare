SELECT op.razao_social, SUM(rt.vl_saldo_final - rt.vl_saldo_inicial) AS despesa_total 
FROM operadoras_ativas op
INNER JOIN registros_trimestrais rt ON op.registro_ans = rt.reg_ans
WHERE rt.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
AND rt.data >= '2024-01-10'
AND rt.data < '2025-01-01'
GROUP BY op.razao_social
ORDER BY despesa_total DESC
LIMIT 10;

SELECT op.razao_social, SUM(rt.vl_saldo_final - rt.vl_saldo_inicial) AS despesa_total
FROM operadoras_ativas op
INNER JOIN registros_trimestrais rt ON op.registro_ans = rt.reg_ans
WHERE rt.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
AND rt.data >= '2024-01-01'
AND rt.data < '2025-01-01'
GROUP BY op.razao_social
ORDER BY despesa_total DESC
LIMIT 10;