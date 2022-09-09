class ContaCorrente:
    def __init__(self, titulares):
        self.titular = [] # Pode conter um ou mais titulares
        self.saldo = 0
        self.movimentos = [] # Armazena as movimentações da conta
    
    def depositar(self, montante):
        self.saldo += montante
        self.movimentos.append('+{}'.format(montante))
    
    def sacar(self, montante):
        if montante > self.saldo:
            print("Saldo insuficiente. O valor máximo possível de saque é $ {}".format(self.saldo))
        else:
            self.saldo -= montante
            self.movimentos.append('-{}'.format(montante))
    
    def print_movimentos(self):
        for movimento in self.movimentos:
            print(movimento)
        
    def print_informacoes(self):
        for titular in self.titular:
            print(titular.get_nome())
        print("Saldo: {}".format(self.saldo))
        print("")
    
    # Getters
    def get_titulares(self):
        return self.titular
    def get_saldo(self):
        return self.saldo
    def get_movimentos(self):
        return self.movimentos
    
class Titular:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    # Getters
    def get_nome(self):
        return self.nome
    def get_telefone(self):
        return self.telefone