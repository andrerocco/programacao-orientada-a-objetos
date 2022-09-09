print("Responda as seguintes perguntas [S/N]:")
r1 = str(input("Telefonou para a vítima? ")).upper()
r2 = str(input("Esteve no local do crime? ")).upper()
r3 = str(input("Mora perto da vítima? ")).upper()
r4 = str(input("Devia para a vítima? ")).upper()
r5 = str(input("Já trabalhou com a vítima? ")).upper()

vetor_respostas = [r1, r2, r3, r4, r5]

resposta_positivas = 0
for reposta in vetor_respostas:
    if reposta == "S":
        resposta_positivas += 1

if resposta_positivas == 2:
    print("Suspeita")
elif resposta_positivas == 3 or resposta_positivas == 4:
    print("Cúmplice")
elif resposta_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
