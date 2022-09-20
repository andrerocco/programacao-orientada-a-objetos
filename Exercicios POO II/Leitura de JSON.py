import json
import requests #biblioteca para fazer requisições HTTP

class UserDataError(Exception):
    def __init__(self, url, message):
        self.url = url
        self.message = message

    def __str__(self):
        return 'Error: %s at resource from: %s' % (self.message, self.url)


class ArithmeticError(Exception):
    def __init__(self, url, message):
        self.url = url
        self.message = message
    
    def __str__(self):
        return 'Error: {} at resource from: {}'.format(self.message, self.url)


def parseUsersData(data, url):
    logins = []
    for user in data:
        if "login" not in user.keys():
            raise UserDataError(url, "User login was not received")
        logins.append(user["login"])
    return logins


def computeWinRate(user: dict, url):
    if "victories" not in user.keys() or "plays" not in user.keys():
        raise UserDataError(url, "User victories or plays was not received")
    elif user["plays"] == 0:
        raise ArithmeticError(url, "Division by zero (can't divide victories by plays)")
    else:
        return user["victories"] / user["plays"]

#retorna um JSON com os dados dos usuários
url = "https://raw.githubusercontent.com/grellert/jsonbin/master/players.json"

try:
    res = requests.get(url)
    usersData = json.loads(res.content)
    computeWinRate(usersData[3], url)
except (UserDataError, ArithmeticError, AttributeError, IndexError) as e:
    print(e)