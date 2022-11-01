import re
from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andar_atual=0, total_andares_predio=10, capacidade=8, pessoas_no_elevador=0):
        super().__init__()
        self._andar_atual = andar_atual
        self._total_andares_predio = total_andares_predio
        self._capacidade = capacidade
        self._pessoas_no_elevador = pessoas_no_elevador

    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if self._andar_atual == 0:
            raise ElevadorJahNoTerreoException()
        else:
            self._andar_atual -= 1

    # ElevadorCheioException
    def entraPessoa(self) -> str:
        if self._pessoas_no_elevador == self._capacidade:
            raise ElevadorCheioException()
        else:
            self._pessoas_no_elevador += 1

    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
        if self._pessoas_no_elevador == 0:
            raise ElevadorJahVazioException()
        else:
            self._pessoas_no_elevador -= 1

    # ElevadorJahNoUltimoAndarException
    """ CONFERIR??? """
    def subir(self) -> str:
        if self._andar_atual == self._total_andares_predio - 1:
            raise ElevadorJahNoUltimoAndarException()
        else:
            self._andar_atual += 1

    @property
    def capacidade(self) -> int:
        return self._capacidade

    @property
    def totalPessoas(self) -> int:
        return self._pessoas_no_elevador

    @property
    def totalAndaresPredio(self) -> int:
        return self._total_andares_predio

    @property
    def andarAtual(self) -> int:
        return self._andar_atual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        if not totalAndaresPredio < self.andarAtual:
            self._total_andares_predio = totalAndaresPredio
