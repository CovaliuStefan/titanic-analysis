import pandas as pd

# citim datele din train.csv
df = pd.read_csv('train.csv')

# determinam numarul de coloane
numarColoane = len(df.columns)

# determinam tipurile de date pentru fiecare coloana
tipuriDeDate = df.dtypes

# determinam numarul de valori lipsa pentru fiecare coloana
valoriLipsa = df.isnull().sum()

# determinam numarul de linii
nrLinii = len(df)

# verific daca exista linii duplicate
duplicate = df.duplicated().sum()

print(f'Numarul de coloane: {numarColoane}')
print(f'Tipurile de date pentru fiecare colaona:\n{tipuriDeDate}')
print(f'Numarul de valori lipsa pentru fiecare coloana:\n{valoriLipsa}')
print(f'Numarul de linii: {nrLinii}')
print(f'Numarul de linii duplicate: {duplicate}')
