# 1758

casos = int(input())
for c in range(casos):
    provas, numero_alunos = [int(x) for x in input().split()]
    
    for a in range(numero_alunos):
        notas = [float(x) for x in input().split()]
        
        # Calcula a média do aluno
        soma_notas = 0
        for i in notas:
            soma_notas += i
        media = soma_notas / provas
    
        # A nota final dos alunos reprovados se mantém
        if media < 4:
            nota_final = media
    
        # Substitui a média pela maior nota desde que não mude a situação de aprovação
        if media >= 7:
            nota_final = max(notas)
        elif media >= 4 and max(notas) < 7:
            nota_final = max(notas)
        else:
            nota_final = media
    
        print("{:.2f}".format(nota_final))

# 2422

numero_casas = int(input())

lista_casa = []
for c in range(numero_casas):
    casa = int(input())
    lista_casa.append(casa)
soma_das_escondidas = int(input())

for i in range(len(lista_casa)):
    for j in range(len(lista_casa)-i-1):
        soma = lista_casa[i] + lista_casa[i+j+1]
        if soma == soma_das_escondidas:
            break
    else:
        continue
    break


print("{} {}".format(lista_casa[i], lista_casa[i+j+1]))

# 2650

numero_titans, tamanho_muralha = [int(x) for x in input().split()]

matriz_titans = []
for i in range(numero_titans):
    info = str(input())
    nome = (''.join([letra for letra in info if not letra.isdigit()])).strip()
    altura = int(''.join([letra for letra in info if letra.isdigit()]))
    
    titan = []
    titan.append(nome)
    titan.append(altura)
    matriz_titans.append(titan)

for x in matriz_titans:
    if x[1] > tamanho_muralha:
        print(x[0])
