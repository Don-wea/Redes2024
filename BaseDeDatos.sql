-- Crear la base de datos

-- Conectarse a la nueva base de datos
\c proyecto_raspberry;

-- Crear tabla de usuarios
    id SERIAL PRIMARY KEY,
    nom_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasena VARCHAR(50) NOT NULL
);

-- Crear tabla de lista negra
    id SERIAL PRIMARY KEY,
    nom_usuario VARCHAR(50) UNIQUE NOT NULL
);

-- Crear tabla de logs para registrar todos los intentos de acceso
    id SERIAL PRIMARY KEY,
    nom_usuario VARCHAR(50),
    acceso_permitido BOOLEAN,
    mensaje TEXT,
    fecha TIMESTAMP DEFAULT NOW()
);

-- Función para pedir usuario y contraseña, validar acceso, y guardar todo en logs
DECLARE
    usuario_encontrado BOOLEAN;
    en_lista_negra BOOLEAN;
BEGIN
    -- Verificar si el usuario existe en la tabla de usuarios con la contraseña correcta
    SELECT TRUE INTO usuario_encontrado
    FROM usuarios
    WHERE nom_usuario = validar_acceso.nom_usuario AND contrasena = validar_acceso.contrasena;

    -- Verificar si el usuario está en la lista negra
    SELECT TRUE INTO en_lista_negra
    FROM lista_negra
    WHERE nom_usuario = validar_acceso.nom_usuario;

    -- Guardar el intento en logs dependiendo de si el acceso es permitido o denegado
    IF usuario_encontrado AND NOT en_lista_negra THEN
        INSERT INTO logs_acceso (nom_usuario, acceso_permitido, mensaje)
        VALUES (nom_usuario, TRUE, 'Acceso permitido');
        RAISE NOTICE 'Acceso permitido para el usuario %', nom_usuario;
    ELSE
        INSERT INTO logs_acceso (nom_usuario, acceso_permitido, mensaje)
        VALUES (nom_usuario, FALSE, 'Acceso denegado - Usuario no encontrado o en blacklist');
        RAISE NOTICE 'Acceso denegado para el usuario %', nom_usuario;
    END IF;
END;
$$ LANGUAGE plpgsql;