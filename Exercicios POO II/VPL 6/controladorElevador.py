from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        pass

    def subir(self) -> str:
        try:
            self.__elevador.subir()
            return "Elevador subiu um andar"
        except ComandoInvalidoException:
            return "O elevador ja esta no ultimo andar!"

    def descer(self) -> str:
        try:
            self.__elevador.descer()
            return "Elevador desceu um andar"
        except ComandoInvalidoException:
            return "O elevador ja esta no terreo!"

    def entraPessoa(self) -> str:
        try:
            self.__elevador.entraPessoa()
            return "Uma pessoa entrou no elevador"
        except ComandoInvalidoException:
            return "O elevador ja esta cheio!"

    def saiPessoa(self) -> str:
        try:
            self.__elevador.saiPessoa()
            return "Uma pessoa saiu do elevador"
        except ComandoInvalidoException:
            return "O elevador ja esta vazio!"

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        try:
            andarAtual = int(andarAtual)
            totalAndaresPredio = int(totalAndaresPredio)
            capacidade = int(capacidade)
            totalPessoas = int(totalPessoas)
        except ValueError:
            raise ComandoInvalidoException()
        else:
            if andarAtual < 0 or totalAndaresPredio < 0 or capacidade < 0 or totalPessoas < 0:
                raise ComandoInvalidoException()
            elif totalPessoas > capacidade or andarAtual not in range(totalAndaresPredio):
                raise ComandoInvalidoException()
            else:
                self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)

    @property
    def elevador(self) -> Elevador:
        return self.__elevador
