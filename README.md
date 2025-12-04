# SmartWeather

SmartWeather ist ein einfaches Python-Projekt zur Verwaltung
verschiedener Wettersensoren. Das Projekt demonstriert objektorientierte
Programmierung durch die Implementierung einer Basisklasse `Sensor`
sowie spezifischen Sensorklassen wie `HumiditySensor`, `TempSensor` und
`WindSensor`.

## Inhalt

-   Überblick
-   Struktur
-   Installation
-   Verwendung
-   Beispielcode
-   Klassenbeschreibung
-   Lizenz

## Überblick

SmartWeather ermöglicht das einfache Anlegen und Anzeigen von
verschiedenen Sensoren. Jeder Sensor besitzt: - einen Namen (`name`) -
eine Einheit (`unit`) - einen Messwert (`value`)

Die Basisklasse `Sensor` dient als Grundlage für spezialisierte
Sensoren.

## Struktur

    SmartWeather/
    │
    ├── Sensors/
    │   └── Sensor.py
    │   └── HumiditySensor.py
    │   └── TempSensor.py
    │   └── WindSensor.py
    |
    ├── Interface/
    │   └── APISource.py
    │   └── Source.py
    │   └── TestSource.py
    |
    ├── Station/
    │   └── WeatherStation.py
    |
    └── Main.py

## Installation

1.  Projektverzeichnis klonen oder herunterladen.
2.  Sicherstellen, dass Python 3 installiert ist.
3.  Das Projekt in Ihrer Arbeitsumgebung öffnen.

## Verwendung

Sie können Instanzen der Sensorsubklassen erstellen und deren Daten mit
der Methode `showdata()` ausgeben.

## Beispielcode

``` python
from HumiditySensor import HumiditySensor
from TempSensor import TempSensor
from WindSensor import WindSensor

class Main:
    if __name__ == "__main__":
        temp = TempSensor("Temperatur-Sensor", "Celsius", 31)
        wind = WindSensor("Wind-Sensor", "km/h", 45)
        humidity = HumiditySensor("Feuchtigkeits-Sensor", "%", 95)
        
        sensors = [temp, wind, humidity]
        for s in sensors
            s.showdata()
```

## Klassenbeschreibung

### Sensor (Basisklasse)

-   **Attribute:**
    -   `__name` -- Name des Sensors
    -   `__unit` -- Einheit des Messwerts
    -   `__value` -- Messwert
-   **Methoden:**
    -   `showdata()` -- Gibt Name, Einheit und Messwert aus.

### HumiditySensor

Erbt von `Sensor`. Repräsentiert einen Luftfeuchtigkeitssensor.

### TempSensor

Erbt von `Sensor`. Repräsentiert einen Temperatursensor.

### WindSensor

Erbt von `Sensor`. Repräsentiert einen Windsensor.

## Lizenz

Ich bsetzte das Patent A, B, C und die 6
