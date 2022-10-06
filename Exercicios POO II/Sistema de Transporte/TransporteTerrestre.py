from Transporte import Transporte

class TransporteTerrestre(Transporte):
    def __init__(self, motor: str, rodas: str):
        self.__motor = motor
        self.__rodas = rodas
    
    # Getters
    @property
    def motor(self):
        return self.__motor
    
    @property
    def rodas(self):
        return self.__rodas
