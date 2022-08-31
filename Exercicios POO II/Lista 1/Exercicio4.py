class SeriesMatematicas:
    def __init__(self, fibonacci_length = 10, fatorial_length = 10, fibonarial_length = 10, primo_length = 10):
        self.fibonacci = self.set_fibonacci(fibonacci_length)
        self.fatorial = self.set_fatorial(fatorial_length)
    
    def set_fibonacci(self, length):
        fibonacci_sequence = []
        
        def fibonacci(n):
            if n==1:
                return 0
            elif n==2:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        
        for size in range(1, length+1):
            fibonacci_sequence.append(fibonacci(size))
        
        self.fibonacci = fibonacci_sequence

    def set_fatorial(self, length):
        ...
    
    # Getters
    def get_fibonacci(self):
        return self.fibonacci
    def get_fatorial(self):
        return self.fatorial
    def get_fibonarial(self):
        return self.fibonarial
    def get_primo(self):
        return self.primo
        