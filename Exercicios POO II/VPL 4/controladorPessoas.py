from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes
    
    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        for cliente in self.__clientes:
            if cliente.codigo == codigo:
                return "Cliente já cadastrado"

        cliente = Cliente(nome, codigo)
        self.__clientes.append(cliente)

        return cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        for tecnico in self.__tecnicos:
            if tecnico.codigo == codigo:
                return "Técnico já cadastrado"
        
        tecnico = Tecnico(nome, codigo)
        self.__tecnicos.append(tecnico)

        return tecnico
