from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Separar datos en características y etiquetas
X = df.drop(columns=['etiqueta'])
y = df['etiqueta']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar un modelo de clasificación
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Realizar predicciones y calcular la precisión
y_pred = clf.predict(X_test)
print("Precisión:", accuracy_score(y_test, y_pred))
