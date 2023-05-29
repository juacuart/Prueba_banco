
SELECT 
CATALOGO_CLASE.desc_clase,
tarjetas.tjclstrj,
tarjetas.tjesttrj
INTO punto1
FROM TARJETAS_ACTIVAS
INNER JOIN CATALOGO_CLASE ON
val(tjclstrj) = val(clase)
GROUP BY 1, 2
ORDER BY COUNT(tarjetas.tjesttrj) DESC