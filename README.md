# Analyse von Zugriffsdaten | DAW SoSe 2023

- Autoren: Florian Lenz, Tom Seiffert
- Grundlage: Zur Vorbereitung wurde folgendes Lernmodul verwendet: https://projectbase.medien.hs-duesseldorf.de/eild.nrw-module/lernmodul-pandas

## Aufgaben

Die Datenbasis ist ein Auszug der Logdaten aus dem Zugriffslog eines Apache Webservers. Die Daten liegen in Form einer Textdatei vor.

1. Aufgabe: Analysieren Sie welche Produkte beliebt sind. Entwickeln Sie dazu eine Definition eines beliebten Produktes.
2. Aufgabe: Untersuchen Sie den Datensatz auf weitere Auffälligkeiten

## Setup

- Du benötigst Python3 in der 64-Bit-Version
- Du benötigst einige Packages (siehe `requirements.txt`)
  - Installiere alle Packages mit `pip install -r requirements.txt`
- Bevor es losgehen kann, brauchst du noch die **Datensets**.
  - Alle Datensets findest du auf [Sharepoint](https://fhd-my.sharepoint.com/:f:/g/personal/florian_lenz_study_hs-duesseldorf_de/ElsRv7-Cle9EqKOhQBtYK10BC4xY-UkdNeQ9n-YJVlF_GQ?e=MbV2gp).
  - Wir empfehlen die `access_log.csv`, das geht am schnellsten. Alternativ kannst du auch die anderen CSV-Dateien herunterladen. Diese enthalten verschiedene Zwischenstände.
  - Platziere die Daten in deinem `data/`-Ordner.

## Lösung Starten

Unsere Lösungen mit allen Schritten findet ihr im Notebook [`project.ipynb`](project.ipynb).  
Zusätzlich werden in der [`wip_ip.ipynb`](wip_ip.ipynb) die IP-Adressen analysiert. Hierfür benötigst du auch den `geo-city/`-Ordner ([Sharepoint](https://fhd-my.sharepoint.com/:f:/g/personal/florian_lenz_study_hs-duesseldorf_de/ElsRv7-Cle9EqKOhQBtYK10BC4xY-UkdNeQ9n-YJVlF_GQ?e=MbV2gp)) in deinem `data/`-Ordner.

### Lokal

Öffnet das Projekt / die Notebooks einfach in einer IDE deiner Wahl (z. B. VisualStudioCode): [`project.ipynb`](project.ipynb)

### Docker

Mithilfe der folgenden Befehle kann unsere Aufgabenlösung lokal in einem Docker Container gestartet werden:

```shell
docker build -t daw-zugriffsdaten-ss23:1.0 .
docker run -p 8888:8888 daw-zugriffsdaten-ss23:1.0
```

