from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.models import models
from db.schemas import schema
from dependencies.hotel import Hotel


router = APIRouter()


#Get all data from Hotel
@router.get("/hotel_data", status_code=status.HTTP_200_OK)
def get_hotel_data(db: Session = Depends(get_db)):
    hotel = db.query(models.Hotel).all()
    return hotel

#Post Hotel
@router.post('/create-hotel', status_code=status.HTTP_201_CREATED)
def new_hotel(hotel: schema.HotelSchema, db: Session = Depends(get_db)):
    hotel_created = Hotel(db).create_hotel_in_db(hotel)
    return hotel_created

