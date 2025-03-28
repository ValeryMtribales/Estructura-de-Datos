from pydantic import BaseModel
from typing import Optional 

class Ticket(BaseModel):
    name: str # name of the person
    type: str # type of consultation
    identity: str # identity card
    case_description: str # description of the case
    age: int # age of the person
    priority_attention: bool # priority attention? True or False
    priority: Optional[int] =  None #priority calculated by the system