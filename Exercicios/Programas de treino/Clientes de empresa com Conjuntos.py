def imprimir_relacao():
    print("Clientes cadastrados na Empresa 01:\n{}".format(empresa1))
    print("Clientes cadastrados na Empresa 02:\n{}".format(empresa2))

def cadastrar_novos():
    print("\n------- Cadastrar novo cliente -------")
    while True:
        cadastro = str(input("Nome e número da empresa (separados por espaço): ")).split()
        nome = cadastro[0].capitalize()
        empresa = cadastro[1]
        
        if empresa == "1":
            empresa1.add(nome)
        elif empresa == "2":
            empresa2.add(nome)
        else:
            print("Empresa inválida")
        
        continuar = str(input("Continuar? [S/N] ")).lower()
        if continuar != "s":
            break
        
def clientes_ambas():
    print("\nClientes cadatrados em ambas empresas: {}".format(empresa1.intersection(empresa2)))

def estatisticas():
    print("\n------- Estatísticas -------")
    print("Clientes da Empresa 01: {}".format(len(empresa1)))
    print("Clientes da Empresa 02: {}".format(len(empresa2)))
    print("Clientes cadatrados em ambas empresas: {}".format(len(empresa1.intersection(empresa2))))
    print("Clientes apenas na Empresa 01: {}".format(len(empresa1.difference(empresa2))))
    print("Cadastros totais: {}".format(len(empresa1.union(empresa2))))

empresa1 = {"João", "Roberto"}
empresa2 = {"Roberto", "Maria", "Ítalo"}

while True:
    print("\n------- Selecione uma opção -------")
    print("a. Visualizar a relação de clientes cadastrados nas empresas.")
    print("b. Cadastrar novos clientes.")
    print("c. Visualizar clientes cadastrados em ambas empresas.")
    print("d. Estatísticas gerais.")
    
    entrada = str(input("\nDigite a letra da opção escolhida: ")).lower()
    
    if entrada == "a":
        imprimir_relacao()
    elif entrada == "b":
        cadastrar_novos()
    elif entrada == "c":
        clientes_ambas()
    elif entrada == "d":
        estatisticas()
    
    else:
        print("Entrada inválida. Selecione uma opção válida.")