SELECT DISTINCT
tjnrodoc,
tjclsdoc,
tjnrotrj,
tjclstrj,
tjtpotrj,
tjesttrj
INTO TARJETAS_ACTIVAS
FROM tarjetas
INNER JOIN Cuentas ON
val(tarjetas.tjnrotrj) = val(cuentas.canrotrj)
where tjesttrj = 'ACTIVA'
AND caestcta = 'ACTIVA'
