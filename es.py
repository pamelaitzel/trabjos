import pandas as pd
from scipy.io import arff

# Cargar archivo .arff
data, meta = arff.loadarff('ruta/del/archivo.arff')
df = pd.DataFrame(data)

# Mostrar información básica del DataFrame
print(df.info())
print(df.head())
