import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# citim datele din train.csv
df = pd.read_csv('train.csv')

# categoriile de varsta
bins = [0, 20, 40, 60, df['Age'].max()]
labels = ['0-20', '21-40', '41-60', '61+']

# creez o coloana in plus pentru categoriile de varsta
df['AgeCategory'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)

# pastrez doar barbatii
barbati = df[df['Sex'] == 'male']

# numarul de barbati care au supravietuit in fiecare categorie de varsta
supravietuitori_barbati_per_categorie = barbati[barbati['Survived'] == 1]['AgeCategory'].value_counts().sort_index()

# numarul total de barbati in fiecare categorie de varsta
total_barbati_per_categorie = barbati['AgeCategory'].value_counts().sort_index()

# procentului de supravietuire pentru barbati in fiecare categorie de varsta
procent_supravietuire_barbati = (supravietuitori_barbati_per_categorie / total_barbati_per_categorie) * 100

print(procent_supravietuire_barbati)

plt.figure(figsize=(10, 6))
sns.barplot(x=procent_supravietuire_barbati.index, y=procent_supravietuire_barbati.values, palette='viridis', legend=False, hue=procent_supravietuire_barbati.index)
plt.title('Procentul de supravietuire al barbatilor pe categorii de varsta')
plt.xlabel('Categorie de varsta')
plt.ylabel('Procent de supravietuire')
plt.show()
