###############################
# Sensor Detection
# Version 1.1 / 20230530
# 
# Interpret: Louis Haefliger, louis.haefliger@edu.teko.ch
# 
# Change Log:
# V1.0 Initial Setup
# V1.1 MQTT / PAUSE
#
###############################

import machine
import time
import umqtt.simple as mqtt

motion_sensor_pin = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
mqtt_client = mqtt.MQTTClient("pico_client", "host-Name")

def on_connect(client):
    print("Verbunden mit MQTT-Broker")

mqtt_client.on_connect = on_connect
mqtt_client.connect()

while True:
    if motion_sensor_pin.value() == 1:
        print ("Bewegung erkannt")
        mqtt_client.publish(b"motion_detection", b"motion detected")
        time.sleep(10)
    time.sleep(0.1)
