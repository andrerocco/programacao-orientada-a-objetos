# 1430

notas = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}
 
while True:
    entrada = str(input())
    if entrada == '*':
        break
    
    entrada = entrada.split('/')
    
    corretos = 0
    for compasso in entrada:
        soma = 0
        for nota in range(len(compasso)):
            soma += notas[compasso[nota]]
        if soma == 1:
            corretos += 1
    
    print(corretos)