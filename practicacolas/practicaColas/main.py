from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno
@app.post("/ticketCreate")
def create_ticket(ticket: Ticket):
    """
    Crea un nuevo turno y lo agrega a la cola correspondiente.
    """
    # Asigna prioridad automáticamente si no está especificada y la edad > 60
    if ticket.age > 60 and not ticket.priority_attention:
        ticket.priority_attention = True
    
    # Agrega el turno a la cola correspondiente
    try:
        add_queue(ticket, ticketTypes)
        return {
            "message": "Ticket creado exitosamente",
            "ticket_data": ticket.dict()
        }
    except ValueError as e:
        return {"error": str(e)}

# Endpoint para obtener el siguiente turno
@app.get("/nextTicket")
def get_next_ticket(ticket_type: str):
    """
    Obtiene el siguiente turno en la cola para el tipo de atención especificado.
    """
    controller = ticketTypes.get(ticket_type.lower())
    if not controller:
        return {"error": "Tipo de turno inválido"}
    
    ticket = controller.dequeue()
    if ticket:
        return {
            "message": "Siguiente turno obtenido exitosamente",
            "ticket_data": ticket
        }
    else:
        return {"message": "No hay turnos pendientes para este tipo"}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def list_tickets(ticket_type: str):
    """
    Lista todos los turnos pendientes para el tipo de atención especificado.
    """
    controller = ticketTypes.get(ticket_type.lower())
    if not controller:
        return {"error": "Tipo de turno inválido"}
    
    tickets = controller.get_all()
    return {
        "message": f"Turnos pendientes para {ticket_type}",
        "tickets": [ticket.dict() for ticket in tickets]
    }

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
