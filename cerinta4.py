import pandas as pd

# citim datele din train.csv
df = pd.read_csv('train.csv')

# coloanele cu valori lipsa
valori_lipse = df.isnull().sum()
coloane_valori_lipse = valori_lipse[valori_lipse > 0]

# numarul si proportia valorilor lipsa
numar_valori_lipse = coloane_valori_lipse
proportie_valori_lipse = (coloane_valori_lipse / len(df)) * 100

# procentu valorilor lipsa pentru supravietuitori
procent_lipsa_per_clasa = df.groupby('Survived').apply(lambda x: x.isnull().mean()) * 100
# elimina coloanele care au valoarea zero
procent_lipsa_per_clasa = procent_lipsa_per_clasa.loc[:, procent_lipsa_per_clasa.any()]

print("Coloanele cu valori lipsa și numarul acestora:")
print(numar_valori_lipse)
print("\nProportia valorilor lipsa pentru fiecare coloana:")
print(proportie_valori_lipse)
print("\nProcentul valorilor lipsa pentru supravietuitori:")
print(procent_lipsa_per_clasa)
