import json
import requests
from classeUsuario import Usuario
from classeUserDataError import UserDataError

lista_usuarios = []
url = 'https://jsonplaceholder.typicode.com/users'

# Bloco de tentativa de requisição da url
try:
    res = requests.get(url)
    json_data = json.loads(res.content)
except json.decoder.JSONDecodeError:
    print('Response was not a JSON string, but', url.text)


for user in json_data:
    try:
        temp_user = Usuario(url, user)
        lista_usuarios.append(temp_user)
    except UserDataError as e:
        print(e)