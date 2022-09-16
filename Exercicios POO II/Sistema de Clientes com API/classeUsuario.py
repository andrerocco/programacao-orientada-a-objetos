from classeUserDataError import UserDataError
from classeAddress import Address
from classeCompany import Company

class Usuario:
    def __init__(self, url, user_info):
        if "id" not in user_info.keys(): raise UserDataError("id", url)
        if "name" not in user_info.keys(): raise UserDataError("name", url)
        if "username" not in user_info.keys(): raise UserDataError("username", url)
        if "email" not in user_info.keys(): raise UserDataError("email", url)
        if "address" not in user_info.keys(): raise UserDataError("address", url)
        if "phone" not in user_info.keys(): raise UserDataError("phone", url)
        if "website" not in user_info.keys(): raise UserDataError("website", url)
        if "company" not in user_info.keys(): raise UserDataError("company", url)

        self.__id = user_info["id"]
        self.__name = user_info["name"]
        self.__username = user_info["username"]
        self.__email = user_info["email"]
        self.__address = Address(url, user_info["address"])
        self.__phone = user_info["phone"]
        self.__website = user_info["website"]
        self.__company = Company(url, user_info["company"])
    
    # Getters
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email
    
    @property
    def address(self):
        return self.__address
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def website(self):
        return self.__website
    
    @property
    def company(self):
        return self.__company
    
    # Setters
    @id.setter
    def id(self, id):
        self.__id = id
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @username.setter
    def username(self, username):
        self.__username = username
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @address.setter
    def address(self, url, address: dict):
        self.__address = Address(url, address)
    
    @phone.setter
    def phone(self, phone):
        self.__phone = phone
    
    @website.setter
    def website(self, website):
        self.__website = website
        
    @company.setter
    def company(self, url, company: dict):
        self.__company = Company(url, company)
    
    # Methods
    def __str__(self):
        return "ID: {}\tName: {}\tUsername: {}\tEmail: {}\tAddress: {}\tPhone: {}\tWebsite: {}\tCompany: {}".format(self.id, self.name, self.username, self.email, self.address, self.phone, self.website, self.company)
