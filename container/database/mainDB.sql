-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL  
);

-- Tabla de la Blacklist de usuarios
CREATE TABLE IF NOT EXISTS blacklist (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

-- Función para validar acceso de usuario
CREATE OR REPLACE FUNCTION validar_acceso(nom_usuario VARCHAR, contrasena VARCHAR)
RETURNS BOOLEAN AS $$
DECLARE
    en_blacklist BOOLEAN;
    es_valido BOOLEAN;
    hash_contrasena VARCHAR;
BEGIN
    -- Verificar si el usuario está en la lista negra
    SELECT EXISTS (
        SELECT 1 FROM blacklist WHERE nombre = nom_usuario
    ) INTO en_blacklist;

    IF en_blacklist THEN
        RETURN FALSE;
    END IF;

    -- Obtener el hash de la contraseña del usuario
    SELECT contraseña INTO hash_contrasena
    FROM usuarios WHERE nombre = nom_usuario;

    -- Verificar si la contraseña ingresada coincide con el hash almacenado
    IF hash_contrasena IS NULL THEN
        RETURN FALSE;
    END IF;

    -- Comparar la contraseña con el hash almacenado
    IF crypt(contrasena, hash_contrasena) = hash_contrasena THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;