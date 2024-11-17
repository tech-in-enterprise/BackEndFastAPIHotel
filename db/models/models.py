from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from db.config.database import Base
from sqlalchemy.orm import relationship


class Hotel(Base):
    __tablename__ = 'hotels'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_name = Column(String, nullable=False)
    registered_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email_address = Column(String,  nullable=False)
    cnpj = Column(String,  nullable=False)

    #address
    street_address = Column(String, nullable=False)
    number_address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    cep = Column(String, nullable=False)

    #redes sociais
    social_media = Column(String)

    #Wi-fi
    wifi_network = Column(String)
    wifi_password = Column(String)

    #Comodidades (Amenity)
    amenity = Column(String)
    start_time = Column(String)
    end_time = Column(String)


    rooms = relationship('Room', back_populates='hotel')
    departments = relationship('Department', back_populates='hotel')

class Guest(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    email_address = Column(String)
    room_id = Column(Integer, ForeignKey('rooms.id'))

    room = relationship('Room', back_populates='guests')
    requests = relationship("Request", back_populates='guest')

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(String, nullable=False)
    status = Column(String)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))

    hotel = relationship('Hotel', back_populates='rooms')
    guests = relationship('Guest', back_populates='room')

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))

    hotel = relationship('Hotel', back_populates='departments')
    requests = relationship('Request', back_populates='department')
    service = relationship("Service", back_populates="department")

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    department_id = Column(Integer, ForeignKey('departments.id')) 

    department = relationship("Department", back_populates="service") 


class Request(Base):
    __tablename__ = 'requests'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_created = Column(String)
    date_updated = Column(String)
    status = Column(String)
    guest_id = Column(Integer, ForeignKey('guests.id'))
    department_id = Column(Integer, ForeignKey('departments.id'))

    guest = relationship("Guest", back_populates="requests")
    department = relationship("Department", back_populates="requests")  

