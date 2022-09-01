from getpass import getpass # Usado para receber a palavra escolhida sem que ela seja mostrada no console

class Forca:
    def __init__(self, palavra):
        self.palavra = [*palavra.upper()] # Transforma a palavra em uma lista com as letras
        self.erros = 0
        self.rodadas = 0
        self.vitoria = False
        self.finalizou = False
        self.entradas = []
        self.letras_disponiveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        # Monta a palavra oculta baseada no tamanho da palavra
        self.parte_descoberta = []
        for i in range(len(self.palavra)):
            self.parte_descoberta.append('_') 
    
    def reiniciar(self, palavra):
        # Reinicia a instância executando novamente a classe construtora
        self.__init__(palavra)

    def status(self): # A função status retorna True se o jogo deve continuar e retorna False se o jogo acabou
        if '_' not in self.parte_descoberta: # Confere se o jogador ganhou o jogo
            self.vitoria = True
            self.finalizou = True
            return False # O jogo finalizou
        
        elif self.erros == 9: # ALTERAR O VALOR DE ERROS
            self.vitoria = False
            self.finalizou = True
            return False # O jogo finalizou
        
        else: # No caso do jogo continuar
            return True # O jogo continuou

    def rodada(self):
        # Entrada da letra escolhida na rodada
        letra_escolhida = str(input("LETRA: ")).upper()
        # Confere se a letra está no alfabeto ou se a letra já foi escolhida
        while (letra_escolhida not in self.alfabeto) or (letra_escolhida not in self.letras_disponiveis):
            letra_escolhida = str(input("LETRA INVÁLIDA, DIGITE NOVAMENTE: ")).upper()
        self.entradas.append(letra_escolhida)
        
        # Determina o resultado da rodada
        if letra_escolhida not in self.palavra: # Se a letra não estiver na palavra
            self.erros += 1
            
        else: # Se a letra estiver na palavra
            # Substitui os espaços vazios com a letra acertada na lista self.parte_descoberta
            for index_posicao, letra in enumerate(self.palavra):
                if letra == letra_escolhida:
                    self.parte_descoberta[index_posicao] = letra_escolhida
        
        # Remove a letra escolhida da lista de letras disponíveis
        self.letras_disponiveis.remove(letra_escolhida)
        # Acrescenta o contador de rodadas
        self.rodadas += 1
    

    def string_parte_descoberta(self): # Formata a parte descoberta até o momento em uma string
        string = ''
        for parte in self.parte_descoberta:
            string += (parte + ' ')
        
        return string

    def print_desenho_atual(self): # Imprime o desenho atual da forca baseado no número de erros
        if self.erros == 0:
            print(" +======+       ")
            print(" |      |       ")
            print(" |              ")
            print(" |              ")
            print(" |              ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 1:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |              ")
            print(" |              ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 2:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |      |       ")
            print(" |              ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 3:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |     /|       ")
            print(" |              ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 4:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |     /|\      ")
            print(" |              ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 5:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |     /|\      ")
            print(" |      |       ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 6:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |     /|\      ")
            print(" |    ^ |       ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 7:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |     /|\      ")
            print(" |    ^ | ^     ")
            print(" |              ")
            print("_|_             ")
        elif self.erros == 8:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |     /|\      ")
            print(" |    ^ | ^     ")
            print(" |     /        ")
            print("_|_             ")
        elif self.erros == 9:
            print(" +======+       ")
            print(" |      |       ")
            print(" |     (_)      ")
            print(" |     /|\      ")
            print(" |    ^ | ^     ")
            print(" |     / \      ")
            print("_|_             ")
    
    def string_alfabeto_disponivel(self):
        string_alfabeto = ''
        for letra in self.alfabeto:
            if letra in self.letras_disponiveis: # Se a letra está disponível
                string_alfabeto += letra + ' '
            else: # Se a letra já foi usado, será mostrada riscada
                string_alfabeto += '- '
        
        return string_alfabeto
    
    def display(self):
        print("\nRODADA: {}".format(self.rodadas))
        self.print_desenho_atual()
        print(self.string_alfabeto_disponivel())
        print(self.string_parte_descoberta())


def __main__():
    palavra = getpass("Digite a palavra da forca [a digitação é escondida]: ")
    print(palavra)

    jogo = Forca(palavra)

    status = True
    while status == True:
        jogo.display()
        jogo.rodada()
        status = jogo.status()
    
    jogo.result()

__main__()