from conexion import conectar

try:
    conexion = conectar()

    print("Conexion exitosa con MySQL")

    conexion.close()

except Exception as error:
    print("Error al conectar:", error)