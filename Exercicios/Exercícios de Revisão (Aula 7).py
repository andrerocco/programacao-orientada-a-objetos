# 1017

tempo = int(input("Tempo gasto na viagem (horas): "))
velocidade_media = int(input("Velocidade media da viagem (km/h): "))

distancia = tempo * velocidade_media
litros_gastos = distancia / 12

print("{:.3f}".format(litros_gastos))

# 2927

entrada = (str(input())).split()
alunos = int(entrada[0])
computadores = int(entrada[1])
queimados = int(entrada[2])
sem_compilador = int(entrada[3])

computadores_validos = computadores - queimados - sem_compilador - 1

if computadores_validos >= alunos:
    print("Igor feliz!")
else:
    if queimados > (sem_compilador/2):
        print("Caio, a culpa eh sua!")
    elif alunos > computadores_validos:
        print("Igor bolado!")

# 1046

entrada = (str(input())).split()
inicio = int(entrada[0])
fim = int(entrada[1])

if inicio == fim:
    print("O JOGO DUROU 24 HORA(S)")
if inicio > fim:
    duracao = (24-inicio) + fim
    print("O JOGO DUROU {} HORA(S)".format(duracao))
if inicio < fim:
    duracao = fim - inicio
    print("O JOGO DUROU {} HORA(S)".format(duracao))

# 2434

entrada = (str(input())).split()

numero_de_dias = int(entrada[0])
saldo = int(entrada[1])
menor_saldo = 10000 # 10^3, valor max da entrada

for i in range(numero_de_dias):
    movimento = int(input())
    saldo = saldo + movimento
    
    if saldo < menor_saldo:
        menor_saldo = saldo

print(menor_saldo)

# 2116

def primo_proximo(num):
    contador = num
    
    while True:
        multiplos = 0
        for i in range(2, contador):
            if contador % i == 0:
                multiplos += 1
        if multiplos == 0:
            primo = contador
            break
        contador -= 1

    return primo

entrada = (str(input())).split()
n = int(entrada[0])
m = int(entrada[1])

primo_n = primo_proximo(n)
primo_m = primo_proximo(m)

multiplicacao = primo_n * primo_m

print(multiplicacao)
