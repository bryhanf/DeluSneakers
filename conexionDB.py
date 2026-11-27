
import psycopg2


def obtener_conexion():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port="5432",
            database="DeluSneakers",
            user="postgres",
            password="emmanames"
        )

        return conexion

    except psycopg2.Error as error:
        print("Error al conectar con PostgreSQL:", error)
        return None


def probar_conexion():
    conexion = obtener_conexion()

    if conexion is not None:
        print("¡Conexión exitosa con PostgreSQL!")
        conexion.close()
        return True

    return False


def obtener_productos():
    conexion = obtener_conexion()

    if conexion is None:
        return []

    cursor = conexion.cursor()

    consulta = """
        SELECT
            p.id_producto,
            p.nombre_producto,
            pr.empresa AS marca,
            c.nombre_categoria AS categoria,
            p.genero_producto::text AS genero,
            p.precio,
            COALESCE(SUM(tp.stock_talla), 0)::INTEGER AS stock_total

        FROM productos p

        INNER JOIN proveedores pr
            ON p.id_proveedor = pr.id_proveedor

        INNER JOIN categorias c
            ON p.id_categoria = c.id_categoria

        LEFT JOIN tallas_productos tp
            ON p.id_producto = tp.id_producto

        GROUP BY
            p.id_producto,
            pr.empresa,
            c.nombre_categoria

        ORDER BY p.id_producto;
    """

    try:
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        # Obtener los nombres de las columnas
        columnas = [columna[0] for columna in cursor.description]

        # Convertir los resultados en diccionarios
        productos = [
            dict(zip(columnas, fila))
            for fila in resultados
        ]

        return productos

    except psycopg2.Error as error:
        print("Error al consultar productos:", error)
        return []

    finally:
        cursor.close()
        conexion.close()


if __name__ == "__main__":

    if probar_conexion():

        productos = obtener_productos()

        print("\nPRODUCTOS REGISTRADOS EN DELUSNEAKERS")
        print("--------------------------------------")

        for producto in productos:
            print(
                f"ID: {producto['id_producto']} | "
                f"Nombre: {producto['nombre_producto']} | "
                f"Marca: {producto['marca']} | "
                f"Categoría: {producto['categoria']} | "
                f"Precio: ${producto['precio']} | "
                f"Stock: {producto['stock_total']}"
            )

        print("\nTotal de productos:", len(productos))
