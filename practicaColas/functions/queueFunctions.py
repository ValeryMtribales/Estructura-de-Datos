from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    print("Añadiendo ticket a la cola")

    # Verificar si el tipo de ticket es válido
    if ticket.tipo not in ticket_types:
        print("Tipo de ticket no válido.")
        return
    
    # Asignar prioridad automáticamente a mayores de 60 años
    if ticket.edad > 60:
        ticket.prioridad = True
    
    # Agregar el ticket a la cola correspondiente
    ticket_types[ticket.tipo].enqueue(ticket)
    print(f"Ticket para {ticket.tipo} añadido correctamente con {'prioridad' if ticket.prioridad else 'atención regular'}.")
    