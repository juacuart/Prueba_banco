CREATE TABLE PROCESO.PUNTO1 AS
WITH t1 AS (
SELECT 
tjnrodoc,
tjclsdoc,
tjnrotrj,
tjclstrj,
tjtpotrj,
tjesttrj
FROM PROCESO.TARJETAS_ACTIVAS
)
SELECT 
desc_clase,
CAST(tjclstrj AS INT) AS clase,
COUNT(tjesttrj) AS cantidad
FROM T1
INNER JOIN proceso.clasespp ON
tjclstrj = clase
WHERE tjesttrj = "ACTIVA"
GROUP BY 1, 2
ORDER BY COUNT(tjesttrj) DESC