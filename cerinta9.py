import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# citim datele din train.csv
df = pd.read_csv('train.csv')

# extrag titlurile din coloana Name
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

# verific daca corespund titlurile cu sexul persoanei
def verifica_titlul(row):
    male_titles = ['Mr', 'Master', 'Don', 'Rev', 'Dr', 'Major', 'Sir', 'Col', 'Capt', 'Jonkheer']
    female_titles = ['Mrs', 'Miss', 'Ms', 'Mme', 'Mlle', 'Lady', 'Dona', 'Countess']
    
    if row['Title'] in male_titles and row['Sex'] != 'male':
        return False
    elif row['Title'] in female_titles and row['Sex'] != 'female':
        return False
    else:
        return True

df['Title_Sex_Match'] = df.apply(verifica_titlul, axis=1)

plt.figure(figsize=(10, 6))
sns.countplot(y='Title', data=df, order=df['Title'].value_counts().index)
plt.title('Distribuția Titlurilor')
plt.xlabel('Număr de Persoane')
plt.ylabel('Titlu')
plt.show()

# verific cate titluri nu corespund cu sexul
incorrect_titles = df[df['Title_Sex_Match'] == False]
print("Titluri care nu corespund cu sexul persoanei:")
print(incorrect_titles[['Name', 'Sex', 'Title']])

# afiseaz procentul de barbati si femei pentru a verifica corectitudinea
barbati = df[df['Sex'] == 'male']
print("Procentajul de barbati:", len(barbati) / len(df) * 100, "%")

