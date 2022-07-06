anos = int(input("Digite seus anos de idade: "))
meses = int(input("Digite seus meses de idade: "))
dias = int(input("Digite seus dias de idade: "))

idade_em_dias = int((anos*365) + (meses*30) + dias)
print("Sua idade em dias é {}".format(idade_em_dias))