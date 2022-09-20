""" Escreva um programa para armazenar uma agenda de telefones usando
um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o
nome completo da pessoa. Seu programa deve ter as seguintes funções:
incluir_novo_nome – essa função acrescenta um novo nome na agenda, com
um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
incluir_telefone – essa função acrescenta um telefone em um nome existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja
incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo
nome.
excluir_telefone – essa função exclui um telefone de uma pessoa que
já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da
agenda.
excluir_nome – essa função exclui uma pessoa da agenda.
consultar_telefone – essa função retorna os telefones de uma pessoa
na agenda. """

agenda_telefonica = {}

def incluir_novo_nome(nome, telefones):
    for telefone in telefones:
        if nome in agenda_telefonica:
            agenda_telefonica[nome].append(telefone)
        else:
            agenda_telefonica[nome] = [telefone]

def incluir_telefone(nome, telefone):
    if nome in agenda_telefonica:
        agenda_telefonica[nome].append(telefone)
    else:
        print("Nome não encontrado na agenda!")
        resposta = input("Deseja incluí-lo? (S/N): ")
        if resposta == "S":
            incluir_novo_nome(nome, [telefone])

def excluir_nome(nome):
    if nome in agenda_telefonica:
        del agenda_telefonica[nome]
    else:
        print("Nome não encontrado na agenda!")

def excluir_telefone(nome, telefone):
    if nome in agenda_telefonica:
        if telefone in agenda_telefonica[nome]:
            agenda_telefonica[nome].remove(telefone)
            if len(agenda_telefonica[nome]) == 0:
                excluir_nome(nome)
        else:
            print("Telefone não encontrado na agenda!")
    else:
        print("Nome não encontrado na agenda!")

def consultar_telefone(nome):
    if nome in agenda_telefonica:
        print("Telefones de {}:".format(nome))
        for telefone in agenda_telefonica[nome]:
            print(telefone)
    else:
        print("Nome não encontrado na agenda!")