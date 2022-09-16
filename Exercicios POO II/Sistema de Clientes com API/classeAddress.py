from classeUserDataError import UserDataError

class Address:
    def __init__(self, url, data):
        if "street" not in data.keys(): raise UserDataError("street", url)
        if "suite" not in data.keys(): raise UserDataError("suite", url)
        if "city" not in data.keys(): raise UserDataError("city", url)
        if "zipcode" not in data.keys(): raise UserDataError("zipcode", url)
        if "geo" not in data.keys(): raise UserDataError("geo", url)

        self.__street = data["street"]
        self.__suite = data["suite"]
        self.__city = data["city"]
        self.__zipcode = data["zipcode"]

        if "lat" not in data["geo"].keys() or "lng" not in data["geo"].keys(): raise UserDataError("lat/lng", url)
        self.__geo = (data["geo"]["lat"], data["geo"]["lng"])
    
    # Getters
    @property
    def street(self):
        return self.__street
    
    @property
    def suite(self):
        return self.__suite
    
    @property
    def city(self):
        return self.__city
    
    @property
    def zipcode(self):
        return self.__zipcode
    
    @property
    def geo(self):
        return self.__geo
    
    # Setters
    @street.setter
    def street(self, street):
        self.__street = street
    
    @suite.setter
    def suite(self, suite):
        self.__suite = suite
    
    @city.setter
    def city(self, city):
        self.__city = city
    
    @zipcode.setter
    def zipcode(self, zipcode):
        self.__zipcode = zipcode
    
    @geo.setter
    def geo(self, geo):
        self.__geo = geo
    
    # Methods
    def __str__(self):
        return "Address: {} - {} - {} - {} - {}".format(self.street, self.suite, self.city, self.zipcode, self.geo)