from Transporte import Transporte

class TransporteAereo(Transporte):
    def __init__(self, autonomia, envergadura):
        self.__autonomia = autonomia
        self.__envergadura = envergadura