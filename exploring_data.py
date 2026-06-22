import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import analyse_1 as al1

df  = pd.read_csv("Gro_handelspreise_Stunde.csv", sep=";")

# Erster Einblick in die Daten
# print(df.head(8))
# print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
# print(f"Duplicates: {df.duplicated().sum()}, missing Values: {df.isna().any(axis=1).sum()}")

# Welche Spalten habe ich?
# for i, col in enumerate(df.columns, start=1):
 #   print(f"{i}: {col}")

# Relevante Spalten behalten
df = df[["Datum von", "Datum bis", "Deutschland/Luxemburg [€/MWh] Berechnete Auflösungen",
        "∅ Anrainer DE/LU [€/MWh] Berechnete Auflösungen", "DE/AT/LU [€/MWh] Berechnete Auflösungen" ]]

df = df.rename(columns={"Deutschland/Luxemburg [€/MWh] Berechnete Auflösungen": "DE/LU preis",
                   "∅ Anrainer DE/LU [€/MWh] Berechnete Auflösungen": "Ds. DE/LU",
                   "DE/AT/LU [€/MWh] Berechnete Auflösungen": "DE/AT/LU preis"})


# print(df.head(8))
# print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
# print(f"Duplicates: {df.duplicated().sum()}, missing Values: {df.isna().any(axis=1).sum()}")

# Relevanz der Spalte prüfen
# print(df["DE/AT/LU preis"].unique())

df = df.drop(columns="DE/AT/LU preis")

# Datum bearbeiten
df["Datum von"] = pd.to_datetime(df["Datum von"], format="%d.%m.%Y %H:%M")
df["Datum bis"] = pd.to_datetime(df["Datum bis"], format="%d.%m.%Y %H:%M")
df = df.sort_values("Datum von")
df = df.set_index("Datum von")

df.to_csv("Clean_Data.csv")