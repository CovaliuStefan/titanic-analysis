import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# citim datele din train.csv
df = pd.read_csv('train.csv')

# copii = persoane cu varsta < 18 ani
df['IsChild'] = df['Age'] < 18

# procentul copiilor aflati la bord
nuamrCopii = df['IsChild'].sum()
totalPersoane = len(df)
procentCopii = (nuamrCopii / totalPersoane) * 100

# rata de supravieturie pentru copii si adulți
rataSupravietuireCopii = df[df['IsChild'] & (df['Survived'] == 1)]['Survived'].count() / nuamrCopii * 100
rataSupravietuireAdulti = df[~df['IsChild'] & (df['Survived'] == 1)]['Survived'].count() / (totalPersoane - nuamrCopii) * 100

# DataFrame pentru a crea graficul
rataSupravietuire = pd.DataFrame({
    'Group': ['copii', 'adulti'],
    'Survival Rate': [rataSupravietuireCopii, rataSupravietuireAdulti]
})

plt.figure(figsize=(10, 6))
sns.barplot(x='Group', y='Survival Rate', data=rataSupravietuire, palette='viridis', legend=False, hue='Group')
plt.title('Rata de supravieturie pentru copii si adulti')
plt.xlabel('Grup')
plt.ylabel('Rata de supravieturie (%)')
plt.ylim(0, 100)
plt.show()

print(f'Procentul copiilor aflati la bord: {procentCopii:.2f}%')
print(f'Rata de supravieturie pentru adulti: {rataSupravietuireAdulti:.2f}%')
print(f'Rata de supravieturie pentru copii: {rataSupravietuireCopii:.2f}%')
