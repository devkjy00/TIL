import datetime

import jwt

payload = {
    "id": "123",
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
}
token = jwt.encode(payload, "123", algorithm='HS256')
print(type(jwt.decode(token, "123", algorithms="HS256")))
