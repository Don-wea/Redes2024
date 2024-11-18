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
            
def mostrar_logs():
    try:
        # Conexión a la base de datos
        conexion = psycopg2.connect(
            host="localhost",
            database="proyecto_raspberry",
            user="tu_usuario",
            password="tu_password"
        )
        cursor = conexion.cursor()

        # Consultar los registros de logs_acceso
        cursor.execute("SELECT * FROM logs_acceso;")
        registros = cursor.fetchall()

        print("\n--- LOGS DE ACCESO ---")
        for registro in registros:
            print(registro)

    except psycopg2.Error as e:
        print(f"Error al consultar los logs: {e}")

    finally:
        # Cerrar conexión
        if conexion:
            cursor.close()
            conexion.close()
