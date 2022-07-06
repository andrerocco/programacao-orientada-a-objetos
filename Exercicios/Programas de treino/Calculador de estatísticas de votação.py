eleitores = int(input("Número total de eleitores: "))
votos_validos = int(input("Número de votos válidos: "))
votos_brancos = int(input("Número de votos brancos: "))
votos_nulos = int(input("Número de votos nulos: "))

total_votos = votos_validos + votos_brancos + votos_nulos

porcentagem_total = (total_votos / eleitores)
porcentagem_validos = (votos_validos / total_votos)
porcentagem_brancos = (votos_brancos / total_votos)
porcentagem_nulos = (votos_nulos / total_votos)

print("\n------ ESTATÍSTICAS DA ELEIÇÃO ------\n")

if (eleitores == total_votos):
    print("Todos os eleitores votaram")
else:
    print("{:7.1%}s dos eleitores votaram".format(porcentagem_total))

print("{:7.1%} dos votos foram válidos ( {:,} validos / {:,} total de votos )".format(porcentagem_validos, votos_validos, total_votos))
print("{:7.1%} dos votos foram brancos ( {:,} brancos / {:,} total de votos )".format(porcentagem_brancos, votos_validos, total_votos))
print("{:7.1%} dos votos foram nulos   ( {:,} nulos / {:,} total de votos )".format(porcentagem_nulos, votos_nulos, total_votos))
