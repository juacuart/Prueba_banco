CREATE TABLE PROCESO.PUNTO3 AS
with t1 as (
select
num_doc,
cod_tipo_doc,
edad_cli,
segmento,
ciudad_residencia,
genero_cli
from proceso.ppclientes
group by 1,2,3,4,5,6
),
t2 as (
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
SEGMENTO
,COUNT(SEGMENTO) as cantidad
from t2 inner join t1  on
TJNRODOC = NUM_DOC AND
COD_TIPO_DOC = tjclsdoc AND
tjtpotrj = "TARJETA DEBITO MAESTRO"
group by 1
ORDER BY COUNT(SEGMENTO) DESC