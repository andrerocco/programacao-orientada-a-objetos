class UserDataError(Exception):
    def __init__(self, missing, url):
        self.__missing = missing
        self.__url = url

    def __str__(self):
        return "Error: Missing value '{}' at user from: {}".format(self.missing, self.url)