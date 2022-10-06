from socket import BDADDR_LOCAL
from Transporte import Transporte

class TransporteAquatico(Transporte):
    def __init__(self, boca, calado):
        self.__boca = boca
        self.__calado = calado

    # Getters
    @property
    def boca(self):
        return self.__boca
    
    @property
    def calado(self):
        return self.__calado
