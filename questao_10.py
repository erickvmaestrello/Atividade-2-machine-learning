#Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan]
})

print("DataFrame original:")
print(df)

df_filled = df.fillna(0)

print("\nDataFrame após preencher valores ausentes com 0:")
print(df_filled)
