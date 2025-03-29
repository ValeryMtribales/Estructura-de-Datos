from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue, get_next_ticket, get_queue_list

app = FastAPI()

# Diccionario que almacena los controladores de turnos por tipo de servicio
ticket_types = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno
@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    add_queue(turno, ticket_types)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

# Endpoint para obtener el siguiente turno (LIBERAR LA COLA)
@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    siguiente_turno = get_next_ticket(tipo, ticket_types)
    if siguiente_turno:
        return {"mensaje": "El siguiente turno es", "datos_turno": siguiente_turno}
    return {"mensaje": "No hay turnos en la cola", "datos_turno": None}

# Endpoint para listar los turnos en cola por tipo de servicio
@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    lista_turnos = get_queue_list(tipo, ticket_types)
    return {"mensaje": "Lista de turnos en cola", "datos_turnos": lista_turnos}

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint para obtener un ítem de ejemplo
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
