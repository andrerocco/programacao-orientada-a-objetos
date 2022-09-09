vetor = [int(x) for x in input("Digite 5 inteiros separados por espaço: ").split()]

multiplicacao = 1
for numero in vetor:
    multiplicacao *= numero

print(f'Soma: {sum(vetor)}')
print(f'Multiplicação: {multiplicacao}')
print('Numeros:', ", ".join([str(x) for x in vetor]))