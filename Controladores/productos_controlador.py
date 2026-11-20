from Database.conexion import conectar


def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_producto, nombre, categoria, precio, stock FROM productos")
    productos = cursor.fetchall()

    cursor.close()
    conexion.close()
    return productos


def registrar_producto(nombre, categoria, precio, stock):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO productos (nombre, categoria, precio, stock)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nombre, categoria, precio, stock)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()