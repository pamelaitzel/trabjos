data, meta = arff.loadarff('ruta/del/archivo.arff')
df = pd.DataFrame(data)
print(df.describe())
