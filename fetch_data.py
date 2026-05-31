# ============================================
# GLOBAL HEALTH MONITOR
# Schritt 1: Daten von der World Bank API holen
# ============================================

import requests
import pandas as pd
from datetime import datetime

print("🌍 Global Health Monitor startet...")
print("⏳ Verbinde mit World Bank API...")

# ── Was wollen wir abrufen? ──────────────────
# Das sind unsere 5 Gesundheits-Indikatoren
indikatoren = {
    "SP.DYN.LE00.IN":    "Lebenserwartung",
    "SH.MED.BEDS.ZS":    "Krankenhausbetten_pro_1000",
    "SH.XPD.CHEX.GD.ZS": "Gesundheitsausgaben_BIP",
    "SP.DYN.IMRT.IN":    "Kindersterblichkeit",
    "SH.MED.PHYS.ZS":    "Aerzte_pro_1000"
}

# ── Funktion: Daten für einen Indikator holen ─
def hole_daten(indikator_code, indikator_name):
    
    # Die Adresse der API
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indikator_code}"
    
    # Was wir der API mitteilen
    parameter = {
        "format":   "json",
        "per_page": 500,
        "mrv":      1        # mrv=1 bedeutet: nur neuester Wert
    }
    
    # Anfrage senden (wie beim Kellner bestellen)
    antwort = requests.get(url, params=parameter)
    
    # Antwort in lesbares Format umwandeln
    daten = antwort.json()
    
    # Ergebnisse sammeln
    ergebnisse = []
    
    for eintrag in daten[1]:  # daten[0] = Info, daten[1] = echte Daten
        if eintrag["value"] is not None:  # Nur wenn Wert vorhanden
            ergebnisse.append({
                "Land":          eintrag["country"]["value"],
                "Ländercode":    eintrag["countryiso3code"],
                "Jahr":          eintrag["date"],
                "Indikator":     indikator_name,
                "Wert":          eintrag["value"]
            })
    
    print(f"   ✅ {indikator_name}: {len(ergebnisse)} Länder geladen")
    return pd.DataFrame(ergebnisse)

# ── Alle 5 Indikatoren abrufen ───────────────
alle_daten = []

for code, name in indikatoren.items():
    df = hole_daten(code, name)
    alle_daten.append(df)

# ── Alles zusammenfügen ──────────────────────
gesamt_df = pd.concat(alle_daten, ignore_index=True)

# ── Zeitstempel hinzufügen ───────────────────
gesamt_df["Letzte_Aktualisierung"] = datetime.now().strftime("%d.%m.%Y %H:%M")

# ── Als CSV speichern ────────────────────────
speicherpfad = "data/health_rohdaten.csv"
gesamt_df.to_csv(speicherpfad, index=False, encoding="utf-8-sig")

# ── Zusammenfassung anzeigen ─────────────────
print("")
print("=" * 45)
print("✅ FERTIG! Hier die Zusammenfassung:")
print("=" * 45)
print(f"📊 Gesamte Datensätze:  {len(gesamt_df)}")
print(f"🌍 Anzahl Länder:       {gesamt_df['Land'].nunique()}")
print(f"📁 Gespeichert in:      {speicherpfad}")
print(f"🕐 Zeitpunkt:           {datetime.now().strftime('%d.%m.%Y %H:%M')}")
print("=" * 45)