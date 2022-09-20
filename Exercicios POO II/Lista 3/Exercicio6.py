""" Criar 10 frozensets com 30 números aleatórios cada, e construir um
dicionário que contenha a soma de cada um deles """

import random

dicionario = {}

for i in range(10):
    frozenset = frozenset(random.sample(range(100), 30))
    dicionario[frozenset] = sum(frozenset)