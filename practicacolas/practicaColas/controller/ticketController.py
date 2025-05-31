from model.ticket import Ticket           # Importa la clase Ticket (estructura de los tickets)
from model.node import Node               # Importa la clase Node (nodo para la lista enlazada)

class TicketController:                        # Controlador de la cola de tickets (con prioridad)
    def _init_(self) -> None:
        self.head = None                       # Puntero al primer nodo de la cola (inicio de la lista)

    def is_empty(self) -> bool:
        return self.head == None               # Devuelve True si la cola está vacía

    def enqueue(self, ticket: Ticket) -> None:
        node = Node(ticket, ticket.priority)   # Crea un nodo nuevo con el ticket y su prioridad
        if self.is_empty():                
            self.head = node                   
        else:
            current = self.head                # Empieza desde la cabeza
            if current.priority < node.priority:   # Si el nuevo nodo tiene mayor prioridad que la cabeza
                node.next = current            # El nuevo nodo apunta al actual primero
                self.head = node               # El nuevo nodo se convierte en la cabeza
            else:
                while current.next != None and current.next.priority > node.priority:
                    current = current.next     # Avanza hasta encontrar el lugar correcto según prioridad
                node.next = current.next       # Inserta el nuevo nodo en la posición encontrada
                current.next = node

    def dequeue(self) -> Ticket:
        if self.is_empty():                    
            return None                        
        else:
            ticket = self.head.data            # Guarda el ticket de la cabeza
            self.head = self.head.next         # Mueve la cabeza al siguiente nodo
            return ticket                      # Devuelve el ticket que estaba en la cabeza

    def peek(self) -> Ticket:
        if self.is_empty():                    
            return None                        
        else:
            return self.head.data              # Devuelve el ticket de la cabeza sin sacarlo

    def print_queue(self) -> None:
        current = self.head                    
        while current != None:                 # Mientras haya nodos
            print(f"Turno: {current.data.turno}, Prioridad: {current.priority}") # Muestra turno y prioridad
            current = current.next             
        print("Fin de la cola")                
        
    def get_all(self) -> list[Ticket]:
        current = self.head               
        tickets = []                       # Lista para guardar los tickets
        while current:                     # Mientras haya nodos
            tickets.append(current.data)   # Agrega el ticket a la lista 
            current = current.next         # Avanza al siguiente nodo
        return tickets                    
