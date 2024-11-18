DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'proyecto_raspberry'
   ) THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE proyecto_raspberry');
   END IF;
END
$$;

-- Seleccionar la base de datos
\c proyecto_raspberry;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nom_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasena VARCHAR(50) NOT NULL
);

-- Crear tabla de lista negra
CREATE TABLE IF NOT EXISTS blacklist (
    id SERIAL PRIMARY KEY,
    nom_usuario VARCHAR(50) UNIQUE NOT NULL
);

-- Crear tabla de logs
CREATE TABLE IF NOT EXISTS logs_acceso (
    id SERIAL PRIMARY KEY,
    nom_usuario VARCHAR(50),
    acceso_permitido BOOLEAN,
    mensaje TEXT,
    fecha TIMESTAMP DEFAULT NOW()
);