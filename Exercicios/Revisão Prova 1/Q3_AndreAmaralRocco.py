# Andre Amaral Rocco

def conferir_status_elevador(valor):
    if contador>0:
        print("S")
    else:
        print("N")

dados = (str(input())).split()
n = int(dados[0])
c = int(dados[1])

total = 0
contador = 0
for i in range(0, n):
    info = (str(input())).split()
    s = int(info[0])
    e = int(info[1])
    
    total += (e - s)
    if total > c:
        contador += 1
conferir_status_elevador(contador)