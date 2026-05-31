# ============================================
# GLOBAL HEALTH MONITOR
# Schritt 2: Daten bereinigen & für Power BI vorbereiten
# ============================================

import pandas as pd

print("🧹 Datenbereinigung startet...")

# ── Rohdaten laden ───────────────────────────
df = pd.read_csv("data/health_rohdaten.csv")
print(f"📥 Rohdaten geladen: {len(df)} Zeilen")

# ── Schritt 1: Regionen entfernen ────────────
# Die API liefert auch "Regionen" wie "World", "Europe" etc.
# Wir wollen nur echte Länder behalten
# Echte Länder haben einen 3-buchstabigen Code
keine_laender = [
    "World", "Europe & Central Asia",
    "Sub-Saharan Africa", "South Asia",
    "North America", "Middle East & North Africa",
    "Latin America & Caribbean", "East Asia & Pacific",
    "European Union", "OECD members",
    "High income", "Low income",
    "Middle income", "Low & middle income",
    "Africa Eastern and Southern", "Africa Western and Central",
    "Early-demographic dividend", "Late-demographic dividend",
    "Pre-demographic dividend", "Post-demographic dividend",
    "Fragile and conflict affected situations",
    "Heavily indebted poor countries (HIPC)",
    "Least developed countries: UN classification",
    "Small states", "Other small states",
    "Pacific island small states", "Caribbean small states",
    "IDA & IBRD total", "IDA total", "IBRD only",
    "IDA only", "IDA blend", "Not classified"
]

df_sauber = df[~df["Land"].isin(keine_laender)]
print(f"🌍 Nach Filterung: {df_sauber['Land'].nunique()} echte Länder")

# ── Schritt 2: Ländercode bereinigen ─────────
# Nur Codes mit genau 3 Buchstaben behalten
df_sauber = df_sauber[df_sauber["Ländercode"].str.len() == 3]

# ── Schritt 3: Pivot-Tabelle erstellen ───────
# Statt jeder Indikator in einer eigenen Zeile
# → jeder Indikator bekommt eine eigene Spalte
# (Power BI arbeitet besser damit)

df_pivot = df_sauber.pivot_table(
    index=["Land", "Ländercode", "Jahr"],
    columns="Indikator",
    values="Wert"
).reset_index()

# Spaltenname-Index entfernen (technisches Detail)
df_pivot.columns.name = None

print(f"📊 Pivot-Tabelle erstellt: {df_pivot.shape[0]} Zeilen, {df_pivot.shape[1]} Spalten")

# ── Schritt 4: Zeitstempel hinzufügen ────────
from datetime import datetime
df_pivot["Letzte_Aktualisierung"] = datetime.now().strftime("%d.%m.%Y %H:%M")

# ── Schritt 5: Speichern ─────────────────────
speicherpfad = "data/health_dashboard_data.csv"
df_pivot.to_csv(speicherpfad, index=False, encoding="utf-8-sig")

# ── Zusammenfassung ──────────────────────────
print("")
print("=" * 45)
print("✅ BEREINIGUNG ABGESCHLOSSEN!")
print("=" * 45)
print(f"🌍 Länder:    {df_pivot['Land'].nunique()}")
print(f"📋 Spalten:   {list(df_pivot.columns)}")
print(f"📁 Datei:     {speicherpfad}")
print("=" * 45)

# ── Vorschau der ersten 5 Zeilen ─────────────
print("\n📋 Vorschau (erste 5 Zeilen):")
print(df_pivot.head())