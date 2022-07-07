from petshopCadastro import Cachorro
from petshopVIP import VIP

def imprimir_nome_caes_cadastrados():
    string_nomes = ''
    for i in range(len(caes_cadastrados)):
        if i == len(caes_cadastrados)-1:
            nome = caes_cadastrados[i].getNomeAnimal()
            string_nomes += nome
        else:
            nome = caes_cadastrados[i].getNomeAnimal() + ", "
            string_nomes += nome
    
    print(f"\nCães cadastrados: {string_nomes}")

def imprimir_informacoes(instancia):
    print("Nome do dono: {}".format(instancia.nome_dono))
    print("Nome do animal: {}".format(instancia.nome_animal))
    print("Raça: {}".format(instancia.raca))
    print("Peso: {} kg".format(instancia.peso))
    print("Idade: {} anos".format(instancia.idade))
    print("Cor do pelo: {}".format(instancia.cor_pelo))
    
    if isinstance(instancia, VIP):
        print("\nCadrastro - VIP")
        print("Periodicidade de banho: {} dias".format(instancia.periocidade_banho))
        print("Restrição alimentar: {}".format(instancia.resticao_alimentar))
    else:
        print("Cadrastro - Regular")

def mais_velho():
    maior_idade = None
    cao_mais_velho = None
    for cao in caes_cadastrados:
        if maior_idade == None:
            maior_idade = cao.getIdade()
            cao_mais_velho = cao
        elif cao.getIdade() > maior_idade:
            maior_idade = cao.getIdade()
            cao_mais_velho = cao

    return cao_mais_velho


# nome_dono, nome_animal, raca, peso, idade, cor_pelo, banho, restricao
armando = Cachorro("Armando Costa", "Robert", "Pastor Suiço", 30, 7, "Branco")
jonatan = Cachorro("Jonatan da Silva", "Totó", "Pitbul", 45, 3, "Preto e branco")
bruna = VIP("Bruna Morais", "Mel", "Shitzu", 8, 5, "Dourado", 3, True)

caes_cadastrados = []
caes_cadastrados.append(armando)
caes_cadastrados.append(jonatan)
caes_cadastrados.append(bruna)

while True:
    print("\n1. Cadastrar novo cão no sistema")
    print("2. Visualizar informações de um cão cadastrado")
    print("3. Verificar restrição alimentar de cão cadastrado")
    print("4. Vizualizar cachorro mais velho cadastrado")
    print("5. Fechar sistema")
    entrada = int(input("Selecione uma opção: "))

    # Escolha da opção 1 (cadastrar novo cão)
    if entrada == 1:
        print("\nTipo de cadastro: \n1. Regular \n2. VIP")
        tipo = int(input("Selecione uma opção: "))
        if tipo == 1:
            print("\n> Nome do dono, nome do animal, raça, peso, idade, cor do pelo")
            informacoes = str(input("Insira as informações acima em ordem e separadas por espaço:\n")).split()
            informacoes[3] = int(informacoes[3]) # Converte o peso de str para int
            informacoes[4] = int(informacoes[4]) # Converte a idade de str para int
            cao = Cachorro(*informacoes)
            caes_cadastrados.append(cao)
        elif tipo == 2:
            print("\n> Nome do dono, nome do animal, raça, peso, idade, cor do pelo, periodicidade de banho, restrição alimentar [S ou N]")
            informacoes = str(input("Insira as informações acima em ordem e separadas por espaço:\n")).split()
            informacoes[3] = int(informacoes[3]) # Converte o peso de str para int
            informacoes[4] = int(informacoes[4]) # Converte a idade de str para int
            informacoes[6] = int(informacoes[6]) # Converte a periodicidade do banho de str para int
            if informacoes[7].upper() == "S":
                informacoes[7] = True
            else:
                informacoes[7] = False
            cao = Cachorro(*informacoes)
            caes_cadastrados.append(cao)
    
    # Escolha da opção 2 (visualizar informação de um cão)
    elif entrada == 2:
        imprimir_nome_caes_cadastrados()
        cao_escolhido = input("Insira o nome do cão o qual quer ver as informações: ").lower()
        
        for cao in caes_cadastrados:
            if cao.getNomeAnimal().lower() == cao_escolhido:
                imprimir_informacoes(cao)
                break
        else:
            print("Nome inválido")

    # Escolha da opção 3 (verificar restrição alimentar de cão cadastrado)
    elif entrada == 3:
        imprimir_nome_caes_cadastrados()
        cao_escolhido = input("Insira o nome do cão o qual quer ver as informações: ").lower()
        
        for cao in caes_cadastrados:
            if cao.getNomeAnimal().lower() == cao_escolhido:
                if isinstance(cao, VIP):
                    if cao.getRestricaoAlimentar():
                        print("O cão tem restrições alimentares.")
                    else: 
                        print("O cão não tem restrições alimentares.")
                else:
                    print("O cão não é VIP")
                break
        else:
            print("Nome inválido")

    # Escolha da opção 4
    elif entrada == 4:
        print(f"Cão mais velho cadastrado: {mais_velho().getNomeAnimal()}, tem {mais_velho().getIdade()} anos")

    # Escolha da opção 5
    elif entrada == 5:
        break
