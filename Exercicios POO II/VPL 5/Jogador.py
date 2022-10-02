from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__mao = []

    # Retorna o nome do jogador
    @property
    def nome(self) -> str:
        return self.__nome

    # Retorna a mao atual do jogador (lista das cartas que ele possui)
    @property
    def mao(self) -> list:
        return self.__mao
    
    def baixa_carta_da_mao(self) -> Carta:
        carta = random.choice(self.__mao)
        self.__mao.remove(carta)
        
        return carta

    # Inclui na mao do jogador a carta passada como parametro
    def inclui_carta_na_mao(self, carta:Carta):
        self.__mao.append(carta)
