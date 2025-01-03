from jose import jwt
from datetime import datetime, timedelta


#Config
SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
EXPIRES_IN_MINUTE = 3000


def create_access_token(data: dict):
    data = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTE)

    data.update({'exp': expiration})

    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload