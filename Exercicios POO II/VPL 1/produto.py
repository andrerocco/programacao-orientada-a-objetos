class Produto:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__fone = telefone

    """Insira aqui todos metodos e atributos ... """
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__fone

    @telefone.setter
    def telefone(self, telefone):
        self.__fone = telefone
