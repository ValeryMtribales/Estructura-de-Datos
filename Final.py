# Importamos scikit-learn para el sistema de recomendaciones
from sklearn.tree import DecisionTreeClassifier

# =================== CLASE TAREA ===================
class Tarea:
    """Representa una tarea individual con sus propiedades básicas"""
    def __init__(self, titulo, categoria, duracion, prioridad):
        self.titulo = titulo        # Nombre de la tarea
        self.categoria = categoria  # Tipo: trabajo, personal, etc.
        self.duracion = duracion    # Tiempo estimado en horas
        self.prioridad = prioridad  # alta, media, baja

# =================== LISTA ENLAZADA ===================
class NodoTarea:
    """Nodo individual para la lista enlazada de tareas"""
    def __init__(self, tarea):
        self.tarea = tarea          # Almacena el objeto Tarea
        self.siguiente = None       # Puntero al siguiente nodo

class ListaTareas:
    """Lista enlazada para almacenar y manejar tareas"""
    def __init__(self):
        self.cabeza = None          # Primer nodo de la lista

    def agregar_tarea(self, tarea):
        """Agrega una nueva tarea al inicio de la lista"""
        nuevo = NodoTarea(tarea)    # Crear nuevo nodo
        nuevo.siguiente = self.cabeza  # El nuevo apunta al que era primero
        self.cabeza = nuevo         # Ahora el nuevo es la cabeza

    def obtener_tareas(self):
        """Recorre la lista y retorna todas las tareas en orden de inserción"""
        tareas = []
        actual = self.cabeza        # Empezar desde la cabeza
        while actual:               # Mientras haya nodos
            tareas.append(actual.tarea)  # Agregar tarea a la lista
            actual = actual.siguiente    # Moverse al siguiente nodo
        return tareas[::-1]         # Invertir para mostrar en orden de inserción

    def mostrar_recursivo(self, nodo=None):
        """Muestra todas las tareas usando recursión"""
        if nodo is None:            # Si es la primera llamada
            nodo = self.cabeza      # Empezar desde la cabeza
        if nodo:                    # Si el nodo existe
            t = nodo.tarea          # Obtener la tarea del nodo
            print(f"- {t.titulo} | {t.categoria} | {t.duracion}h | Prioridad: {t.prioridad}")
            self.mostrar_recursivo(nodo.siguiente)  # Llamada recursiva

    def buscar_tarea(self, titulo):
        """Busca una tarea por título y retorna nodo anterior y actual"""
        actual = self.cabeza        # Empezar desde la cabeza
        anterior = None             # Inicialmente no hay anterior
        while actual:               # Recorrer la lista
            if actual.tarea.titulo == titulo:  # Si encontramos la tarea
                return anterior, actual        # Retornar ambos nodos
            anterior = actual       # El actual se vuelve anterior
            actual = actual.siguiente  # Moverse al siguiente
        return None, None           # No se encontró la tarea

    def eliminar_tarea(self, titulo):
        """Elimina una tarea de la lista y la retorna"""
        anterior, actual = self.buscar_tarea(titulo)  # Buscar la tarea
        if actual:                  # Si se encontró la tarea
            if anterior:            # Si no es el primer nodo
                anterior.siguiente = actual.siguiente  # Conectar anterior con siguiente
            else:                   # Si es el primer nodo
                self.cabeza = actual.siguiente        # La cabeza es el siguiente
            return actual.tarea     # Retornar la tarea eliminada
        return None                 # No se encontró la tarea

# =================== PILA PARA DESHACER ===================
class NodoPila:
    """Nodo para la pila de acciones a deshacer"""
    def __init__(self, accion):
        self.accion = accion        # Información de la acción realizada
        self.siguiente = None       # Puntero al siguiente nodo en la pila

class PilaDeshacer:
    """Pila (Stack) para manejar funcionalidad de deshacer"""
    def __init__(self):
        self.cima = None            # Elemento en la cima de la pila

    def registrar(self, accion):
        """Registra una acción en la pila (push)"""
        nuevo = NodoPila(accion)    # Crear nuevo nodo con la acción
        nuevo.siguiente = self.cima # El nuevo apunta a la cima anterior
        self.cima = nuevo           # El nuevo se vuelve la cima

    def deshacer(self):
        """Quita y retorna la última acción de la pila (pop)"""
        if self.cima:               # Si hay elementos en la pila
            accion = self.cima.accion      # Obtener la acción
            self.cima = self.cima.siguiente # Mover la cima al siguiente
            return accion           # Retornar la acción
        return None                 # Pila vacía

# =================== COLA PARA PLANIFICADOR ===================
class NodoCola:
    """Nodo para la cola del planificador"""
    def __init__(self, tarea):
        self.tarea = tarea          # Tarea a planificar
        self.siguiente = None       # Puntero al siguiente en la cola

class Planificador:
    """Cola (Queue) para planificar orden de ejecución de tareas"""
    def __init__(self):
        self.frente = None          # Primer elemento de la cola
        self.final = None           # Último elemento de la cola

    def agendar(self, tarea):
        """Agrega una tarea al final de la cola (enqueue)"""
        nuevo = NodoCola(tarea)     # Crear nuevo nodo
        if not self.frente:         # Si la cola está vacía
            self.frente = self.final = nuevo  # Frente y final son el mismo
        else:                       # Si ya hay elementos
            self.final.siguiente = nuevo      # Conectar al final
            self.final = nuevo      # Actualizar el final

    def siguiente(self):
        """Quita y retorna la primera tarea de la cola (dequeue)"""
        if self.frente:             # Si hay elementos
            tarea = self.frente.tarea          # Obtener la tarea
            self.frente = self.frente.siguiente # Mover frente al siguiente
            if not self.frente:     # Si la cola quedó vacía
                self.final = None   # Final también debe ser None
            return tarea            # Retornar la tarea
        return None                 # Cola vacía

# =================== TABLERO KANBAN ===================
class Tablero:
    """Sistema de tablero Kanban con tres columnas"""
    def __init__(self):
        # Crear tres listas para las columnas del tablero
        self.listas = {
            "To Do": ListaTareas(),   # Tareas por hacer
            "Doing": ListaTareas(),   # Tareas en progreso
            "Done": ListaTareas()     # Tareas completadas
        }

    def mover_tarea(self, desde, hacia, titulo):
        """Mueve una tarea de una columna a otra"""
        tarea = self.listas[desde].eliminar_tarea(titulo)  # Quitar de origen
        if tarea:                   # Si se encontró la tarea
            self.listas[hacia].agregar_tarea(tarea)        # Agregar a destino
            return True             # Operación exitosa
        return False                # Tarea no encontrada

    def mostrar_tablero(self):
        """Visualiza el tablero completo en formato columnas"""
        # Crear encabezados centrados de 30 caracteres
        headers = [f"{nombre:^30}" for nombre in self.listas.keys()]
        print(" | ".join(headers))  # Imprimir títulos
        print("-" * (34 * len(self.listas)))  # Línea separadora

        # Obtener todas las tareas de cada columna
        listas_tareas = [lista.obtener_tareas() for lista in self.listas.values()]
        max_len = max(len(l) for l in listas_tareas)  # Encontrar columna más larga

        # Imprimir fila por fila
        for i in range(max_len):
            fila = []
            for tareas in listas_tareas:  # Para cada columna
                if i < len(tareas):       # Si hay tarea en esta posición
                    t = tareas[i]
                    # Formatear: "Título (prioridad)" alineado a la izquierda
                    fila.append(f"{t.titulo} ({t.prioridad})".ljust(30))
                else:                     # Si no hay tarea
                    fila.append(" ".ljust(30))  # Espacio vacío
            print(" | ".join(fila))       # Imprimir la fila

# =================== SISTEMA DE RECOMENDACIONES ===================
class Recomendador:
    """Sistema de ML para recomendar prioridades automáticamente"""
    def __init__(self):
        self.modelo = DecisionTreeClassifier()  # Modelo de árbol de decisión
        self.entrenado = False      # Flag para saber si está entrenado
        # Mapeos de texto a números para el modelo
        self.categorias = {"trabajo": 0, "personal": 1, "otro": 2}
        self.prioridades = {"alta": 2, "media": 1, "baja": 0}

    def entrenar(self):
        """Entrena el modelo con datos de ejemplo"""
        # Datos de entrenamiento: [categoria_numerica, duracion] => prioridad
        X = [
            [0, 5], [0, 3], [1, 2], [1, 1], [2, 4]  # Características
        ]
        y = [2, 1, 1, 0, 1]         # Etiquetas: alta, media, media, baja, media
        self.modelo.fit(X, y)       # Entrenar el modelo
        self.entrenado = True       # Marcar como entrenado

    def predecir_prioridad(self, categoria, duracion):
        """Predice la prioridad de una nueva tarea"""
        if self.entrenado:          # Solo si el modelo está entrenado
            # Convertir categoría a número, usar 2 (otro) por defecto
            x = [self.categorias.get(categoria, 2), duracion]
            prio = self.modelo.predict([x])[0]  # Hacer predicción
            # Convertir número de vuelta a texto
            for k, v in self.prioridades.items():
                if v == prio:
                    return k        # Retornar prioridad como texto
        return "media"              # Valor por defecto

# =================== EJEMPLO DE USO ===================
if __name__ == "__main__":
    # Inicializar todos los componentes del sistema
    tablero = Tablero()           # Crear tablero Kanban
    pila = PilaDeshacer()         # Crear pila para deshacer
    plan = Planificador()         # Crear cola de planificación
    recomendador = Recomendador() # Crear sistema de recomendaciones
    recomendador.entrenar()       # Entrenar el modelo

    # Crear tareas con prioridades automáticas
    t1 = Tarea("Informe final", "trabajo", 5, 
               recomendador.predecir_prioridad("trabajo", 5))
    t2 = Tarea("Pagar servicios", "personal", 1, 
               recomendador.predecir_prioridad("personal", 1))
    t3 = Tarea("Organizar archivos", "trabajo", 3, 
               recomendador.predecir_prioridad("trabajo", 3))

    # Agregar todas las tareas a la columna "To Do"
    tablero.listas["To Do"].agregar_tarea(t1)
    tablero.listas["To Do"].agregar_tarea(t2)
    tablero.listas["To Do"].agregar_tarea(t3)

    # Mostrar estado inicial del tablero
    tablero.mostrar_tablero()

    # Mover una tarea y registrar la acción para poder deshacerla
    if tablero.mover_tarea("To Do", "Doing", "Informe final"):
        pila.registrar(("Doing", "To Do", t1))  # Guardar acción inversa

    print("\nTarea movida con éxito al tablero 'Doing:")
    tablero.mostrar_tablero()    # Mostrar tablero actualizado

    # Demostrar el planificador de tareas
    plan.agendar(t1)             # Agregar tareas a la cola
    plan.agendar(t2)
    siguiente_tarea = plan.siguiente()  # Obtener siguiente tarea
    if siguiente_tarea:
        print("\nTarea siguiente programada:", siguiente_tarea.titulo)

    # Demostrar funcionalidad de deshacer
    accion = pila.deshacer()     # Obtener última acción
    if accion:
        origen, destino, tarea = accion  # Desempaquetar acción
        # Realizar movimiento inverso
        tablero.listas[origen].eliminar_tarea(tarea.titulo)
        tablero.listas[destino].agregar_tarea(tarea)
        print("\nDeshacer última acción:")
        tablero.mostrar_tablero()  # Mostrar tablero después de deshacer