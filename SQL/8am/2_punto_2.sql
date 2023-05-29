
select
catalogo_clase.desc_clase
,COUNT(tarjetas.tjesttrj)
INTO punto2
from tarjetas inner join catalogo_clase on
val(tarjetas.tjclstrj) = val(catalogo_clase.clase)
where  tarjetas.tjtpotrj = 'TARJETA MASTERDEBIT' AND tarjetas.tjesttrj != 'ACTIVA'
group by 1
;