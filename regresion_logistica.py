from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
print("Exactitud en entrenamiento:", model.score(X_train, y_train))
