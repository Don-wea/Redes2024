import psycopg2
from psycopg2 import sql

def validar_acceso(nom_usuario, contrasena):
    try:
        # Conexión a la base de datos PostgreSQL
        conexion = psycopg2.connect(
            host="localhost",        
            database="proyecto_raspberry",
            user="1234",      
            password="1234"  
        )
        cursor = conexion.cursor()

        # Llamar a la función SQL validar_acceso
        cursor.execute(
            """
            SELECT validar_acceso(%s, %s);
            """,
            (nom_usuario, contrasena)
        )

        # Confirmar la ejecución (solo si se modifica algo)
        conexion.commit()

        print(f"Validación completada para el usuario '{nom_usuario}'. Revisa los logs en la tabla 'logs_acceso'.")

    except psycopg2.Error as e:
        print(f"Error al ejecutar la función en la base de datos: {e}")

    finally:

        if conexion:
            cursor.close()
            conexion.close()
def insertar_datos_desde_json(cursor, archivo_json):
    try:
        with open(archivo_json, 'r') as archivo:
            datos = json.load(archivo)

        # Insertar datos en la tabla `usuarios`
        for usuario in datos['usuarios']:
            cursor.execute("""
            INSERT INTO usuarios (nom_usuario, contrasena)
            VALUES (%s, %s)
            ON CONFLICT (nom_usuario) DO NOTHING;
            """, (usuario['nom_usuario'], usuario['contrasena']))

        # Insertar datos en la tabla `blacklist`
        for usuario in datos['blacklist']:
            cursor.execute("""
            INSERT INTO blacklist (nom_usuario)
            VALUES (%s)
            ON CONFLICT (nom_usuario) DO NOTHING;
            """, (usuario['nom_usuario'],))

        print("Datos insertados exitosamente desde el archivo JSON.")
    except Exception as e:
        print(f"Error al insertar datos desde JSON: {e}")

if __name__ == "__main__":
    try:
        # Conexión a la base de datos PostgreSQL
        conexion = psycopg2.connect(
            host="localhost",
            database="proyecto_raspberry",
            user="1234",
            password="1234"
        )
        cursor = conexion.cursor()

        # Validar acceso para un usuario específico
        nom_usuario = "test_user"
        contrasena = "test_password"
        validar_acceso(nom_usuario, contrasena)

        # Insertar datos desde un archivo JSON
        archivo_json = "datos.json"  # Ruta al archivo JSON
        insertar_datos_desde_json(cursor, archivo_json)

        # Confirmar cambios
        conexion.commit()

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")

    finally:
        if conexion:
            cursor.close()
            conexion.close()