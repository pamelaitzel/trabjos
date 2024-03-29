lass Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    else:
        if valor < raiz.valor:
            raiz.izquierda = insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = insertar(raiz.derecha, valor)
    return raiz

def imprimir_arbol(raiz, nivel=0, prefijo="Raíz: "):
    if raiz is not None:
        print(" " * (nivel * 4) + prefijo + str(raiz.valor))
        if raiz.izquierda is not None or raiz.derecha is not None:
            imprimir_arbol(raiz.izquierda, nivel + 1, "Izq: ")
            imprimir_arbol(raiz.derecha, nivel + 1, "Der: ")

# Crear el árbol
numeros = [58, 22, 66, 7, 10, 35, 44, 71, -8, 29, 77, 9, -3, 29, 61, 0, 10, 33, 80, 59, -1, 12, 72, 20, 5, 48, 34, 74, 19, 22]
raiz = None
for numero in numeros:
    raiz = insertar(raiz, numero)

# Imprimir el árbol
imprimir_arbol(raiz)
