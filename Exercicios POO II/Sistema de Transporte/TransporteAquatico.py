from socket import BDADDR_LOCAL
from Transporte import Transporte

class TransporteAquatico(Transporte):
    def __init__(self, boca, calado):
        self.__boca = boca
        self.__calado = calado