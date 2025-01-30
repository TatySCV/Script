import pymysql

# Configuración de la conexión a la base de datos
db_config = {
    "host": "teraflex-databases.cd2ko8oc2p2w.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "Teraf2024.",
    "database": "porticos-prod"  # Reemplaza con el nombre real de tu BD
}

# Prefijo a agregar a las imágenes
prefix_url = "https://process-image-portix.s3.us-east-1.amazonaws.com/"

try:
    # Conexión a la base de datos
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # Actualiza absolutamente todos los registros
    update_query = """
        UPDATE aplicacion_registro 
        SET imagen = CONCAT(%s, imagen)
    """
    cursor.execute(update_query, (prefix_url,))

    # Confirmar cambios en la BD
    connection.commit()
    print(f"✅ {cursor.rowcount} registros actualizados correctamente.")

except pymysql.MySQLError as e:
    print(f"❌ Error en la base de datos: {e}")

finally:
    # Cerrar conexión
    if connection:
        cursor.close()
        connection.close()