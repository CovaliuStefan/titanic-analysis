import pandas as pd
import matplotlib.pyplot as plt

# citim datele din train.csv
df = pd.read_csv('train.csv')

# coloanele numerice
coloane_numerice = df.select_dtypes(include=['int64', 'float64']).columns

# histogramele pentru fiecare coloana numerica
for col in coloane_numerice:
    plt.figure(figsize=(10, 6))
    df[col].hist(bins=30, edgecolor='black')
    plt.title(f'Histograma pentru {col}')
    plt.xlabel(col)
    plt.ylabel('Frecventa')
    plt.grid(False)
    plt.show()
