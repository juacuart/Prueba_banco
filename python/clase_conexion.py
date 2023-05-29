#LIBRERIAS 
import pyodbc 
import json 
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

        
"""
ruta = os.getcwd()
archivo_json = '\parametros.json'
datos = ConexionAccess(ruta,archivo_json)
cursor, _ = datos.conectar()
"""
"""
cursor.execute('select * from Tarjetas')
rows = cursor.fetchall()
for row in rows:
    print(row)
"""