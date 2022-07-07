class Cachorro:
    def __init__(self, nome_dono, nome_animal, raca, peso, idade, cor_pelo):
        self.nome_dono = nome_dono
        self.nome_animal = nome_animal
        self.raca = raca
        self.peso = peso
        self.idade = idade
        self.cor_pelo = cor_pelo

    # Setters
    def setNomeDono(self, nome_dono):
        self.nome_dono = nome_dono
    def setNomeAnimal(self, nome_animal):
        self.nome_animal = nome_animal
    def setRaca(self, raca):
        self.raca = raca
    def setPeso(self, peso):
        self.peso = peso
    def setIdade(self, idade):
        self.idade = idade
    def setCorPelo(self, cor_pelo):
        self.cor_pelo = cor_pelo

    # Getters
    def getNomeDono(self):
        return self.nome_dono
    def getNomeAnimal(self):
        return self.nome_animal
    def getRaca(self):
        return self.raca
    def getPeso(self):
        return self.peso
    def getIdade(self):
        return self.idade
    def getCorPelo(self):
        return self.cor_pelo