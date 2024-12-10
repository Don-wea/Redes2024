# <img src="container/assets/img/logo.png" alt="raspe logo" width="64"/> REDES 2024 <img src="container/assets/img/logo.png" alt="raspe logo" width="64"/>
Emitidor de senial wifi y filtrador de mensajes.

## <img src="container/assets/img/logo.png" alt="raspe logo" width="64"/> Requirements

### Windows
- Docker

### Unix
- Install Docker
```bash
chmod +x docker/prerequisites/setupDocker.sh
./docker/prerequisites/setupDocker.sh
```


## <img src="container/assets/img/logo.png" alt="raspe logo" width="64"/> Installation

### Unix

#### Crear Docker Images del servidor

- Configuracion
```bash
chmod +x docker/*.sh
sudo ./docker/setup.sh
```

#### Crear Docker Images del cliente de prueba
- Configuracion
```bash
chmod +x client/docker/*.sh
sudo ./client/docker/setup.sh
```

### Windows

nose

## <img src="container/assets/img/logo.png" alt="raspe logo" width="64"/> Execution

### Unix

- Arrancar el servidor
```bash
sudo ./docker/run.sh
```
- Arrancar el servidor en mode explorer
```bash
sudo ./docker/explorer.sh
```

- Arrancar el cliente de prueba
```bash
sudo ./client/docker/run.sh
```
- Arrancar el cliente de prueba en modo explorer
```bash
sudo ./client/docker/explorer.sh
```

### Windows

nose

## <img src="container/assets/img/logo.png" alt="raspe logo" width="64"/> Miscellaneous

### Unix

- Para ver todas las imagenes, volumenes, networks y containers actualmente ejecutandose en docker
```bash
sudo ./docker/check.sh
```

- Para eliminar toda instancia de docker que no este siendo utilizada
```bash
sudo ./docker/prune.sh
```

- Para revisar la lista de comandos de docker revisar archivo "docker/commands.txt"