import network

# WLAN-Verbindung konfigurieren
WIFI_SSID = "Enter SSID"
WIFI_PASSWORD = "Enter Password"

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Verbinde mit WLAN...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print("Verbunden mit WLAN")
    print("IP-Adresse:", sta_if.ifconfig()[0])

connect_wifi()

# Führen Sie das andere Skript aus
exec(open('Sensor_V1_1.py').read())
