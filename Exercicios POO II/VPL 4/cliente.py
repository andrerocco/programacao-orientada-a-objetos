from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
    
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def nome(self) -> str:
        return super().nome

    def __str__(self) -> str:
        return f"Cliente: {self.nome} - Código: {self.codigo}"