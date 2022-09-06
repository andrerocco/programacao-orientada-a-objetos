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
        for i in range(max(len( self.lista_coeficientes, len(outro_polinomio.get_lista_coeficientes()) ))):
            lista_novos_coeficientes.append(self.lista_coeficientes[i] + self.lista_coeficientes[i])
        
        if len(self.lista_coeficientes) > len(outro_polinomio.get_lista_coeficientes()):
            coeficientes_faltantes = range( len(outro_polinomio.get_lista_coeficientes())+1 , len(self.lista_coeficientes) )
            for i in coeficientes_faltantes:
                lista_novos_coeficientes.append(self.lista_coeficientes[i])

        elif len(outro_polinomio.get_lista_coeficientes()) > len(self.lista_coeficientes):
            coeficientes_faltantes = range( len(self.lista_coeficientes) + 1, len(outro_polinomio.get_lista_coeficientes()) )
            for i in coeficientes_faltantes:
                lista_novos_coeficientes.append(outro_polinomio.get_lista_coeficientes()[i])

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