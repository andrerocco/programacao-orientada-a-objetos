from Transporte import Transporte

class TransporteTerrestre(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, motor: str, rodas: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas
    
    def __str__(self):
        print(f"Nome: {super().nome}")
        print(f"Altura: {super().altura} - Comprimento: {super().comprimento}")
        print(f"Carga: {super().carga}")
        print(f"Velocidade: {super().velocidade}")
        print(f"Boca: {self.__motor}")
        print(f"Calado: {self.__rodas}")

    # Getters
    @property
    def motor(self):
        return self.__motor
    
    @property
    def rodas(self):
        return self.__rodas
