from classeUserDataError import UserDataError

class Company:
    def __init__(self, url, data):
        if "name" not in data.keys(): raise UserDataError("name", url)
        if "catchPhrase" not in data.keys(): raise UserDataError("catchPhrase", url)
        if "bs" not in data.keys(): raise UserDataError("bs", url)

        self.__name = data["name"]
        self.__catchPhrase = data["catchPhrase"]
        self.__bs = data["bs"]
    
    # Getters
    @property
    def name(self):
        return self.__name
    
    @property
    def catchPhrase(self):
        return self.__catchPhrase
    
    @property
    def bs(self):
        return self.__bs
    
    # Setters
    @name.setter
    def name(self, name):
        self.__name = name
    
    @catchPhrase.setter
    def catchPhrase(self, catchPhrase):
        self.__catchPhrase = catchPhrase
    
    @bs.setter
    def bs(self, bs):
        self.__bs = bs
    
    # Methods
    def __str__(self):
        return "Company: {} - {} - {}".format(self.name, self.catchPhrase, self.bs)