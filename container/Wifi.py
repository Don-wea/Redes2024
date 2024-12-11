import os
import subprocess
import socket
import threading

NombreWifi = input("Ingrese un nombre para su red WIFI: ")
PasswordWifi = input(f"Ingrese la contraseña de su red '{NombreWifi}': ")



# Libera el wifi
os.system("sudo rfkill unblock wlan")

# Detiene los servicios del wifi
os.system("sudo systemctl stop NetworkManager")

#
os.system("sudo systemctl stop wpa_supplicant")

# Crear la interfaz de red virtual para el punto de acceso
os.system("sudo iw dev wlan0 interface add ap0 type __ap")

# Configurar la dirección IP y la máscara de subred
os.system("sudo ip addr add 192.168.4.1/24 dev ap0")

# Activar la interfaz de punto de acceso
os.system("sudo ip link set ap0 up")



# Crear un archivo de configuración para hostapd
with open("/etc/hostapd/hostapd.conf", "w") as f:
    f.write(f"""
interface=ap0
ssid={NombreWifi}
wpa_passphrase={PasswordWifi}
driver=nl80211
hw_mode=g
channel=6
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
""")

def init_hostapd():
        # Iniciar hostapd para crear el punto de acceso
        os.system("sudo hostapd /etc/hostapd/hostapd.conf")

def DHCP_DNS():
        # Configurar dnsmasq para proporcionar DHCP y DNS
        os.system("sudo dnsmasq -C /dev/null -kd -F 192.168.4.2,192.168.4.20 -i ap0 --bind-dynamic")

def rootIP():
        # Habilitar el reenvío de IP para permitir el acceso a Internet
        os.system("sudo sysctl net.ipv4.ip_forward=1")

def Nat():
        # Configurar NAT para el enrutamiento de paquetes
        os.system("sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")

hilo1 = threading.Thread(target = init_hostapd)
hilo2 = threading.Thread(target = DHCP_DNS)
hilo3 = threading.Thread(target = rootIP)
hilo4 = threading.Thread(target = Nat)

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
