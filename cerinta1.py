import pandas as pd

# Citirea datelor din fisierul train.csv
df = pd.read_csv('train.csv')

# Determinarea numărului de coloane
numar_coloane = len(df.columns)

# Determinarea tipurilor de date pentru fiecare coloană
tipuri_date = df.dtypes

# Determinarea numărului de valori lipsă pentru fiecare coloană
valori_lipse = df.isnull().sum()

# Determinarea numărului de linii
numar_linii = len(df)

# Verificarea liniilor duplicate
linii_duplicate = df.duplicated().sum()

# Afisarea rezultatelor
print(f'Numărul de coloane: {numar_coloane}')
print(f'Tipurile de date pentru fiecare coloană:\n{tipuri_date}')
print(f'Numărul de valori lipsă pentru fiecare coloană:\n{valori_lipse}')
print(f'Numărul de linii: {numar_linii}')
print(f'Numărul de linii duplicate: {linii_duplicate}')
