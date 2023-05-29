CREATE TABLE PROCESO.punto2 AS
with t1 as (
select 
tjnrodoc,
tjclsdoc,
tjnrotrj,
tjclstrj,
tjtpotrj,
tjesttrj
from proceso.PPtarjetas
group by 1,2,3,4,5,6
)
select
desc_clase
,COUNT(tjesttrj) as cantidad
from t1 inner join proceso.ppclases on
tjclstrj = clase
where  tjtpotrj = "TARJETA MASTERDEBIT" AND tjesttrj != "ACTIVA"
group by 1
;