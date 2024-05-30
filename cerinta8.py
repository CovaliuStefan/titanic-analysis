import pandas as pd

# citim datele din train.csv
df = pd.read_csv('train.csv')

# completez valorile lipsa pentru coloanele numerice
def fill_missing_numeric(df, column_name, groupByColumns):
    # pentru fiecare grup
    for group, group_df in df.groupby(groupByColumns):
        # calculez media valorilor non-lipsa din coloana specificata
        group_mean = group_df[column_name].mean()
        # inlocuiesc valorile lipsa din grup cu media
        df.loc[group_df.index, column_name] = group_df[column_name].fillna(group_mean)
    return df

# completez valorile lipsa pentru coloanele categoriale
def fill_missing_categorical(df, column_name, groupByColumns):
    # pentru fiecare grup
    for group, group_df in df.groupby(groupByColumns):
        # cea mai intalnita valoare din coloana
        mostCommonValue = group_df[column_name].mode().values[0]
        
        # inlocuiesc valorile lipsa din grup cu cea mai intalnita valoare
        df.loc[group_df.index, column_name] = group_df[column_name].fillna(mostCommonValue)
    return df

# grupez dupa clasa si supravietuire
groupByColumns = ['Pclass', 'Survived']

df = fill_missing_numeric(df, 'Age', groupByColumns)
df = fill_missing_numeric(df, 'Fare', groupByColumns)

df['Age'] = df['Age'].round().astype('int64')

df = fill_missing_categorical(df, 'Embarked', groupByColumns)
df = fill_missing_categorical(df, 'Cabin', groupByColumns)

# salvez fisierul
df.to_csv('train_filled.csv', index=False)
