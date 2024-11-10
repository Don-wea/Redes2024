# <img src="assets/img/logo.png" alt="raspe logo" width="64"/> REDES 2024 <img src="assets/img/logo.png" alt="raspe logo" width="64"/>
Emitidor de senial wifi y filtrador de mensajes.

## <img src="assets/img/logo.png" alt="raspe logo" width="64"/> Requirements

### Windows
- Docker

### Unix
- Install Docker
```bash
chmod +x docker/prerequisites/setupDocker.sh
./docker/prerequisites/setupDocker.sh
```


## <img src="assets/img/logo.png" alt="raspe logo" width="64"/> Installation

### Unix

#### Crear Docker Images del servidor

- Configuracion
```bash
chmod +x docker/*.sh
sudo ./docker/setup.sh
```
- efectuar cambios en el code
```bash
sudo ./docker/build.sh
```

#### Crear Docker Images del cliente de prueba
- Configuracion
```bash
chmod +x client/docker/*.sh
sudo ./client/docker/setup.sh
```
- efectuar cambios en el code
```bash
sudo ./client/docker/build.sh
```

### Windows

nose

## <img src="assets/img/logo.png" alt="raspe logo" width="64"/> Execution

### Unix

- Arrancar el servidor
```bash
sudo ./docker/run.sh
```
- Arrancar el cliente de prueba
```bash
sudo ./client/docker/run.sh
```

### Windows

nose