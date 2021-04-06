import sqlite3
from pathlib import Path
#dbFolder = Path("c:/Users/Usuario/Documents/UNIVERSIDAD/PYTHON/PROGRAMAS/BASE DE DATOS")
#miConexion =  sqlite3.connect(dbFolder / "Datos1")
#estas lineas estan comentadas en caso de que quieras editar donde se genera la base de datos
miConexion =  sqlite3.connect("Datos1")
miCursor = miConexion.cursor()
miCursor.execute("CREATE TABLE CUENTAS (ID INTEGER PRIMARY KEY AUTOINCREMENT ,USUARIO VARCHAR(50), CONTRASEÑA VARCHAR(20))")
def basedatos(valores):
    miCursor.execute("INSERT INTO CUENTAS VALUES(NULL,?,?)",valores)
    miConexion.commit()
def eliminar(nombre):
    miCursor.execute("DELETE FROM CUENTAS WHERE USUARIO = ?",(nombre,))
    miConexion.commit()
def remplazar(nuevacontra,name):
    query = """ UPDATE CUENTAS
                SET CONTRASEÑA = ?
                WHERE USUARIO = ? """
    data = (nuevacontra,name)
    miCursor.execute(query,data)
    miConexion.commit()
i=0 
Datos = []
while i == 0 :
    print(">> 1. Crear Cuenta")
    print(">> 2. Eliminar Cuenta")
    print(">> 3. Cambiar Contraseña")
    print(">> 4. Imprimir Base de datos")
    print(">> 5. Terminar Programa")
    x = int(input("Escoga una opcion entrando el numero :"))
    if x == 1:
        Usuario = input("Ingrese Un Usuario: ")
        Contraseña = input("Ingrese Una Contraseña: ") 
        Datos = (Usuario,Contraseña)
        basedatos(Datos)
    elif x == 2:
        nombre = input("ingrese el nombre del usuario que quiere eliminar la cuenta: ")
        eliminar(nombre)
        print("cuenta eliminada con exito")
    elif x == 3:
        name = input("ingrese el usuario que quiere cambiar la contraseña: ")
        nueva = input("ingrese la nueva contraseña: ")
        remplazar(nueva,name)
        print("Contraseña Actualizada")
    elif x == 4:
        print("Base de Datos Actual")
        miCursor.execute("SELECT *FROM CUENTAS")
        cuentas = miCursor.fetchall()
        for n in cuentas:
            print(n)
    elif x == 5:
        print("termino el programa")
        miConexion.close()
        break    

