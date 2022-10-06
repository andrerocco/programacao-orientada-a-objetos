from socket import BDADDR_LOCAL
from Transporte import Transporte

class TransporteAquatico(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, boca, calado):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    def __str__(self):
        print(f"Nome: {super().nome}")
        print(f"Altura: {super().altura} - Comprimento: {super().comprimento}")
        print(f"Carga: {super().carga}")
        print(f"Velocidade: {super().velocidade}")
        print(f"Boca: {self.__boca}")
        print(f"Calado: {self.__calado}")

    # Getters
    @property
    def boca(self):
        return self.__boca
    
    @property
    def calado(self):
        return self.__calado
