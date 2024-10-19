from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.models import models
from db.schemas.schema import ServiceSchema
from dependencies.services import Services


router = APIRouter()



# Get all services
@router.get('/servicesfromdepartments', status_code = status.HTTP_200_OK)
def get_services(db: Session = Depends(get_db)):
    services = db.query(models.Service).all()
    return services

#get a respective service by department
@router.get('/services', status_code=status.HTTP_200_OK)
def get_services_by_department(department_id: int, db: Session = Depends(get_db)):
    services = db.query(models.Service).filter(models.Service.department_id == department_id).all()
    if not services:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Serviços não encontrados")
    return services

# Post Services of Departments from hotel
@router.post('/servicesfromdepartments', status_code = status.HTTP_201_CREATED)
def add_new_service(service: ServiceSchema, db: Session = Depends(get_db)):
    service_created = Services(db).create_service(service)
    return service_created