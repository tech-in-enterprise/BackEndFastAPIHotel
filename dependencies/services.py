from sqlalchemy.orm import Session
from db.models import models
from db.schemas import schema



class Services():
    

    def __init__(self, db: Session):
        self.db = db 

    #Post Services
    def create_service(self, serviceFromShema: schema.ServiceSchema):
        db_services = models.Service(
            name = serviceFromShema.name,
            price = serviceFromShema.price,
            department_id = serviceFromShema.department_id
        )
    
        self.db.add(db_services)
        self.db.commit()
        self.db.refresh(db_services)
        return db_services
    