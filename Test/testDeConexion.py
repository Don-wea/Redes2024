import os
import time

def conectar_wifi(ssid, password):
    # Crear o modificar el archivo de configuración de wpa_supplicant
    wpa_config = f"""
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={{
        ssid="{ssid}"
        psk="{password}"
        key_mgmt=WPA-PSK
    }}
    """

    # Guardar el archivo de configuración
    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as file:
        file.write(wpa_config)

    # Reiniciar el servicio de red para aplicar los cambios
    os.system('sudo wpa_cli -i wlan0 reconfigure')
    print(f"Intentando conectar a la red {ssid}...")

    # Esperar unos segundos para darle tiempo a la Raspberry Pi a conectarse
    time.sleep(10)

def verificar_conexion():
    # Intentar hacer 5 pings a 8.8.8.8 para verificar la conexión
    response = os.system('ping -c 5 8.8.8.8')

    if response == 0:
        print("Conexión exitosa a la red y a Internet.")
    else:
        print("No se pudo establecer la conexión a Internet.")

if __name__ == '__main__':
    ssid = input("Ingresa el nombre de la red Wi-Fi (SSID): ")
    password = input("Ingresa la contraseña de la red Wi-Fi: ")

    conectar_wifi(ssid, password)
    verificar_conexion()
