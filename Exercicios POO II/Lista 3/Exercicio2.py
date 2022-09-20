""" Escreva uma função que apaga do dicionário anterior, todas as palavras
que sejam ‘stopwords’. Ver https://gist.github.com/alopes/5358189 """

def apagar_stopwords(dicionario, stopwords):
    for i in dicionario:
        if i in stopwords:
            del dicionario[i]
    
    return dicionario