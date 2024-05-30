import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# citim datele din train.csv
df = pd.read_csv('train.csv')

# verific daca un pasager este singur
df['IsAlone'] = (df['SibSp'] == 0) & (df['Parch'] == 0)

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='IsAlone', hue='Survived', multiple='stack', kde=False)
plt.title('Relatia dintre starea de a fi singur și supravietuire')
plt.xlabel('Este Singur')
plt.ylabel('Numarul de Pasageri')
plt.xticks([0, 1], ['Nu', 'Da'])
plt.show()

# relatia dintre tarif, clasa și supravietuire pentru primele 100 inregistrari
sns.catplot(x='Pclass', y='Fare', hue='Survived', data=df.head(100), kind='strip', jitter=True)
plt.title('Relatia dintre tarif, clasa și supravietuire (primele 100 de inregistrari)')
plt.xlabel('Clasa')
plt.ylabel('Tarif')
plt.show()
