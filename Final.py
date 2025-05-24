from sklearn.tree import DecisionTreeClassifier
from collections import deque


class Tarea:
    def __init__(self, titulo, categoria, duracion, prioridad):
        self.titulo = titulo
        self.categoria = categoria
        self.duracion = duracion
        self.prioridad = prioridad


class NodoTarea:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        nuevo = NodoTarea(tarea)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def obtener_tareas(self):
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append(actual.tarea)
            actual = actual.siguiente
        return tareas[::-1]  # Para mostrarlas en orden de inserción

    def mostrar_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo:
            t = nodo.tarea
            print(f"- {t.titulo} | {t.categoria} | {t.duracion}h | Prioridad: {t.prioridad}")
            self.mostrar_recursivo(nodo.siguiente)

    def buscar_tarea(self, titulo):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.tarea.titulo == titulo:
                return anterior, actual
            anterior = actual
            actual = actual.siguiente
        return None, None

    def eliminar_tarea(self, titulo):
        anterior, actual = self.buscar_tarea(titulo)
        if actual:
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
            return actual.tarea
        return None


class NodoPila:
    def __init__(self, accion):
        self.accion = accion
        self.siguiente = None

class PilaDeshacer:
    def __init__(self):
        self.cima = None

    def registrar(self, accion):
        nuevo = NodoPila(accion)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def deshacer(self):
        if self.cima:
            accion = self.cima.accion
            self.cima = self.cima.siguiente
            return accion
        return None


class NodoCola:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class Planificador:
    def __init__(self):
        self.frente = None
        self.final = None

    def agendar(self, tarea):
        nuevo = NodoCola(tarea)
        if not self.frente:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def siguiente(self):
        if self.frente:
            tarea = self.frente.tarea
            self.frente = self.frente.siguiente
            if not self.frente:
                self.final = None
            return tarea
        return None


class Tablero:
    def __init__(self):
        self.listas = {
            "To Do": ListaTareas(),
            "Doing": ListaTareas(),
            "Done": ListaTareas()
        }

    def mover_tarea(self, desde, hacia, titulo):
        tarea = self.listas[desde].eliminar_tarea(titulo)
        if tarea:
            self.listas[hacia].agregar_tarea(tarea)
            return True
        return False

    def mostrar_tablero(self):
        # Mostrar títulos
        headers = [f"{nombre:^30}" for nombre in self.listas.keys()]
        print(" | ".join(headers))
        print("-" * (34 * len(self.listas)))

   
        listas_tareas = [lista.obtener_tareas() for lista in self.listas.values()]
        max_len = max(len(l) for l in listas_tareas)

     
        for i in range(max_len):
            fila = []
            for tareas in listas_tareas:
                if i < len(tareas):
                    t = tareas[i]
                    fila.append(f"{t.titulo} ({t.prioridad})".ljust(30))
                else:
                    fila.append(" ".ljust(30))
            print(" | ".join(fila))


class Recomendador:
    def __init__(self):
        self.modelo = DecisionTreeClassifier()
        self.entrenado = False
        self.categorias = {"trabajo": 0, "personal": 1, "otro": 2}
        self.prioridades = {"alta": 2, "media": 1, "baja": 0}

    def entrenar(self):
        # Datos ficticios: [categoria, duracion] => prioridad
        X = [
            [0, 5], [0, 3], [1, 2], [1, 1], [2, 4]
        ]
        y = [2, 1, 1, 0, 1]  # alta, media, media, baja, media
        self.modelo.fit(X, y)
        self.entrenado = True

    def predecir_prioridad(self, categoria, duracion):
        if self.entrenado:
            x = [self.categorias.get(categoria, 2), duracion]
            prio = self.modelo.predict([x])[0]
            for k, v in self.prioridades.items():
                if v == prio:
                    return k
        return "media"

# ---------------------- USO DE EJEMPLO ----------------------
if __name__ == "__main__":
    tablero = Tablero()
    pila = PilaDeshacer()
    plan = Planificador()
    recomendador = Recomendador()
    recomendador.entrenar()

    # Crear tareas
    t1 = Tarea("Informe final", "trabajo", 5, recomendador.predecir_prioridad("trabajo", 5))
    t2 = Tarea("Pagar servicios", "personal", 1, recomendador.predecir_prioridad("personal", 1))
    t3 = Tarea("Organizar archivos", "trabajo", 3, recomendador.predecir_prioridad("trabajo", 3))

    # Agregar tareas
    tablero.listas["To Do"].agregar_tarea(t1)
    tablero.listas["To Do"].agregar_tarea(t2)
    tablero.listas["To Do"].agregar_tarea(t3)

    # Mostrar
    tablero.mostrar_tablero()

    # Mover tarea
    if tablero.mover_tarea("To Do", "Doing", "Informe final"):
        pila.registrar(("Doing", "To Do", t1))

    print("\nTarea movida con éxito al tablero 'Doing:")
    tablero.mostrar_tablero()

    # Agendar tareas
    plan.agendar(t1)
    plan.agendar(t2)
    siguiente_tarea = plan.siguiente()
    if siguiente_tarea:
        print("\nTarea siguiente programada:", siguiente_tarea.titulo)

    # Deshacer última acción
    accion = pila.deshacer()
    if accion:
        origen, destino, tarea = accion
        tablero.listas[origen].eliminar_tarea(tarea.titulo)
        tablero.listas[destino].agregar_tarea(tarea)
        print("\nDeshacer última acción:")
        tablero.mostrar_tablero()

