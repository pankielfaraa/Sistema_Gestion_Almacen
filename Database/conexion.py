import mysql.connector


def conectar():

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Luna260619f",
        database="sistema_almacen"
    )

    return conexion