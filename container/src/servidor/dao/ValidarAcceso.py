import logging
import psycopg2
import bcrypt

# Configurar logging
logging.basicConfig(
    filename='eventos.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Conexión a la base de datos PostgreSQL
def conectar_postgres():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="Proyecto_Raspberry",
            user="1234",
            password="1234"
        )
        conexion.autocommit = True
        return conexion
    except psycopg2.Error as e:
        logging.error(f"Error al conectar a PostgreSQL: {e}")
        return None

# Insertar log de acceso en la base de datos
def insertar_log_acceso(cursor, usuario, acceso):
    try:
        cursor.execute("""
        INSERT INTO logs_acceso (usuario, acceso) 
        VALUES (%s, %s)
        """, (usuario, acceso))
        logging.info(f"Log de acceso registrado para {usuario}. Acceso {'concedido' if acceso else 'denegado'}.")
    except psycopg2.Error as e:
        logging.error(f"Error al insertar log de acceso: {e}")

# Función para registrar un nuevo usuario
def registrar_usuario(nombre, contrasena):
    # Generar el hash de la contraseña
    hash_contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    conexion = conectar_postgres()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
            INSERT INTO usuarios (nombre, contraseña) 
            VALUES (%s, %s)
            """, (nombre, hash_contrasena))
            conexion.commit()
            logging.info(f"Usuario '{nombre}' registrado exitosamente.")
        except psycopg2.Error as e:
            logging.error(f"Error al registrar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

# Validar acceso de usuario
def validar_acceso(nom_usuario, contrasena):
    conexion = conectar_postgres()
    if conexion:
        try:
            cursor = conexion.cursor()

            # Llamar a la función SQL validar_acceso
            cursor.execute(
                """
                SELECT validar_acceso(%s, %s);
                """,
                (nom_usuario, contrasena)
            )
            resultado = cursor.fetchone()[0]

            # Insertar log de acceso según el resultado
            if resultado:
                logging.info(f"Acceso concedido al usuario '{nom_usuario}'.")
                insertar_log_acceso(cursor, nom_usuario, True)
            else:
                logging.warning(f"Acceso denegado para '{nom_usuario}'.")
                insertar_log_acceso(cursor, nom_usuario, False)

            conexion.commit()

        except psycopg2.Error as e:
            logging.error(f"Error al ejecutar la función en la base de datos: {e}")
        finally:
            cursor.close()
            conexion.close()
    else:
        logging.error("No se pudo conectar a la base de datos para validar el acceso.")