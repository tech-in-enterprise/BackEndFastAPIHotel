from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.models import models
from db.schemas import schema

router = APIRouter()

#serve para criar níveis de acesso dentro do banco de dados 'Administrador', 'Acesso completo ao sistema'
#por exemplo: 1 - corresponde a admin, 2 - corresponde a manager e 3 - corresponde a funcionário


@router.get("/roles")
def read_all_roles(db: Session = Depends(get_db)):
    roles = db.query(models.Role).all()
    return roles

@router.post("/roles/")
async def create_role(role: schema.RoleSchema, db: Session = Depends(get_db)):
    # Verificando se já existe uma role com o mesmo access_level
    db_role = db.query(models.Role).filter(models.Role.access_level == role.access_level).first()
    if db_role:
        raise HTTPException(status_code=400, detail="Access level already exists")

    # Criando e adicionando a nova role no banco de dados
    db_role = models.Role(
        access_level=role.access_level, 
        description_of_access_level=role.description_of_access_level
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    
    return db_role