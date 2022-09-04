from random import randint

class CampoMinado:
    def __init__(self, tamanho_campo):
        self.tamanho_campo = tamanho_campo # Define o tamanho da matriz quadrada usada pelo campo
        self.posicoes_entradas = [] # É uma lista de tuplas com as posições já inseridas pelo usuário
        
        self.matriz_bombas = [] # Contém bombas nos espaços com 1
        # Gera de forma aleatória a matriz com as bombas
        for linha in range(tamanho_campo):
            self.matriz_bombas.append([])
            for coluna in range(tamanho_campo):
                num = randint(0, 4)
                if num == 4:
                    self.matriz_bombas[linha].append(1)
                else:
                    self.matriz_bombas[linha].append(0)
        
    def conferir_bomba(self, posicao):
        if self.matriz_bombas[posicao[0]][posicao[1]] == 1:
            return True
        else:
            return False
    
    def gerar_matriz_usuario(self, posicao):
        ...
