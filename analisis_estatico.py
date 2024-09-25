import numpy as np
import matplotlib.pyplot as plt

# Calcular estadísticas
media = np.mean(df['columna_numerica'])
desviacion = np.std(df['columna_numerica'])
print(f"Media: {media}, Desviación estándar: {desviacion}")

# Histograma de una columna numérica
plt.hist(df['columna_numerica'], bins=30, color='skyblue')
plt.title("Distribución de la columna")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()
