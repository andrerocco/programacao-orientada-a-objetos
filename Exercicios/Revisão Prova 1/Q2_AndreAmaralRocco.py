# André Amaral Rocco

def resultados(entrevistados, total_idade, salarios_maior_2000, idade_menor_salario, sexo_menor_salario, nome_maior_idade, maior_idade):
    print("--------- Resultados ---------")
    
    media_idade = total_idade / entrevistados
    print("A média de idade dos {} entrevistados era de {:.1f}".format(entrevistados, media_idade))

    print("{} mulheres entrevistadas tem salário maior que R$ 2000.00".format(salarios_maior_2000))
    
    print("A pessoa com menor salário tem {} anos e é do sexo {}".format(idade_menor_salario, sexo_menor_salario))
    
    print("O morador mais velho é {} e tem {} anos".format(nome_maior_idade, maior_idade))

contador = 1
total_idade = 0
salarios_maior_2000 = 0
menor_salario = -1
maior_idade = -1

while True:
    print("--------- Entrevistado {} ---------".format(contador))
    nome = str(input("Nome: "))
    idade = int(input("Idade do entrevistado: "))
    sexo = str(input("Sexo [M/F]: "))
    salario = float(input("Salário: "))

    total_idade += idade
    
    if sexo == "F" and salario > 2000:
        salarios_maior_2000 += 1
    
    if salario < menor_salario or menor_salario == -1:
        menor_salario = salario
        sexo_menor_salario = sexo
        idade_menor_salario = idade

    if idade > maior_idade or maior_idade == -1:
        maior_idade = idade
        nome_maior_idade = nome

    contador += 1
    
    print("Continuar cadastrando? [S/N]")
    continuar = str(input())
    if continuar == "N":
        resultados(contador, total_idade, salarios_maior_2000, idade_menor_salario, sexo_menor_salario, nome_maior_idade, maior_idade)
        break