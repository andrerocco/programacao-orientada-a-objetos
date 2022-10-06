from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, nome, altura, comprimento, carga, velocidade):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    # Getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def comprimento(self):
        return self.__comprimento
    
    @property
    def carga(self):
        return self.__carga
    
    @property
    def velocidade(self):
        return self.__velocidade

    @abstractmethod
    def __str__(self) -> str:
        pass