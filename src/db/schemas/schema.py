from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime



class RoleSchema(BaseModel):
    access_level: str
    description_of_access_level: Optional[str] = None


class UserSchema(BaseModel):
    id: int | None = None
    name: str
    email: str
    password: str


class HotelSchema(BaseModel):
    id: int
    hotel_name: str
    registered_name: str
    phone_number: str
    hotel_email: str
    cnpj: str

    # Endereço
    street_address: str
    number_address: str
    city: str
    state: str
    cep: str

    class Config:
        orm_mode = True

class HotelAdditionalDataSchema(BaseModel):
    social_media: Optional[str]
    wifi_network: Optional[str]
    wifi_password: Optional[str]
    amenity: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]

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