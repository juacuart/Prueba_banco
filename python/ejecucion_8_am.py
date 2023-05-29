from clase_conexion import ConexionAccess
from clase_conexion import EjecutarSQL
import os

ruta = os.getcwd()
archivo_json = '\python\parametros.json'
datos = ConexionAccess(ruta,archivo_json)
cursor, conn = datos.conectar()

ejecutar = EjecutarSQL(ruta,archivo_json,cursor,'consultas_8_am')
ejecutar.EjecutarSQL()

conn.close()