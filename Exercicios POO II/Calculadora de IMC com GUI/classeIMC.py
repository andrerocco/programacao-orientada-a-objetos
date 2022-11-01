class IMC:
    def __init__(self, peso: float, altura: float):
        self.peso = peso
        self.altura = altura
        self.imc = self.peso / (self.altura / 100) ** 2
    
    def get_imc(self):
        return self.imc
    
    def get_classificacao(self):
        if self.imc < 18.5:
            return "Abaixo do peso"
        elif self.imc < 25:
            return "Peso ideal"
        elif self.imc < 30:
            return "Sobrepeso"
        elif self.imc < 40:
            return "Obesidade"
        else:
            return "Obesidade mórbida"
