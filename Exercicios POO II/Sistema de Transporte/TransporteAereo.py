from Transporte import Transporte

class TransporteAereo(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, autonomia, envergadura):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura
    
    def __str__(self):
        print(f"Nome: {super().nome}")
        print(f"Altura: {super().altura} - Comprimento: {super().comprimento}")
        print(f"Carga: {super().carga}")
        print(f"Velocidade: {super().velocidade}")
        print(f"Boca: {self.__autonomia}")
        print(f"Calado: {self.__envergadura}")

    # Getters
    @property
    def autonomia(self):
        return self.__autonomia
    
    @property
    def envergadura(self):
        return self.__envergadura
