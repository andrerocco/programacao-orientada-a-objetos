print('Digite 20 inteiros')

numeros = []
par = []
impar = []
for i in range(20):
    num = int(input(f"{i+1}. Digite um inteiro: "))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("Numeros: ", end = "") 
print(*numeros, sep = ", ") 
print("Pares: ", end = "")
print(*par, sep = ", ") 
print("Impares: ", end = "")
print(*impar, sep = ", ") 