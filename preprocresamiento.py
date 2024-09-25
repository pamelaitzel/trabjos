import numpy as np

# Llenar los valores nulos con la media de cada columna
df.fillna(df.mean(), inplace=True)

# Convertir valores categóricos a numéricos
df['columna_categorica'] = pd.factorize(df['columna_categorica'])[0]
print(df.head())
