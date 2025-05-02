class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def __str__(self):
        return str(self.valor)

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)

    def buscar(self, valor):
        if self.raiz is None:
            return False
        else:
            return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor and nodo.izq is not None:
            return self._buscar(valor, nodo.izq)
        elif valor > nodo.valor and nodo.der is not None:
            return self._buscar(valor, nodo.der)
        return False

    def preorden(self):
        if self.raiz is not None:
            self._preorden(self.raiz)

    def _preorden(self, nodo):
        print(nodo.valor)
        if nodo.izq is not None:
            self._preorden(nodo.izq)
        if nodo.der is not None:
            self._preorden(nodo.der)


    def imprimir(self):
        """Se crea el metodo imprimir, el cual imprime el arbol"""
        if self.raiz is not None:
            self._imprimir(self.raiz, 0)

    def _imprimir(self, nodo, nivel):
        if nodo is not None:
            self._imprimir(nodo.der, nivel+1)
            print('   '*nivel, nodo.valor)
            self._imprimir(nodo.izq, nivel+1)

# Path: clase-Arboles/main.py
arbol = ArbolBinario()

valores = [20, 10, 30, 5, 15, 25, 35]
for v in valores:
    arbol.insertar(v)

# Mostrar el árbol en preorden
arbol.preorden()

# Buscar un valor
busqueda = int(input("Ingrese un valor para buscar en el árbol: "))
if arbol.buscar(busqueda):
    print(f"El valor {busqueda} SÍ se encuentra en el árbol.")
else:
    print(f"El valor {busqueda} NO se encuentra en el árbol.")