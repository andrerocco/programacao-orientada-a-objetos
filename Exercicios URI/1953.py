# 1953

while True:
    try:
        numero_alunos = int(input())
        epr = 0
        ehd = 0
        intruso = 0
        
        for i in range(numero_alunos):
            matricula, curso = input().split()
            if curso == 'EPR':
                epr += 1
            elif curso == 'EHD':
                ehd += 1
            else:
                intruso += 1
        
        print("EPR: {}".format(epr))
        print("EHD: {}".format(ehd))
        print("INTRUSOS: {}".format(intruso))
        
    except EOFError:
        break