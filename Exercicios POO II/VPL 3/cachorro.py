from mamifero import Mamifero

class Cachorro(Mamifero):
    def __init__(self):
        super().__init__(volume_som = 3, tamanho_passo = 3)

    def latir(self):
        return "MAMIFERO: PRODUZ SOM: {} SOM: AU".format(self.volume_som)
    
    def produzir_som(self):
        self.latir()
    
    def mover(self):
        return super().mover()
