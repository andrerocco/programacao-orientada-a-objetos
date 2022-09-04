from random import randint

class CampoMinado:
    def __init__(self, tamanho_campo):
        self.tamanho_campo = tamanho_campo # Define o tamanho da matriz quadrada usada pelo campo
        self.posicoes_entradas = [] # É uma lista de tuplas com as posições já inseridas pelo usuário
        
        self.matriz_bombas = []
        # Gera de forma aleatória a matriz com as bombas
        for linha in range(tamanho_campo):
            self.matriz_bombas.append([])
            for coluna in range(tamanho_campo):
                num = randint(0, 5)
                if num == 5:
                    self.matriz_bombas[linha].append(1)
                else:
                    self.matriz_bombas[linha].append(0)
