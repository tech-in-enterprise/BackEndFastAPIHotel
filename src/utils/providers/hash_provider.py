from passlib.context import CryptContext



pwd_context = CryptContext(schemes=['bcrypt'])

def create_hash(text):               #uma função que toda vez que for preciso criar hash de algo, pode ser usada. Recebe o texto como parâmetro e transforam em hash
    return pwd_context.hash(text) 

def verify_hash(text, hash):
    return pwd_context.verify(text, hash) 