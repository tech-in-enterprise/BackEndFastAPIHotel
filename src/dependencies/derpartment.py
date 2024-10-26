from sqlalchemy.orm import Session
from sqlalchemy import delete
from db.schemas import schema
from db.models import models



class Departments():

    def __init__(self, db: Session) -> None:
        self.db = db


    #Post Dependencies
    def create_department_in_db(self, department: schema.DepartmentSchema):
        db_department = models.Department(
            name = department.name.title() #title é um método para deixar a primeira letra de cada palavra maiúscula
        )
        self.db.add(db_department)
        self.db.commit()
        self.db.refresh(db_department)
        return db_department
    
    #Delete dependencies
    def destroy_department(self, department_id: int):
        self.db.query(models.Department).filter(models.Department.id == department_id).delete()

        self.db.commit()