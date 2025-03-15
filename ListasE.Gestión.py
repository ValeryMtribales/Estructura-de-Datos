from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None
    
    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        nueva_tarea.siguiente = self.cabeza
        self.cabeza = nueva_tarea
    
    def eliminar_tarea(self, descripcion):
        actual, previo = self.cabeza, None
        while actual and actual.descripcion != descripcion:
            previo, actual = actual, actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
    
    def mostrar_tareas(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.descripcion} - Prioridad: {actual.prioridad} - Vence: {actual.fecha_vencimiento.date()}")
            actual = actual.siguiente
    
    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                print(f"Encontrada: {actual.descripcion} - Prioridad {actual.prioridad} - {actual.fecha_vencimiento.date()}")
                return
            actual = actual.siguiente
        print("Tarea no encontrada.")
    
    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)
        print("Tarea completada y eliminada.")

# Ejemplo de uso
tareas = ListaTareas()
tareas.agregar_tarea("Comprar utiles de aseo", 2, "2024-03-15")
tareas.agregar_tarea("Entregar informe", 1, "2024-03-14")
tareas.mostrar_tareas()
tareas.marcar_completada("Entregar informe")
tareas.mostrar_tareas()
