""" Implemente a classe MeuDicionario usando duas listas, uma para chave e
uma para valores. Deve ser possível inserir, remover e acessar elementos no dicionário
(use magic methods), além de verificar se um valor encontra-se no dicionário (em caso
positivo, retorna a chave correspondente, caso contrário retorna False). """

class MeuDicionario:
    def __init__(self):
        self.chaves = []
        self.valores = []

    def __setitem__(self, chave, valor):
        if chave in self.chaves:
            self.valores[self.chaves.index(chave)] = valor
        else:
            self.chaves.append(chave)
            self.valores.append(valor)

    def __getitem__(self, chave):
        if chave in self.chaves:
            return self.valores[self.chaves.index(chave)]
        else:
            return False

    def __delitem__(self, chave):
        if chave in self.chaves:
            self.valores.pop(self.chaves.index(chave))
            self.chaves.remove(chave)
        else:
            print("Chave não encontrada!")

    def __contains__(self, valor):
        if valor in self.valores:
            return self.chaves[self.valores.index(valor)]
        else:
            return False