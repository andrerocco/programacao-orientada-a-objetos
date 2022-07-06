# André Amaral Rocco

while True:
    entrada = (str(input())).split()

    andre = int(entrada[0])
    pedro = int(entrada[1])
    camila = int(entrada[2])
    manoel = int(entrada[3])
    lara = int(entrada[4])

    total = (andre*300) + (pedro*1500) + (camila*600) + (manoel*1000) + (lara*150) + 225

    print(total)
    
    print("Deseja continuar executando? [S/N]")
    continuar = str(input())
    if continuar == "N":
        break