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

# numarul de pasageri pentru fiecare categorie de varsta
numar_pasageri_per_categorie = df['AgeCategory'].value_counts().sort_index()

print(numar_pasageri_per_categorie)

plt.figure(figsize=(10, 6))
sns.barplot(x=numar_pasageri_per_categorie.index, y=numar_pasageri_per_categorie.values, palette='viridis', legend=False, hue=numar_pasageri_per_categorie.index)
plt.title('Numarul de pasageri pe categorii de varsta')
plt.xlabel('Categorie de varsta')
plt.ylabel('Numar de pasageri')
plt.show()
