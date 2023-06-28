#!/usr/bin/python3
# -*- coding: utf-8 -*-

######################################################
# Umfrage
# ==========
# Version 4.0 / 20230601
#
# Interpret: Louis Haefliger, louis.haefliger@edu.teko.ch
#
# Change Log:
# v01_00: Initial Version
# v02_00: Question
# v03_00: Pause
# v04_00: Simple Message
######################################################


# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# GPIO-Pins für LED und Taster
led_pin = 23
button_pin_1 = 18
button_pin_2 = 19
button_pin_3 = 20
button_pin_4 = 21

# MQTT-Verbindung
mqtt_broker = "host-t08b"
mqtt_topic = "umfrage/antworten"

# Setup der GPIO-Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED einschalten
GPIO.output(led_pin, GPIO.HIGH)

# Frage
question = "Wie zufrieden sind Sie mit der Teko?"

# MQTT-Client initialisieren
mqtt_client = mqtt.Client()

# Funktion zur Veröffentlichung der Antworten
def publish_answer(answer):
    if answer == 1:
        mqtt_client.publish(mqtt_topic, "Sehr schlecht")
    elif answer == 2:
        mqtt_client.publish(mqtt_topic, "Schlecht")
    elif answer == 3:
        mqtt_client.publish(mqtt_topic, "Gut")
    elif answer == 4:
        mqtt_client.publish(mqtt_topic, "Sehr Gut")
    elif answer == 0:
        mqtt_client.publish(mqtt_topic, "Keine Antwort")

# Funktion zum Ausschalten der LED
def turn_off_led():
    GPIO.output(led_pin, GPIO.LOW)

# Umfrage starten
# print("Umfrage gestartet!")

# Textausgabe der Frage
#print(question)

# Variable zur Überwachung der Zeit
start_time = time.time()

# Warte auf Tastenbetätigung oder Timeout nach 30 Sekunden
while True:
    if GPIO.input(button_pin_1) == GPIO.HIGH:
        print("Sehr schlecht")
        publish_answer(1)
        break

    if GPIO.input(button_pin_2) == GPIO.HIGH:
        print("Schlecht")
        publish_answer(2)
        break

    if GPIO.input(button_pin_3) == GPIO.HIGH:
        print("Gut")
        publish_answer(3)
        break

    if GPIO.input(button_pin_4) == GPIO.HIGH:
        print("Sehr Gut")
        publish_answer(4)
        break

    # Überprüfen, ob 30 Sekunden vergangen sind
    if time.time() - start_time >= 30:
        print("Keine Antwort")
        publish_answer(0)
        break

# Umfrage beendet

# GPIO-Ressourcen freigeben
GPIO.cleanup()
