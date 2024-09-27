X = df.drop(columns=['etiqueta'])
y = df['etiqueta']
print("Características:\n", X.head())
print("Etiquetas:\n", y.head())
