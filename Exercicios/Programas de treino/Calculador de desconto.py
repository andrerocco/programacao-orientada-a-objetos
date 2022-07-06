valor = int(input("Digite o preço inicial: R$"))
desconto = int(input("Digite a % de desconto: R$"))

valor_final = valor * (1 - desconto / 100)
print("Valor final: R${}".format(valor_final))