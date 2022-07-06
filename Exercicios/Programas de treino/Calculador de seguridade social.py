print("Cálculo do valor de seguridade social")
salario = float(input("Digite o salário: "))

if (salario <= 720.00):
    seguridade = salario * 0.0765
elif (salario <= 1200.00):
    seguridade = salario * 0.09
elif (salario <= 2400.00):
    seguridade = salario * 0.11
else:
    seguridade = 2400 * 0.11

print(f"A seguridade social para um salário de R${salario} é de R${seguridade}")