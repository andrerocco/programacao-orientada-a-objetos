from getpass import getpass # Usado para receber a palavra escolhida sem que ela seja mostrada no console

class Forca:
    def __init__(self, palavra):
        self.palavra = [*palavra.upper()] # Transforma a palavra em uma lista com as letras
        self.erros = 0
        self.rodadas = 0
        self.vitoria = False
        self.entradas = []
        self.letras_disponiveis = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        # self.alfabeto = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def iniciar_jogo(self):
        parte_descoberta = []
        for i in range(len(self.palavra)):
            parte_descoberta.append('_') 

    def rodada(self):
        letra_escolhida = str(input("LETRA: ")).upper
        while letra_escolhida not in self.alfabeto:
            print("\nLETRA INVÁLIDA, DIGITE NOVAMENTE: ")
            letra_escolhida = str(input()).upper
        
        if letra_escolhida not in palavra: # Se a letra não estiver na palavra
            ...
        else: # Se a letra estiver na palavra
            ...
    
    def reiniciar_jogo():
        ...
        


def __main__():
    palavra = getpass("Digite a palavra da forca [a digitação é escondida]: ")
    print(palavra)

    while True:
        ...




__main__()