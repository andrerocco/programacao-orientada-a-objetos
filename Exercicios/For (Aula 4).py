#EXERCÍCIO 1

for x in range(2004, 2101):
    if(x%4 == 0):
        print(x)

#EXERCÍCIO 2

for x in range(1, 51):
    if(x%2 != 0):
        print(x)

#EXERCÍCIO 3

maior_nome = ""
maior_nota = 0
maior_valor = ""

for x in range(0, 5):
    nome = str(input("Nome: "))
    nota = float(input("Média: "))
    valor = float(input("Valor da mensalidade: R$ "))
    
    if(nota > maior_nota):
        maior_nome = nome
        maior_nota = nota
        maior_valor = valor

desconto = maior_valor * 0.7

print("\n---------- Resultado ----------")
print("Aluno com a melhor nota: {}".format(maior_nome))
print("Nota: {}".format(maior_nota))
print("Valor da mensalidade inicial: R$ {}".format(maior_valor))
print("Valor da mensalidade com desconto: R$ {:.2f}".format(desconto))

#EXERCÍCIO 4
pares = 0
impares = 0
for x in range(0, 11, 1):
    numero = int(input("Número: "))
    if(numero%2 == 0):
        pares += 1
    else:
        impares += 1

print("Número pares: {}".format(pares))
print("Número impares: {}".format(impares))

#EXERCÍCIO 5
#EXERCÍCIO 6

numero = int(input("Insira um número: "))

confirmar = 0
for i in range(2, numero):
    if(numero%i == 0):
        print("O número {} é divisível por {}".format(numero, i))
        confirmar += 1

if(confirmar == 0):
    print("O número {} é primo".format(numero))

#EXERCÍCIO 7

pessoas = int(input("Número de pessoas: "))

soma_idades = 0
for i in range(pessoas):
    idade = int(input("Idade: "))
    
    soma_idades += idade

media = soma_idades / pessoas

print("A média das idades das {} pessoas é {:.1f}".format(pessoas, media))

#EXERCÍCIO 8

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if(n1 < n2):
    print("Os números inteiros no intervalo {} e {} são:".format(n1, n2))
    for i in range(n1+1, n2):
        print(i)
elif(n1 > n2):
    print("Os números inteiros no intervalo {} e {} são:".format(n2, n1))
    for i in range(n2+1, n1):
        print(i)
else:
    print("Os números são iguais")

#EXERCÍCIO 9

print("--------- GERADOR DE TABUADA ---------")
numero = int(input("Escolha um número entre 1 e 10: "))

for i in range(1, 11):
    resultado = numero * i
    print("{:3} x {:^3} = {:3}".format(numero, i, resultado))

#EXERCÍCIO 10
    
print("--------- CALCULAR MÉDIA ---------")
soma_notas = 0
maior_nota = 0
aluno_maior_nota = 0

for i in range(5):
    nota = float(input("Nota do aluno 0{}: ".format(i+1)))
    soma_notas += nota
    
    if(nota > maior_nota):
        maior_nota = nota
        aluno_maior_nota = i+1
    
    if(nota >= 5.75):
        print("RESULTADO: APROVADO".format(i+1))
    elif(nota >= 2.75):
        print("RESULTADO: EM RECUPERAÇÃO".format(i+1))
    elif(nota < 2.75):
        print("RESULTADO: REPROVADO".format(i+1))

media = soma_notas / 5

print("\n--------- ESTATÍSTICAS ---------")
print("Média da turma = {:.2f}".format(media))
print("Aluno com a maior nota = Aluno 0{}, com nota {}".format(aluno_maior_nota, maior_nota))