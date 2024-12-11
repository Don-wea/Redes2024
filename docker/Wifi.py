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
