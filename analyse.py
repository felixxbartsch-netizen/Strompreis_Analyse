import pandas as pd
import numpy as np
import analyse_1 as al1
import matplotlib.pyplot as plt

df = pd.read_csv("Clean_Data.csv")

# Alles rund um das Datum richten & kleine Übersicht von den Daten
df["Datum von"] = pd.to_datetime(df["Datum von"])
df["Datum bis"] = pd.to_datetime(df["Datum bis"])
df = df.set_index("Datum von")
print(df.shape)
print(df.head())

# Datentypen anpassen
df["DE/LU preis"] = (
    df["DE/LU preis"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)

df["Ds. DE/LU"] = (
    df["Ds. DE/LU"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# Grunddaten:
st = al1.statistik(df, "DE/LU preis")
print(st)

# wann gab es negative Preise?
print(al1.filter_k(df, "DE/LU preis", 0))
print(len(al1.filter_k(df, "DE/LU preis", 0)))

# an wie vielen Tagen?
df_day = df.resample("D").mean()
print(al1.filter_k(df_day, "DE/LU preis", 0))
print(len(al1.filter_k(df_day, "DE/LU preis", 0)))

# Verlauf der 6 Tage
tage = np.array(["2021-04-05",
                "2021-05-22",
                "2022-12-31",
                "2023-07-02",
                "2023-12-24",
                "2025-10-04"])

fig, axes = plt.subplots(3, 2, figsize=(14, 8))

axes = axes.flatten()

for ax, tag in zip(axes, tage):

    daten = df.loc[tag]

    ax.plot(
        daten.index.hour,
        daten["DE/LU preis"]
    )

    ax.set_title(tag)
    ax.set_xlabel("Stunde")
    ax.set_ylabel("€/MWh")

plt.tight_layout()
plt.savefig("Negative_Tage.png", dpi=200)
plt.show()

# negativster Tag/Wert?
print(al1.minimum_zeile(df_day, "DE/LU preis"))
print(al1.minimum_zeile(df, "DE/LU preis"))

df_07_02 = df.loc["2023-07-02"]

plt.plot(df_07_02.index, df_07_02["DE/LU preis"])
plt.tight_layout()
plt.savefig("Min_Wert.png")
plt.show()

# Teuerster Tag/Wert
print(al1.maximum_zeile(df_day, "DE/LU preis"))
print(al1.maximum_zeile(df, "DE/LU preis"))

# Wert 2024-12-12 18:00:00
# Tag 2022-08-26 12:30:00

df_max_d = df.loc["2022-08-26"]
df_max_w = df.loc["2024-12-12"]

figure, axes = plt.subplots(1, 2)

axes[0].plot(df_max_d.index.hour, df_max_d["DE/LU preis"])
axes[0].set_title("Teuerster Tag")

axes[1].plot(df_max_w.index.hour, df_max_w["DE/LU preis"])
axes[1].set_title("Höchster Wert")

plt.tight_layout()
plt.savefig("Max_Werte.png", dpi=200)
plt.show()

# Moving average & Vortagespreis hinzufügen
df["ma20"] = df["DE/LU preis"].rolling(20).mean()
df["ma50"] = df["DE/LU preis"].rolling(50).mean()
df["Preis_Vortag"] = df["DE/LU preis"].shift(24)
df["Preis_Veränderung_%"] = (
    (df["DE/LU preis"] - df["DE/LU preis"].shift(24))
    / df["DE/LU preis"].shift(24)) * 100

df["Preis_Veränderung_%"] = df["Preis_Veränderung_%"].replace(
    [np.inf, -np.inf],np.nan)

print(df.corr(numeric_only=True)["DE/LU preis"])

# Größte Preisänderungen
print(al1.maximum_zeile(df, "Preis_Veränderung_%"))

print(df.loc["2023-10-30"])
print(df.loc["2023-10-29"])

# Preisvergleich nach Tageszeit
df_Hour = df.resample("h").mean()
print(al1.statistik(df_Hour, ["DE/LU preis"]),
      "Teuersten Stunden: ",
      al1.maximum_zeile(df_Hour, ["DE/LU preis"]),
      "Billigsten Stunden: ",
      al1.minimum_zeile(df_Hour, ["DE/LU preis"]))

df_Hour = df.groupby(df.index.hour)["DE/LU preis"].mean()
plt.bar(df_Hour.index, df_Hour.values)
plt.tight_layout()
plt.savefig("TPV.png", dpi=200)
plt.show()