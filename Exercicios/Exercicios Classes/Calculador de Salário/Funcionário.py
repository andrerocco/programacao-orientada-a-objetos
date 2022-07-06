class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
        if self.salario >= 1500 and self.salario < 1750:
            self.salario_ajuste = self.salario*(1.12)
        elif self.salario >= 1750 and self.salario < 2000:
            self.salario_ajuste = self.salario*(1.1)
        elif self.salario >= 2000 and self.salario < 3000:
            self.salario_ajuste = self.salario*(1.07)
        elif self.salario >= 3000:
            self.salario_ajuste = self.salario*(1.05)
        
    def getResultado(self):
        print(f"Nome: {self.nome}")
        print(f"Salario atual: R$ {self.salario:.2f}")
        print(f"Salario ajustado: R$ {self.salario_ajuste:.2f}")