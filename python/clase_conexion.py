#LIBRERIAS 
import pyodbc 
import json 
import os
import sys
from datetime import datetime

#CLASE DE CONEXION A MICROSOFT ACCESS
class ConexionAccess:
    clave_conexion = "conexion"
#CONECTAR CON RUTA JSON
    def __init__(self,ruta,json_archivo):
        self.ruta = ruta
        self.json_archivo = json_archivo
#LERR ARCHIVO JSON
    def __leerJson__(self):
        with open(f'{self.ruta}{self.json_archivo}') as archivo:
            data = json.load(archivo)
        return data
#OBTENER EL DICCIONARIO DONDE ESTAN LOS PARAMETROS DE CONEXION
    def __ObtenerParams__(self):
        params = self.__leerJson__()[self.clave_conexion]
        return params
#CONECTAR CON MICROSOFT ACCESS
    def conectar(self,mostrar_mensaje=True):
        params = self.__ObtenerParams__()
        driver = params['driver']
        db_file = params['db_file']
        source = params['source']
        conn_str = f'DRIVER={driver};DBQ={db_file}'+f'/{source}'

        try:
            conn=pyodbc.connect(conn_str)
            cursor = conn.cursor()
            if mostrar_mensaje:
                print('Estas conectado a access!')
            return cursor, conn
        except:
            raise 'Revisar el string de conexión'
#CERRAR CONEXION CON ACCESS    
    def cerrar_conexion(self):
        _, conn = self.conectar(mostrar_mensaje=False)
        try:
            conn.close()
            print("Conexión cerrada!")
        except:
            raise 'ha ocurrido un error'


class EjecutarSQL:
#CONECTAR CON RUTA JSON
    def __init__(self,ruta_sql,json_archivo,cursor,clave_consulta):
        self.ruta_sql = ruta_sql
        self.json_archivo = json_archivo
        self.cursor = cursor
        self.clave_consulta = clave_consulta
#LERR ARCHIVO JSON   
    def __leerJson__(self):
        with open(f'{self.ruta_sql}{self.json_archivo}') as archivo:
            data = json.load(archivo)
        return data 
#OBTENER EL DICCIONARIO DONDE ESTAN LOS PARAMETROS DE CONEXION
    def __ObtenerParams__(self):
        params = self.__leerJson__()[self.clave_consulta]
        return params
    
    def __ExtraerConsultas__(self):
        rutas_sql = self.__ObtenerParams__()
        rutas_sql = rutas_sql['ruta_raiz']
        sql = sorted(os.listdir(rutas_sql))
        return rutas_sql,sql 
    
    def __Logs__(self):
        stdout = sys.stdout
        log_file = open('archivo.log','w')
        sys.stdout = log_file
        fecha_actual = datetime.now()
        print('fecha actual: ', fecha_actual.strftime("%Y%m%d %H:%M:%S"))
        sys.stdout = stdout
        log_file.close()
    
    def EjecutarSQL(self):
        rutas_sql,sql = self.__ExtraerConsultas__()
        self.__Logs__()
        for i in sql:
            with open('{}/{}'.format(rutas_sql,i), 'r') as archivo:
                contenido = archivo.read()
                print(contenido)
                self.cursor.execute(contenido)
    
