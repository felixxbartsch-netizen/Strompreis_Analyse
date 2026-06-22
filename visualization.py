import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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


print(df[["DE/LU preis", "Ds. DE/LU"]].corr())
# Aufgrund der Korrelation wird der Durchschnittspreis nicht geplottet

# Plots vorbereiten
df_week = df.resample("W").mean()
pl1 = df_week["DE/LU preis"]
#pl2 = df_week["Ds. DE/LU"]

# Optik des Preis_Verlauf plots anpassen
plt.title("Strompreisentwicklung", 
          color="Black")

plt.xlabel("Datum", 
          color="Black")

plt.ylabel("Preis", 
          color="Black")


plt.plot(pl1.index ,pl1.values, color="Blue")
# plt.plot( pl2.index,pl2.values, color="Orange")

# Preis_Verlauf plot anzeigen & speichern
plt.tight_layout()
plt.savefig("Preis_Verlauf.png", dpi=200)
plt.show()

# Preisvergleich der einzehlnen Jahre 
# mit Hilfe eines Barchart
df_year = df.resample("YE").mean()

plY = df_year["DE/LU preis"]

plt.bar(plY.index.year, plY.values, color="blue")

plt.savefig("D.Preis_Jahr.png", dpi=200)
plt.show()


# Die Preisverläufe der einzehlnen Jahre im direkten Vergleich
fig, axes = plt.subplots(
    3,
    2,
    figsize=(12,10),
    sharex=True,
    sharey=True
)

axes = axes.flatten()
jahre = [2021, 2022, 2023, 2024, 2025]

for ax, jahr in zip(axes, jahre):

    daten = df_week[df_week.index.year == jahr]

    ax.plot(range(len(daten)), daten["DE/LU preis"])
    ax.set_title(str(jahr))

plt.tight_layout()
plt.savefig("Jahresverlauf.png", dpi=200)
plt.show()

