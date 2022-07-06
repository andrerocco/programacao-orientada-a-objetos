# 2482

quantidade_traducoes = int(input())
dicionario_traducoes = {}
for i in range(quantidade_traducoes):
    lingua = str(input())
    dicionario_traducoes[lingua] = str(input())

quantidade_criancas = int(input())
for i in range(quantidade_criancas):
    nome = str(input())
    lingua = str(input())
    
    print(nome)
    print("{}\n".format(dicionario_traducoes[lingua]))