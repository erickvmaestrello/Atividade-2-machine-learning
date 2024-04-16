#Utilizando pandas, como selecionar uma coluna específica e filtrar linhas
#em um “DataFrame” com base em uma condição?

import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data)
coluna_A = df['A']
df_filtrado = df[df['B'] < 3]

print(coluna_A)
print(df_filtrado)

