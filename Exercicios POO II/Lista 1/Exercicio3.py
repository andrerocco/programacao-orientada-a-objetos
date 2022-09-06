from math import ceil


class Polinomio:
    def __init__(self, lista_coeficientes):
        self.lista_coeficientes = lista_coeficientes
    
    def string_polinomio(self):
        string_polinomio = ''
        for expoente, coeficiente in enumerate(self.lista_coeficientes):
            
            # Confere se é negativo ou positivo ou se é o ultimo coeficiente do polinômio
            if coeficiente >= 0:
                string_polinomio += ' + '
            elif coeficiente < 0:
                string_polinomio += ' - '
            
            # Confere se o float é inteiro
            if ceil(coeficiente) == coeficiente:
                string_polinomio += '{} . x^{}'.format(int(coeficiente), expoente)
            else:
                string_polinomio += '{} . x^{}'.format(str(coeficiente).replace('.',','), expoente)


        return string_polinomio
    

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