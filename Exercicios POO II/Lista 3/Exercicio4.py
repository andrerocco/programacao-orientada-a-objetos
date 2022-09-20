""" Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Escreva um programa que leia todos os tempos em segundos e os guarde em um
dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta
da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O
campeão é o que tem a menor média de tempos. """

corredores = {}

for i in range(6):
    nome = input("Nome do corredor: ")
    tempos = []
    for j in range(10):
        tempos.append(float(input("Tempo da volta {} em segundos: ".format(j + 1))))
    corredores[nome] = tempos

melhores_voltas = {}
for i in corredores.keys():
    melhores_voltas[i] = (melhor_volta, numero_volta) = min(enumerate(corredores[i]), key=lambda x: x[1])

melhor_volta_geral = (corredor, melhor_volta) = min(melhores_voltas.items(), key=lambda x: x[1][1])
print("\nMelhor volta da prova: {} na volta {} do corredor {}".format(melhor_volta[1], melhor_volta[0] + 1, corredor))

media_tempos = {}
for i in corredores.keys():
    media_tempos[i] = sum(corredores[i]) / len(corredores[i])

classificacao = sorted(media_tempos.items(), key=lambda x: x[1])

print("Classificação final:")
for i in range(len(classificacao)):
    print("\n{}º lugar: {} com média de {}s".format(i + 1, classificacao[i][0], classificacao[i][1]))
