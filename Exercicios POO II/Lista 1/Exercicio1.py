from datetime import date

class ContaCorrente:
    def __init__(self, titulares):
        self.titular = [] # Pode conter um ou mais titulares
        self.saldo = 0
        self.movimentos = [] # Armazena as movimentações da conta
    
    def depositar(self, montante):
        self.saldo += montante
        self.movimentos.append('+{}'.format(montante))
    
    def sacar(self, montante):
        self.saldo -= montante
        self.movimentos.append('-{}'.format(montante))
    
    def get_saldo(self):
        return self.saldo
    
    def get_movimentos(self):
        for movimento in self.movimentos:
            print(movimento)
    
class Titular:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def get_nome(self):
        return self.nome
    
    def get_telefone(self):
        return self.telefone