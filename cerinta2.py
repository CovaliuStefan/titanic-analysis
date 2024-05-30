import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# citim datele din train.csv
df = pd.read_csv('train.csv')

# procentul pasagerilor pentru fiecare tip de clasa
procent_clase = df['Pclass'].value_counts(normalize=True) * 100

# procentul persoanelor care au supravietuit si care nu au supravietuit
procent_supravietuitori = df['Survived'].value_counts(normalize=True) * 100

# procentul barbatilor si femeilor
procent_sex = df['Sex'].value_counts(normalize=True) * 100

# graficele pentru fiecare tip de date
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# graficul pentru supravietuire
sns.barplot(x=procent_supravietuitori.index, y=procent_supravietuitori.values, ax=axs[0])
axs[0].set_title('Supravietuitori')
axs[0].set_ylabel('Procent')
axs[0].set_xlabel('Supravietuitori')
axs[0].set_xticks([0, 1])
axs[0].set_xticklabels(['nu au supravietuit', 'au supravietuit'])

# graficul pentru clase
sns.barplot(x=procent_clase.index, y=procent_clase.values, ax=axs[1])
axs[1].set_title('Procentul Pasagerilor pe Clase')
axs[1].set_ylabel('Procent')
axs[1].set_xlabel('Clasă')

# graficul pentru sex
sns.barplot(x=procent_sex.index, y=procent_sex.values, ax=axs[2])
axs[2].set_title('Procentul Pasagerilor pe Sex')
axs[2].set_ylabel('Procent')
axs[2].set_xlabel('Sex')

plt.tight_layout()
plt.show()



