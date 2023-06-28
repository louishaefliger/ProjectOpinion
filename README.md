# ProjectOpinion

Projektübersicht:
Das erstellte Gerät dient zur Meinungsabfrage zu einer definierten Umfrage. Durch einen Bewegungssensor wird festgestellt, ob sich ein Passant dem Gerät nähert. Der Passant wird durch eine aufleuchtende LED auf die Umfrage aufmerksam gemacht und kann anschliessend über die 4 Tasten seine Einschätzung zur Frage abgeben. Der Sensor hat nach dem Auslösen ein Delay von 30 Sekunden hinterlegt. Dem Betreiber des Gerätes steht ein Dashboard zur Verfügung, über welches manuell Rückmeldungen erfasst oder die Umfrage gestartet werden kann. Im Dashboard findet sich eine Übersicht der Rückmeldungen.
Hilfsmittel
•	Raspberry PI Pico W
•	Raspberry PI
•	Node RED
•	Motion PIR Sensor HC-SR501
•	Sidekick Developement Kit
Konfiguration Pico mit Sensor:
Der Pico verbindet sich über ein MicroPython-Script beim Bootvorgang automatisch mit dem WLAN und führt anschliessend der Sensorscript aus welches sich einerseits mit dem MQTT-Broker (Raspberry Pi) verbindet und in einer While True Schleife den Sensor nach Bewegung abfragt. Im Falle einer erkannten Bewegung wird per MQTT die Meldung „Motion Detected“ gesendet.
Konfiguration NodeRed
Über ein MQTT-IN-Node wird die erkannte Bewegung abgegriffen. Diese wird einerseits über eine Funktion umgewandelt und an ein Balkendiagramm des Dashboards für die Anzahl Erkennungen weitergeleitet und triggert andererseits über ein Exec-Node das Opinion-Python-Programm auf dem Raspberry PI. Die Ausgabe des Programms wird über eine Funktion, welche als Counter dient aufbereitet und im Dashboard als Diagramm aufgeführt.
Konfiguration Raspberry Pi
Auf dem Raspberry Pi ist ein Pythonscript, welches über NodeRed getriggert wird. Im Script sind die GPIO für die Taster und für die LED als Variabel, sowie die MQTT-Verbindung, das Setup der GPIO Pins, sowie alle Funktionen wie LED ein und Ausschalten, und das publizieren der Antworten initial definiert. In der eigentlichen While-True-Schlaufe wird lediglich auf das Bestätigen der Taste oder auf den Ablauf der 30 Sekunden gewartet um anschliessend die entsprechende Antwort (Sehr schlecht, Schlecht, Gut oder Sehr Gut) auszugeben. Anschliessend werden die GPIO-Ressourcen wieder freigegeben.
