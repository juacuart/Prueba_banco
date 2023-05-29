CREATE TABLE PROCESO.TARJETAS_ACTIVAS AS
WITH t1 AS (
SELECT 
tjnrodoc,
tjclsdoc,
tjnrotrj,
tjclstrj,
tjtpotrj,
tjesttrj
FROM proceso.PPtarjetas
INNER JOIN proceso.PPCuentas ON
tjnrotrj = canrotrj
AND tjettrj = "ACTIVA"
AND caestcta = "ACTIVA"
GROUP BY 1,2,3,4,5,6
)
SELECT * FROM t1