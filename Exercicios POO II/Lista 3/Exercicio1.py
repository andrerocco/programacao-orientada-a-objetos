""" Escreva uma função que conta a frequência de ocorrência de cada
palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a
chave é a vogal considerada. """

def leitor():
    texto = open("texto.txt", "r")
    texto = texto.read()
    texto = texto.lower()
    texto = texto.split()
    vogais = ["a", "e", "i", "o", "u"]
    dicionario = {}
    for i in vogais:
        dicionario[i] = 0
    for i in texto: # i = palavra
        for j in i: # j = letra
            if j in vogais: # Se a letra for uma vogal
                dicionario[j] += 1 # Adiciona 1 ao valor da vogal no dicionario
    
    print(dicionario)

if __name__ == "__main__":
    leitor()