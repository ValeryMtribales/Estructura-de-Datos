# Importamos scikit-learn para el sistema de recomendaciones
from sklearn.tree import DecisionTreeClassifier

# =================== CLASE TAREA ===================
class Tarea:
    """Representa una tarea individual con sus propiedades básicas"""
    def __init__(self, titulo, categoria, duracion, prioridad):
        self.titulo = titulo
        self.categoria = categoria
        self.duracion = duracion
        self.prioridad = prioridad

# ===================  ===================
class Nodo:
    """Nodo individual para lista o pila"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaTareas:
    """Lista enlazada para almacenar tareas"""
    def __init__(self):
        self.cabeza = None

    def push(self, tarea):
        """Agrega tarea al inicio (push)"""
        nuevo = Nodo(tarea)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def pop(self):
        """Elimina y retorna la primera tarea (pop)"""
        if self.cabeza:
            tarea = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return tarea
        return None

    def obtener_tareas(self):
        """Retorna las tareas en orden de inserción"""
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append(actual.dato)
            actual = actual.siguiente
        return tareas[::-1]

    def mostrar(self, nodo=None):
        """Muestra tareas recursivamente"""
        if nodo is None:
            nodo = self.cabeza
        if nodo:
            t = nodo.dato
            print(f"- {t.titulo} | {t.categoria} | {t.duracion}h | Prioridad: {t.prioridad}")
            self.mostrar(nodo.siguiente)

    def buscar(self, titulo):
        """Busca una tarea por su título"""
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato.titulo == titulo:
                return anterior, actual
            anterior = actual
            actual = actual.siguiente
        return None, None

    def eliminar(self, titulo):
        """Elimina una tarea por título"""
        anterior, actual = self.buscar(titulo)
        if actual:
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            return actual.dato
        return None

# =================== PILA PARA DESHACER ===================
class PilaDeshacer:
    """Pila para manejar acciones a deshacer"""
    def __init__(self):
        self.cima = None

    def push(self, accion):
        """Guarda una acción en la pila (push)"""
        nuevo = Nodo(accion)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        """Quita y retorna la última acción (pop)"""
        if self.cima:
            accion = self.cima.dato
            self.cima = self.cima.siguiente
            return accion
        return None

# =================== COLA PARA PLANIFICADOR ===================
class Planificador:
    """Cola para agendar tareas"""
    def __init__(self):
        self.frente = None
        self.final = None

    def enqueue(self, tarea):
        """Agrega tarea al final (enqueue)"""
        nuevo = Nodo(tarea)
        if not self.frente:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def dequeue(self):
        """Quita y retorna la primera tarea (dequeue)"""
        if self.frente:
            tarea = self.frente.dato
            self.frente = self.frente.siguiente
            if not self.frente:
                self.final = None
            return tarea
        return None

# =================== TABLERO TRELLO ===================
class Tablero:
    """Tablero Trello con columnas To Do, Doing, Done"""
    def __init__(self):
        self.listas = {
            "To Do": ListaTareas(),
            "Doing": ListaTareas(),
            "Done": ListaTareas()
        }

    def mover_tarea(self, desde, hacia, titulo):
        """Mueve una tarea entre columnas"""
        tarea = self.listas[desde].eliminar(titulo)
        if tarea:
            self.listas[hacia].push(tarea)
            return True
        return False

    def mostrar(self):
        """Muestra el estado del tablero"""
        headers = [f"{nombre:^30}" for nombre in self.listas]
        print(" | ".join(headers))
        print("-" * (34 * len(self.listas)))
        columnas = [l.obtener_tareas() for l in self.listas.values()]
        max_len = max(len(col) for col in columnas)
        for i in range(max_len):
            fila = []
            for col in columnas:
                if i < len(col):
                    t = col[i]
                    fila.append(f"{t.titulo} ({t.prioridad})".ljust(30))
                else:
                    fila.append(" ".ljust(30))
            print(" | ".join(fila))

# =================== RECOMENDADOR (ML) ===================
class Recomendador:
    """Sistema de ML para recomendar prioridad"""
    def __init__(self):
        self.modelo = DecisionTreeClassifier(max_depth=2)  # Árbol simple
        self.entrenado = False
        self.categorias = {"trabajo": 0, "personal": 1, "otro": 2}
        self.prioridades = {0: "baja", 1: "media", 2: "alta"}

    def entrenar(self):
        """Entrena con datos ejemplo"""
        X = [[0, 5], [0, 3], [1, 2], [1, 1], [2, 4]]
        y = [2, 1, 1, 0, 1]
        self.modelo.fit(X, y)
        self.entrenado = True

    def predecir_prioridad(self, categoria, duracion):
        """Predice prioridad para nueva tarea"""
        if not self.entrenado:
            return "media"
        x = [self.categorias.get(categoria, 2), duracion]
        resultado = self.modelo.predict([x])[0]
        return self.prioridades.get(resultado, "media")

# =================== EJEMPLO DE USO ===================
if __name__ == "__main__":
    tablero = Tablero()
    pila = PilaDeshacer()
    plan = Planificador()
    recomendador = Recomendador()
    recomendador.entrenar()

    # Crear tareas con prioridad predicha
    t1 = Tarea("Informe final", "trabajo", 5, recomendador.predecir_prioridad("trabajo", 5))
    t2 = Tarea("Pagar servicios", "personal", 1, recomendador.predecir_prioridad("personal", 1))
    t3 = Tarea("Organizar archivos", "trabajo", 3, recomendador.predecir_prioridad("trabajo", 3))

    tablero.listas["To Do"].push(t1)
    tablero.listas["To Do"].push(t2)
    tablero.listas["To Do"].push(t3)

    tablero.mostrar()

    if tablero.mover_tarea("To Do", "Doing", "Informe final"):
        pila.push(("Doing", "To Do", t1))

    print("\nTarea movida con éxito al tablero 'Doing':")
    tablero.mostrar()

    plan.enqueue(t1)
    plan.enqueue(t2)
    siguiente = plan.dequeue()
    if siguiente:
        print("\nTarea siguiente programada:", siguiente.titulo)

    accion = pila.pop()
    if accion:
        origen, destino, tarea = accion
        tablero.listas[origen].eliminar(tarea.titulo)
        tablero.listas[destino].push(tarea)
        print("\nDeshacer última acción:")
        tablero.mostrar()