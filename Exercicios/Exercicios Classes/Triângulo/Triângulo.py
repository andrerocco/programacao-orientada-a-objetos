class Triangulo:
    def __init__(self, l1, l2, l3):
        lados = sorted([l1, l2, l3], reverse=True)
        if lados[0] < lados[1] + lados[2]:
            self.lados = lados[:]
            
            if self.lados[0] == self.lados[1] == self.lados[2]:
                self.tipo = 'Equilátero'
            elif self.lados[0] == self.lados[1]:
                self.tipo = 'Isóceles'
            else:
                self.tipo = 'Escaleno'
        else:
            print("Os lados não formam um triângulo")
