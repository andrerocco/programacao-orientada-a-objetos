from Transporte import Transporte

class TransporteAereo(Transporte):
    def __init__(self, autonomia, envergadura):
        self.__autonomia = autonomia
        self.__envergadura = envergadura
    
    # Getters
    @property
    def autonomia(self):
        return self.__autonomia
    
    @property
    def envergadura(self):
        return self.__envergadura
