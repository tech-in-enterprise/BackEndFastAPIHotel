from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.models import models
from db.schemas import schema
from dependencies.derpartment import Departments


router = APIRouter()




# Get all departments
@router.get("/departments", status_code=status.HTTP_200_OK)
def get_departments(db: Session = Depends(get_db)):
    departments = db.query(models.Department).all()
    return departments


# Post Department from hotel
@router.post('/departments', status_code=status.HTTP_201_CREATED)
def add_department(department: schema.DepartmentSchema, db: Session = Depends(get_db)):
    department_created = Departments(db).create_department_in_db(department)
    return department_created


# Delete Department from hotel
@router.delete('/departments/{department_id}', status_code=status.HTTP_200_OK)
def remove_department(department_id: int, db: Session = Depends(get_db)):
    Departments(db).destroy_department(department_id)
    return {'message': 'Removido com sucesso'}