from clase_conexion import ConexionAccess
import os

ruta = os.getcwd()
archivo_json = '\parametros.json'
datos = ConexionAccess(ruta,archivo_json)
cursor, _ = datos.conectar()