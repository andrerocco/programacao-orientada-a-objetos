from petshopCadastro import Cachorro

class VIP(Cachorro):
    def __init__(self, nome_dono, nome_animal, raca, peso, idade, cor_pelo, banho, restricao=False):
        super().__init__(nome_dono, nome_animal, raca, peso, idade, cor_pelo)
        self.periocidade_banho = banho
        self.resticao_alimentar = restricao
    
    # Setters
    def setBanho(self, banho):
        self.periocidade_banho = banho
    def setRestricaoAlimentar(self, restricao):
        self.resticao_alimentar = restricao

    # Getters
    def getBanho(self):
        return self.periocidade_banho
    def getRestricaoAlimentar(self):
        return self.resticao_alimentar