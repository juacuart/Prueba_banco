
select
Clientes.segmento
,COUNT(Clientes.segmento)
INTO punto3
from Tarjetas inner join Clientes on
val(Tarjetas.TJNRODOC) = val(Clientes.NUM_DOC)
WHERE
val(Clientes.COD_TIPO_DOC) = val(Tarjetas.tjclsdoc) AND
Tarjetas.tjtpotrj = 'TARJETA DEBITO MAESTRO'
group by lientes.segmento
ORDER BY COUNT(Clientes.SEGMENTO) DESC