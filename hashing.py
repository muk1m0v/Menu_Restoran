from passlib.context import CryptContext

cryptContext = CryptContext(schemes=['argon2'], deprecated='auto')

def hash_password(password):
    return cryptContext.hash(password)

def verify_password(password, hashed_password):
    return cryptContext.verify(password, hashed_password)