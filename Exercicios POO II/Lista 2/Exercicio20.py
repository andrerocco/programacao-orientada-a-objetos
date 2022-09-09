class MinhaLista:
    def __init__(self, *valores):
        self.__tupla = valores
        
        # print(valores)
        # print(type(valores))
    
    def __getitem__(self, key): # Magic method que torna possível invocar a classe pelo índice 
        return self.__tupla[key]
    
    def __setitem__(self, key, value): # Magic method que torna possível atribuir elementos usando o índice
        lista = list(self.__tupla)
        lista[key] = value

        self.__tupla = tuple(lista)
    
    def __str__(self):
        string = str(self.__tupla).replace('(','[').replace(')',']')
        return string

    def append(self, element):
        self.__tupla = (*self.__tupla, element)
    
    def remove(self, element):
        lista = list(self.__tupla)
        for i, elemento_atual in enumerate(lista):
            if elemento_atual == element:
                lista.pop(i)
                self.__tupla = tuple(lista)
                
                return # Para a função

        print('Elemento não encontrado.') 
        
    def sort(self):
        try:
            lista = list(self.__tupla).sort()
            
            self.__tupla = tuple(lista)
        except:
            print('Não foi possível ordenar a lista.')
    
    def reverse(self):
        lista = list(self.__tupla)
        lista_reversed = []

        for elemento in lista[::-1]:
            lista_reversed.append(elemento)
        
        self.__tupla = tuple(lista_reversed)
    
    def pop(self, index = -1):
        if index in range(len(self.__tupla)):
            lista = list(self.__tupla)
            lista.pop(index)

            self.__tupla = tuple(lista)
        else:
            print('Index fora de alcance.')