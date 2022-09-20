""" Crie uma classe MatrizEsparsa que pode ser construida das duas formas
abaixo, e contenha métodos para mostrar a matriz no formato String e também no
formato de dicionário.
1) receber uma dupla (tupla com 2 elementos) indicando quantas linhas e colunas
tem a matriz, e um dicionário com duplas como chave (linha, coluna) e um valor
numérico.
2) Receber uma string no seguinte formato:
matriz = '''0 8 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0
            0 2 0 0 0 0 1 0 0
            0 0 0 0 0 0 0 0 0
            0 0 0 7 0 0 0 0 0
            0 0 0 0 0 0 4 0 0'''
*dica: use os métodos splitlines() e split da classe String, e o método get() da classe dict """

class MatrizEsparsa:
    def __init__(self, tupla, dicionario):
        self.linhas = tupla[0]
        self.colunas = tupla[1]
        self.dicionario = dicionario

    def __str__(self):
        string = ""
        for i in range(self.linhas):
            for j in range(self.colunas):
                string += str(self.dicionario.get((i, j), 0)) + " "
            string += "\n"
    
        return string
    
    def iniciar_com_matriz(self, matriz):
        self.linhas = len(matriz.splitlines())
        self.colunas = len(matriz.splitlines()[0].split())
        self.dicionario = {}
        for i, linha in enumerate(matriz.splitlines()):
            for j, coluna in enumerate(linha.split()):
                if coluna != "0":
                    self.dicionario[(i, j)] = int(coluna)
    

matriz = MatrizEsparsa((6, 9), {(0, 1): 8, (2, 1): 2, (2, 6): 1, (4, 3): 7, (5, 6): 4})
print(matriz)

matriz.iniciar_com_matriz('''0 8 0 0 0 0 0 0 0
                             0 0 0 0 0 0 0 0 0
                             0 2 0 0 0 0 1 0 0
                             0 0 0 0 0 0 0 0 0
                             0 0 0 7 0 0 0 0 0
                             0 0 0 0 0 0 4 0 0''')
print(matriz)