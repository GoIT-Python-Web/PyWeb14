from jose import jwt, JWTError
from pprint import pprint

secret = 'Very secret string'

payload = {"sub": "example@email.com.ua", "username": "example"}

token = jwt.encode(payload, secret, algorithm='HS256')

pprint(token)

try:
    result = jwt.decode(token, secret, algorithms=['HS256', 'HS512'])
    pprint(result)
except JWTError as error:
    pprint(error)

