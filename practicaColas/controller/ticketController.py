from model.ticket import Ticket
from model.node import Node

class TicketController:
    def __init__(self) -> None:
        """
        Inicializa una nueva instancia de la cola de turnos.
        """
        self.head = None
    
    def is_empty(self) -> bool:
        """
        Verifica si la cola está vacía.
        """
        return self.head is None
    
    def enqueue(self, ticket: Ticket) -> None:
        """
        Agrega un ticket a la cola en función de su prioridad.
        Los tickets con prioridad más alta se colocan antes.
        """
        node = Node(ticket, ticket.priority)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            if current.priority < node.priority:
                node.next = current
                self.head = node
            else:
                while current.next is not None and current.next.priority > node.priority:
                    current = current.next
                node.next = current.next
                current.next = node
    
    def dequeue(self) -> Ticket:
        """
        Retira y devuelve el ticket con la mayor prioridad.
        """
        if self.is_empty():
            return None
        else:
            ticket = self.head.data
            self.head = self.head.next
            return ticket
    
    def peek(self) -> Ticket:
        """
        Devuelve el ticket en la cabeza de la cola sin retirarlo.
        """
        if self.is_empty():
            return None
        return self.head.data
    
    def print_queue(self) -> None:
        """
        Imprime los turnos en la cola con sus prioridades.
        """
        current = self.head
        while current is not None:
            print(f"Turno: {current.data.turno}, Prioridad: {current.priority}")
            current = current.next
        print("Fin de la cola")


