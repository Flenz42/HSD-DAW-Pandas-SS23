# Analyse von Zugriffsdaten | DAW SoSe 2023

- Autoren: Florian Lenz, Tom Seiffert
- Grundlage: Zur Vorbereitung wurde folgendes Lernmodul verwendet: https://projectbase.medien.hs-duesseldorf.de/eild.nrw-module/lernmodul-pandas


## Aufgaben

Die Datenbasis ist ein Auszug der Logdaten aus dem Zugriffslog eines Apache Webservers. Die Daten liegen in Form einer Textdatei vor.

1. Aufgabe: Analysieren Sie welche Produkte beliebt sind. Entwickeln Sie dazu eine Definition eines beliebten Produktes.
2. Aufgabe: Untersuchen Sie den Datensatz auf weitere Auffälligkeiten

## Lösung Starten

Mithilfe der folgenden Befehle kann unsere Aufgabenlösung lokal in einem Docker Container gestartet werden:

ToDo: Befehle Anpassen!

```
docker build -t daw-zugriffsdaten-ss23:1.0 .
docker run -p 8888:8888 daw-zugriffsdaten-ss23:1.0
```
