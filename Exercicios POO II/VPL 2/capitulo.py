class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo

    #Getters
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titulo(self):
        return self.__titulo
    
    #Setters
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo