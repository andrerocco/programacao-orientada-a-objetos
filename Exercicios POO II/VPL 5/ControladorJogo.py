from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):

    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    # Permite incluir um novo Personagem na lista de personagens do jogo
    # Deve ser utilizado TipoPersonagem.TIPO
    def inclui_personagem_na_lista(self, energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        if not isinstance(tipo, Tipo):
            return None
        personagem = Personagem(energia,
                                habilidade,
                                velocidade,
                                resistencia,
                                tipo)
        self.__personagems.append(personagem)

        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        # Confere se o personagem está na lista de personagens
        if not personagem in self.__personagems:
            return None
        carta = Carta(personagem)
        self.__baralho.append(carta)

        return carta

    # Inicia o jogo, distribuindo aleatoriamente 5
    # cartas do baralho para cada jogador
    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        for i in range(5):
            carta = random.choice(self.__baralho)
            jogador1.recebe_carta(carta)
            self.__baralho.remove(carta)

            carta = random.choice(self.__baralho)
            jogador2.recebe_carta(carta)
            self.__baralho.remove(carta)

    def jogada(self, mesa: Mesa) -> Jogador:
        carta_jogador1 = mesa.carta_jogador1
        carta_jogador2 = mesa.carta_jogador2

        valor_total1 = carta_jogador1.valor_total_carta()
        valor_total2 = carta_jogador2.valor_total_carta()

        # Verifica se a carta do jogador 1 é maior que a do jogador 2
        if valor_total1 > valor_total2:
            mesa.jogador1.inclui_carta_na_mao(carta_jogador1)
            mesa.jogador1.inclui_carta_na_mao(carta_jogador2)
        # Verifica se a carta do jogador 2 é maior que a do jogador 1
        elif valor_total1 < valor_total2:
            mesa.jogador2.inclui_carta_na_mao(carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(carta_jogador2)
        # Caso as cartas sejam iguais
        else:
            mesa.jogador1.inclui_carta_na_mao(carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(carta_jogador2)

        # Verifica se o jogador 1 perdeu
        if len(mesa.jogador1.mao) == 0:
            return mesa.jogador2
        # Verifica se o jogador 2 perdeu
        elif len(mesa.jogador2.mao) == 0:
            return mesa.jogador1
        # Caso nenhum dos jogadores tenha perdido
        else:
            return None
