from abc import abstractmethod
from animal import Animal

class Mamifero(Animal):
    def __init__(self, volume_som, tamanho_passo):
        super().__init__(tamanho_passo)
        self.__volume_som = volume_som

    @abstractmethod
    def produzir_som(self):
        return super().produzir_som()

    @abstractmethod
    def mover(self):
        return super().mover()

    # Setters e Getters
    @property
    def volume_som(self):
        return self.__volume_som
    @volume_som.setter
    def volume_som(self, volume_som):
        self.__volume_som = volume_som
