import pandas as pd
import os

# Aktuellen Pfad ermitteln und Datei einlesen
current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, "walmart_sales.csv")

# CSV-Datei einlesen mit verbessertem Fehlerhandling
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Fehler: Datei '{file_path}' nicht gefunden.")
    exit()
except pd.errors.EmptyDataError:
    print(f"Fehler: Datei '{file_path}' ist leer.")
    exit()
except Exception as e:
    print(f"Unerwarteter Fehler beim Lesen der Datei: {e}")
    exit()

# Fehlende Werte prüfen und behandeln
if 'Weekly_Sales' in df.columns:
    df['Weekly_Sales'] = df['Weekly_Sales'].fillna(0)
else:
    print("Fehler: 'Weekly_Sales'-Spalte nicht in den Daten vorhanden.")
    exit()

# Konvertieren der 'Date'-Spalte in datetime-Format
if 'Date' in df.columns:
    try:
        df['Date'] = pd.to_datetime(
            df['Date'], format='%d-%m-%Y', errors='coerce')
        if df['Date'].isnull().any():
            print("Warnung: Ungültige Datumswerte gefunden. Diese werden entfernt.")
            df = df.dropna(subset=['Date'])
    except Exception as e:
        print(f"Fehler beim Konvertieren der 'Date'-Spalte: {e}")
        exit()
else:
    print("Fehler: 'Date'-Spalte nicht in den Daten vorhanden.")
    exit()

# Filtern eines bestimmten Zeitraums (Beispiel: Februar 2010)
df_filtered = df.loc[(df['Date'] >= '2010-02-01') &
                     (df['Date'] <= '2010-02-28')]

# Relevante Spalten extrahieren (Prüfung, ob Spalten vorhanden sind)
required_columns = ['Date', 'Store', 'Weekly_Sales',
                    'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"Fehler: Folgende erforderliche Spalten fehlen: {missing_columns}")
    exit()

df_relevant = df[required_columns]

# Monatliche Umsätze berechnen
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Weekly_Sales'].sum()

# Umsatz pro Store berechnen
store_sales = df.groupby('Store')['Weekly_Sales'].sum()

# Identifikation der Top 10 Stores nach Umsatz
top_stores = store_sales.sort_values(ascending=False).head(10)

# Kundendaten einlesen und mit Verkaufsdaten verknüpfen (Optional)
customer_file_path = os.path.join(current_path, "customer_data.csv")
if os.path.exists(customer_file_path):
    try:
        kunden_df = pd.read_csv(customer_file_path)
        if 'Store' not in kunden_df.columns:
            print(
                "Fehler: 'Store'-Spalte fehlt in den Kundendaten. Zusammenführung nicht möglich.")
            df_merged = df.copy()
        else:
            df_merged = df.merge(kunden_df, on="Store", how="left")
    except Exception as e:
        print(f"Fehler beim Lesen der Kundendaten: {e}")
        df_merged = df.copy()
else:
    df_merged = df.copy()
    print("Warnung: 'customer_data.csv' Datei nicht gefunden. Zusammenführung übersprungen.")

# Ergebnisse ausgeben
print("\nMonatlicher Umsatz:")
print(monthly_sales)
print("\nTop 10 Stores nach Gesamtumsatz:")
print(top_stores)
print("\nGefilterte Daten für Februar 2010:")
print(df_filtered.head())
print("\nZusammengeführte Kundendaten:")
print(df_merged.head())
