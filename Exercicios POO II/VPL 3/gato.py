from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self):
        super().__init__(volume_som = 2, tamanho_passo = 2)
    
    def miar(self):
        return "MAMIFERO: PRODUZ SOM: {} SOM: MIAU".format(self.volume_som)
    
    def produzir_som(self):
        self.miar()
    
    def mover(self):
        return super().mover()
