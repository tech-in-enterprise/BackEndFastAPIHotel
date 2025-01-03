from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.config.database import get_db
from fastapi import Depends, HTTPException, status
from utils.providers import token_provider
from jose import JWTError
from dependencies.users import UserDependencies

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def get_user_logged_in(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    try:
        user_data = token_provider.verify_access_token(token)  # Decodificar o token JWT
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido"
        )
    
    user_email = user_data.get("sub")
    if not user_email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="E-mail não encontrado no token"
        )
    
    user = UserDependencies(session).read_email(user_email)  # Obter usuário pelo email
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado"
        )
    
    return user  # Retornar o objeto do usuário para uso nas dependências das rotas

def validate_user_role(user, allowed_roles):
    if not user.role or user.role.access_level not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado para este nível de usuário"
        )
