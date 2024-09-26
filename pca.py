from sklearn.decomposition import PCA

# Reducción a 2 componentes principales
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualizar los componentes principales
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.title("PCA del Conjunto de Datos")
plt.colorbar(label='Etiqueta')
plt.show()
