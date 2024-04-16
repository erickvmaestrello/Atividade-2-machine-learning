#Utilizando pandas, como realizar a leitura de um arquivo CSV em um
#DataFrame e exibir as primeiras linhas?

import pandas as pd
df = pd.read_csv('nome_do_arquivo.csv')
print(df.head())