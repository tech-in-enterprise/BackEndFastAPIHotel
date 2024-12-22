from fastapi import APIRouter, status, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.schemas import schema
from dependencies.users import UserDependencies
from utils.providers import hash_provider



router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED)
def create_users( user: schema.UserSchema, role_id: int = Body(..., embed=True), hotel_id: int = Body(None, embed=True), session: Session = Depends(get_db)):
    # Verifica a existência do usuário pelo e-mail
    find_user = UserDependencies(session).read_email(user.email)

    if find_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='E-mail já cadastrado')

    # Criptografa a senha do usuário
    user.password = hash_provider.create_hash(user.password)

    # Cria o usuário
    user_created = UserDependencies(session).create_user(user, role_id, hotel_id)

    return user_created
