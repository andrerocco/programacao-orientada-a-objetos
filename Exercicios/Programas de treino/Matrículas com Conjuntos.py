def matricular_novo():
    nome = str(input("Nome: ")).capitalize()
    modalidade = str(input("Modalidade: ")).lower()
        
    if modalidade not in lista_modalidades:
        while True:
            print("Modalidade inválida. Digite uma modalidade válida (futebol, basquete, natação, volei):")
            modalidade = str(input("Modalidade: ")).lower
            if modalidade in lista_modalidades:
                break
    
    if modalidade == "futebol":
        futebol.add(nome)
    elif modalidade == "basquete":
        basquete.add(nome)
    elif modalidade == "natação":
        natacao.add(nome)
    elif modalidade == "volei":
        volei.add(nome)
    
    print("{} matriculado em {}".format(nome, modalidade))


futebol = {"Jonas", "Alberto", "Arnaldo"}
basquete = {"Maria", "Romerio", "Jonas", "Leandro"}
natacao = {"Jonas", "Leandro", "Romário", "Andreas"}
volei = {"Leandro", "Maria", "Mario", "Jonas", "Arthur"}
lista_modalidades = ["futebol", "basquete", "natação", "volei"]
multiplas = set()

while True:
    print("\nAlunos matriculados")
    print("Futebol: {}".format(futebol))
    print("Basquete: {}".format(basquete))
    print("Natação: {}".format(natacao))
    print("Volei: {}".format(volei))
    
    # Adicionar novos alunos matriculados
    while True:
        matricular = str(input("\nDeseja matricular um novo aluno [S/N]? ")).lower()
        if matricular == "n":
            break
        matricular_novo()
    
    # Enviar todos os alunos que estão em mais de uma modalidade para o conjunto multiplos
    for x in futebol.intersection(basquete):
        multiplas.add(x)
    for x in futebol.intersection(natacao):
        multiplas.add(x)
    for x in futebol.intersection(volei):
        multiplas.add(x)
    for x in basquete.intersection(natacao):
        multiplas.add(x)
    for x in basquete.intersection(volei):
        multiplas.add(x)
    for x in natacao.intersection(volei):
        multiplas.add(x)
    print("\nAlunos matriculados em mais de uma modalidade: {}".format(multiplas))
    
    # Mostra as estatísticas de matrícula
    print("\nEstatísticas")
    print("> {} alunos matriculados em futebol".format(len(futebol)))
    print("> {} alunos matriculados em basquete".format(len(basquete)))
    print("> {} alunos matriculados em natação".format(len(natacao)))
    print("> {} alunos matriculados em volei".format(len(volei)))
    total_matriculados = ((futebol.union(basquete)).union(natacao)).union(volei)
    print("Total de alunos do Centro de Treinamento: {}".format(len(total_matriculados)))
    
    
    continuar = str(input("Continuar [S/N]?")).lower()
    if continuar != "s":
        break
    
    
            
        