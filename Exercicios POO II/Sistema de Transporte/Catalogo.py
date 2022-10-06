from TransporteAereo import TransporteAereo
from TransporteAquatico import TransporteAquatico
from TransporteTerrestre import TransporteTerrestre

class Catalogo:
    def __init__(self):
        self.__veiculos_cadastrados = []
    
    def inserir_transporte(self, veiculo):
        if not isinstance(veiculo, (TransporteAereo, TransporteAquatico, TransporteTerrestre)):
            return "Tipo de veículo não aceito"
        else:
            self.__veiculos_cadastrados.append(veiculo)
        
    def mostrar_catalogo(self):
        for veiculo in self.__veiculos_cadastrados:
            print(veiculo)

    
    