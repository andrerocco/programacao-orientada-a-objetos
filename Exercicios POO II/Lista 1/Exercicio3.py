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
    
    def somar_polinomio(self, outro_polinomio):
        lista_novos_coeficientes = []
        p2_coeficientes = outro_polinomio.get_lista_coeficientes()

        for i in range(min( len(self.lista_coeficientes) , len(p2_coeficientes ))):
            lista_novos_coeficientes.append(self.lista_coeficientes[i] + p2_coeficientes[i])
        
        if len(self.lista_coeficientes) > len(p2_coeficientes):
            coeficientes_faltantes = list( range( len(p2_coeficientes) , len(self.lista_coeficientes) ) )
            for i in coeficientes_faltantes:
                lista_novos_coeficientes.append(self.lista_coeficientes[i])

        elif len(p2_coeficientes) > len(self.lista_coeficientes):
            coeficientes_faltantes = list( range( len(self.lista_coeficientes), len(p2_coeficientes) ) )
            for i in coeficientes_faltantes:
                lista_novos_coeficientes.append(p2_coeficientes[i])

        self.__init__(lista_novos_coeficientes)
    
    def multiplicar_polinomio(self, outro_polinomio):
        ...
    
    def avaliar_resultado(self, x):
        resultado = 0
        for expoente, coeficiente in enumerate(self.lista_coeficientes):
            resultado += coeficiente * (x**expoente) 

        return resultado   
    
    # Getters
    def get_grau(self):
        return self.grau
    def get_lista_coeficientes(self):
        return self.lista_coeficientes

contador = 0
lista_coeficientes = []

print("\nDigite os coeficientes do polinômio. Digite 'P' para parar.")
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

p2 = Polinomio([1.0, 1.0, 1.0])

p1.somar_polinomio(p2)
print(p1.string_polinomio())