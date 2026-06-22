import pandas as pd
import numpy as np


def lade_csv(dateiname):
	df = pd.read_csv(dateiname)
	return df

def start(df):
	print(df.columns)
	print(df.head())
	print(df.tail())
	print(df.info())

def datum(df):
	df["Datum"] = pd.to_datetime(df["Datum"])
	df = df.sort_values("Datum")
	df = df.set_index("Datum")

	return df

def bereinige(df):
	alt = len(df)
	df = df.fillna(0)
	df = df.drop_duplicates()
	neu = len(df)

	print(alt - neu, "Duplikate wurden gelöscht")

	return df

def statistik(df, spalte):
    return {
        "mittelwert": df[spalte].mean(),
        "maximum": df[spalte].max(),
        "minimum": df[spalte].min(),
        "anzahl": df[spalte].count()
    }

def mittelwert(df, spalte):
    return df[spalte].mean()

def maximum(df, spalte):
    return df[spalte].max()

def maximum_zeile(df, spalte):
    return df.loc[df[spalte].idxmax()]

def minimum(df, spalte):
    return df[spalte].min()

def minimum_zeile(df, spalte):
    return df.loc[df[spalte].idxmin()]

def filter_g(df, spalte, wert):
	return df[df[spalte] > wert]

def filter_k(df, spalte, wert):
	return df[df[spalte] < wert]

def filter_gleich(df, spalte, wert):
	return df[df[spalte] == wert]


def group(df, spalte):
	return df.groupby(spalte)

def gruppen_summe(df, gruppe, spalte):
    return df.groupby(gruppe)[spalte].sum()

def gruppen_mittelwert(df, gruppe, spalte):
    return df.groupby(gruppe)[spalte].mean()

def sort(df, spalte):
	return df.sort_values(spalte)

def sort_ab(df, spalte):
	return df.sort_values(spalte, ascending=False)

def länge(df):
    return len(df)

def top_n(df, spalte, n):
	return df.sort_values(spalte, ascending=False).head(n)

def bottom_n(df, spalte, n):
	return df.sort_values(spalte, ascending=True).head(n)

def percent_change(df, spalte):
	return df[spalte].pct_change()

def moving_averages(df, spalte):
	ma20 = df[spalte].rolling(20).mean()
	ma50 = df[spalte].rolling(50).mean()

	return ma20 > ma50

