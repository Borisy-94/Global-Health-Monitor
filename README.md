# 🌍 Global Health Monitor

![Dashboard].(dashboard_preview.png)

## 📋 Projektbeschreibung

Live-Dashboard mit echten Gesundheitsdaten von 180+ Ländern 
via World Bank API – automatisch täglich aktualisiert.

**Datenbasis:** World Bank Open Data API  
**Länder:** 180+  
**Indikatoren:** 5 Gesundheitskennzahlen  
**Zeitraum:** Aktuellste verfügbare Jahresdaten

---

## 🛠️ Tech Stack

| Tool | Verwendung |
|------|-----------|
| **Python** | API-Abruf & Datenbereinigung |
| **Pandas** | Datenmanipulation & Transformation |
| **Requests** | World Bank API Anbindung |
| **Power BI** | Interaktives Dashboard (DAX, Karte, KPIs) |
| **Windows Task Scheduler** | Automatische tägliche Aktualisierung |

---

## 📊 Indikatoren

| Code | Indikator |
|------|-----------|
| SP.DYN.LE00.IN | Lebenserwartung bei Geburt |
| SP.DYN.IMRT.IN | Kindersterblichkeit (pro 1.000) |
| SH.XPD.CHEX.GD.ZS | Gesundheitsausgaben % BIP |
| SH.MED.BEDS.ZS | Krankenhausbetten pro 1.000 |
| SH.MED.PHYS.ZS | Ärzte pro 1.000 Einwohner |

---

## 🔍 Zentrale Erkenntnisse

### 🏆 Lebenserwartung weltweit
Globaler Durchschnitt: **73,97 Jahre**  
Spitzenreiter: Monaco (86,50) · San Marino (85,82) · Hong Kong (85,39)

### 👶 Kindersterblichkeit
Globaler Durchschnitt: **18,74 pro 1.000 Geburten**  
Zeigt deutliche Unterschiede zwischen Industrie- und Entwicklungsländern

### 💰 Gesundheitsausgaben vs. Lebenserwartung
Klarer positiver Zusammenhang sichtbar im Scatter Plot:  
Länder mit höheren Gesundheitsausgaben (% BIP) haben  
systematisch höhere Lebenserwartung

---

## 🔄 Wie es funktioniert

World Bank API (kostenlos, kein API-Key nötig)
↓
fetch_data.py – Daten abrufen (5 Indikatoren, 180+ Länder)
↓
clean_data.py – Regionen entfernen, Pivot-Tabelle erstellen
↓
health_dashboard_data.csv – für Power BI
↓
Power BI Dashboard – Live-Visualisierung
↓
Windows Task Scheduler – täglich automatisch aktualisiert

---

## 📊 Dashboard Features

- 🗺️ **Weltkarte** – Lebenserwartung nach Land (Bubble Map)
- 📊 **Top 10 Länder** – Balkendiagramm Lebenserwartung
- 📈 **Scatter Plot** – Gesundheitsausgaben vs. Lebenserwartung
- 🔢 **KPI Cards** – Globale Durchschnittswerte
- 🔍 **Slicer** – Filter nach Land und Jahr
- 🕐 **Live Stand** – Zeitstempel der letzten Aktualisierung

---

## 🚀 Installation & Reproduktion

```bash
# Repository klonen
git clone https://github.com/Borisy-94/GlobalHealthMonitor

# Libraries installieren
pip install requests pandas

# Daten abrufen
python scripts/fetch_data.py

# Daten bereinigen
python scripts/clean_data.py

# Power BI öffnen
# → data/health_dashboard_data.csv laden
```

---

## 📁 Projektstruktur

GlobalHealthMonitor/
│
├── 📁 scripts/
│   ├── fetch_data.py       ← API Abruf (World Bank)
│   └── clean_data.py       ← Datenbereinigung & Pivot
│
├── 📁 data/
│   └── health_dashboard_data.csv
│
├── 📁 screenshots/
│   └── dashboard_preview.png
│
└── README.md

---

## 💡 Warum World Bank API?

✅ Komplett kostenlos
✅ Kein API-Key erforderlich
✅ 180+ Länder weltweit
✅ Offizielle UN/WHO Datenbasis
✅ Jährlich aktualisiert

---

## 👨‍💻 Autor

**Boris Petamba** – Junior Data Analyst  
Hintergrund: Medizinische Laboranalyse → Data Analytics  
📧 borispetamba@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/borispetamba)  
💻 [GitHub](https://github.com/Borisy-94)
