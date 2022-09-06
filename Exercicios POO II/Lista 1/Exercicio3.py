from math import ceil


class Polinomio:
    def __init__(self, lista_coeficientes):
        self.lista_coeficientes = lista_coeficientes
        self.grau = len(lista_coeficientes) - 1
    
    def string_polinomio(self):
        string_polinomio = ''
        for expoente, coeficiente in enumerate(self.lista_coeficientes):
            string_polinomio += ' + '

            # Confere se o float é inteiro
            if ceil(coeficiente) == coeficiente:
                string_polinomio += '{} . x^{}'.format(int(coeficiente), expoente)
            else:
                string_polinomio += '{} . x^{}'.format(str(coeficiente).replace('.',','), expoente)

        return string_polinomio
    
    def get_grau(self):
        return self.grau
    
    def somar_polinomio(self, outro_polinomio):
        ...
    
    def multiplicar_polinomio(self, outro_polinomio):
        ...
    
    def avaliar_resultado(self, x):
        resultado = 0
        for expoente, coeficiente in enumerate(self.lista_coeficientes):
            resultado += coeficiente * (x**expoente) 

        return resultado   

contador = 0
lista_coeficientes = []

print("Digite os coeficientes do polinômio. Digite 'P' para parar.")
while True:
    coeficiente = str(input("Coeficiente de x^{}: ".format(contador)))
    if coeficiente.upper() == 'P':
        break
    else:
        try:
            lista_coeficientes.append(float(coeficiente))
            contador += 1
        except ValueError:
            print('Inválido, digite novamente')


p1 = Polinomio(lista_coeficientes)
print(p1.string_polinomio())
print(p1.get_grau())
print(p1.avaliar_resultado(4))