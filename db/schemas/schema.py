from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime



class HotelSchema(BaseModel):
    id: int
    hotel_name: str
    registered_name: str
    phone_number: str
    email_address: str
    cnpj: str

    # Endereço
    street_address: str
    number_address: str
    city: str
    state: str
    cep: str



    class Config:
        orm_mode = True

class DepartmentSchema(BaseModel):
    id: Optional[int] = None
    name: str

    class Config:
        orm_mode = True


class ServiceSchema(BaseModel):
    name: str
    price: Optional[float] = None
    department_id: int

    class Config:
        orm_mode = True