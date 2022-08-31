from math import sqrt

class SeriesMatematicas:
    def __init__(self, fibonacci_length = 10, fatorial_length = 10, fibonarial_length = 10, primo_length = 10):
        self.set_fibonacci(fibonacci_length)
        self.set_fatorial(fatorial_length)
        self.set_fibonarial(fibonarial_length)
        self.set_primo(primo_length)
    
    def set_fibonacci(self, length):
        # Fibonacci recursivo
        def fibonacci(n):
            if n==1:
                return 0
            elif n==2:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        
        # Lista que armazena a sequência
        fibonacci_sequence = []
        
        for size in range(1, length+1):
            fibonacci_sequence.append(fibonacci(size))
        
        self.fibonacci = fibonacci_sequence

    def set_fatorial(self, length):
        # Fatorial recursivo
        def fatorial(n):
            if n == 0 or n == 1:
                return 1 
            else:
                return n * fatorial(n - 1)
        
        # Lista que armazena a sequência
        lista_fatorial = []
        
        for i in range(1, length + 1):
            lista_fatorial.append(fatorial(i))
            
        self.fatorial = lista_fatorial
    
    def set_fibonarial(self, length):
        # Fibonarial recursivo
        def fibonarial(n):
            if n==1:
                return 1 
            elif n==2:
                return 2
            else:
                return fibonarial(n-1) * fibonarial(n-2)
        
        # Lista que armazena a sequência
        fibonarial_sequence = []

        for size in range(1, length+1):
            fibonarial_sequence.append(fibonarial(size))

        self.fibonarial = fibonarial_sequence
    
    def set_primo(self, length):
        # Lista que armazena a sequência
        primos_sequence = []
            
        contador = 0
        i = 1

        while contador < length:
            divisores_numero = 0

            # Acha o número de divisores
            limit = int(sqrt(i))
            for k in range(1, limit+1):
                if (i % k == 0): 
                    divisores_numero += 1
                    if (k != i/k):
                        divisores_numero += 1

            # Confere se o número é primo
            if (divisores_numero == 2 or divisores_numero == 1):
                primos_sequence.append(i)
                contador += 1

            i += 1
        
        self.primo = primos_sequence

    
    # Getters
    def get_fibonacci(self):
        return self.fibonacci
    def get_fatorial(self):
        return self.fatorial
    def get_fibonarial(self):
        return self.fibonarial
    def get_primo(self):
        return self.primo

sequencias = SeriesMatematicas(10)
print(sequencias.get_fatorial())
print(sequencias.get_fibonacci())
print(sequencias.get_fibonarial())
print(sequencias.get_primo())