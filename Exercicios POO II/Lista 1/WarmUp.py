from email.errors import MalformedHeaderDefect
from mailbox import NotEmptyError


class Televisao:
    #1
    def __init__(self, canal, tamanho, marca, canal_minimo = 2, canal_maximo = 14):
        self.ligada = False
        self.canal = canal
        #2
        self.tamanho = tamanho
        self.marca = marca
        #4
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo

    #3
    def muda_canal_para_cima(self):
        #4
        if self.canal == self.canal_maximo:
            self.canal = self.canal_minimo
        else:
            self.canal += 1

    def muda_canal_para_baixo(self):
        #4
        if self.canal == self.canal_minimo:
            self.canal = self.canal_maximo
        else:
            self.canal -= 1

#2
tv1 = Televisao(2, 46, "Samsung")
tv2 = Televisao(9, 88, "LG")
print("Tamanho: {}, Marca: {}".format(tv1.tamanho, tv1.marca))
print("Tamanho: {}, Marca: {}".format(tv2.tamanho, tv2.marca))

#6
tv3 = Televisao(2, 46, "Samsung", "Globo", "Record")
tv4 = Televisao(9, 88, "LG", "History", "Discovery")


#7
class Estado:
    def __init__(self, nome, sigla, cidades=[]):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        self.populacao = 0
        
        for cidade in cidades:
            self.populacao += cidade.populacao

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

florianopolis = Cidade("Florianópolis", 508826)
blumenal = Cidade("Blumenal", 361855)
santa_catarina = Estado("Santa Catarina", "SC", [florianopolis, blumenal])
print("População de SC: {}".format(santa_catarina.populacao))

rio_de_janeiro_cidade = Cidade("Rio de Janeiro", 6748000)
niteroi = Cidade("Niterói", 515317)
rio_de_janeiro_estado = Estado("Rio de Janeiro", "RJ", [rio_de_janeiro_cidade, niteroi])
print("População de RJ: {}".format(rio_de_janeiro_estado.populacao))

recife = Cidade("Recife", 1653461)
petrolina = Cidade("Petrolina", 354317)
pernambuco = Estado("Pernambuco", "PE", [recife, petrolina])
print("População de PE: {}".format(pernambuco.populacao))


#8
from math import sqrt, degrees, atan2, pi

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar_coordenada(self):
        print("X: {}, Y: {}".format(self.x, self.y))
    
    def calcular_distancia(self, x_comparar, y_comparar):
        delta_x = abs(self.x - x_comparar)
        delta_y = abs(self.y - y_comparar)
        distancia = sqrt(delta_x**2 + delta_y**2)

        return distancia
    
    def comparar_coordenadas(self, coordenada_comparar):
        print("X1: {}, X2: {}".format(self.x, coordenada_comparar.x))
        print("Y1: {}, Y2: {}".format(self.y, coordenada_comparar.y))
    
    def calcular_coordenada_polar(self):
        hipotenusa = self.calcular_distancia(0, 0)
        A = self.x
        B = self.y
        angulo = (int(round(degrees(atan2(A,B))))) # Ângulo arredondado em graus
        
        return (hipotenusa, angulo)


coord1 = Coordenada(45, 45)
coord2 = Coordenada(480, 230)
print(coord1.calcular_distancia(coord2.x, coord2.y))
coord1.comparar_coordenadas(coord2)
print(coord1.calcular_coordenada_polar())


#9
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        self.area = lado*lado

class Retangulo:
    def __init__(self, lado1, lado2):
        self.x = lado1
        self.y = lado2
        self.area = lado1*lado2

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = pi*raio*raio


#10
class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def soma(self, fracao):
        denominador_resultado = self.denominador * fracao.denominador
        numerador_resultado = (self.denominador/denominador_resultado)*self.numerador + (fracao.denominador/denominador_resultado)*fracao.numerador

        return (numerador_resultado, denominador_resultado)
    
    def subtracao(self, fracao):
        ...
    
    def multiplicacao(self, fracao):
        numerador_resultado = self.numerador * fracao.numerador
        denominador_resultado = self.denominador * fracao.denominador

        return (numerador_resultado, denominador_resultado)
    
    def divisao(self, fracao):
        numerador_resultado = self.numerador * fracao.denominador
        denominador_resultado = self.denominador * fracao.numerador

        return (numerador_resultado, denominador_resultado)
    
    def inverter_fracao(self):
        self.numerador ,self.denominador = self.denominador, self.numerador
    
    def valor_float(self):
        valor = self.numerador / self.denominador
        
        return valor
    
    def real_para_fracao(self, valor_real):
        fracao = (int(valor_real)).as_integer_ratio()
        self.numerador = fracao[0]
        self.denominador = fracao[1]

        return fracao