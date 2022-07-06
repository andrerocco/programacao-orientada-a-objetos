# 1281

def preco_compra(tabela_preco, tabela_compra):
    preco_total = 0
    for fruta in tabela_compra:
        qnt = tabela_compra[fruta]
        preco_total += tabela_preco[fruta] * qnt
    return preco_total

quantidade_idas = int(input())

for i in range(quantidade_idas):
    quantidade_venda = int(input())
    venda_feira = {}
    for x in range(quantidade_venda):
        info = input().split()
        venda_feira[info[0]] = float(info[1])
    
    quantidade_compra = int(input())
    compra_feira = {}
    for x in range(quantidade_compra):
        info = input().split()
        compra_feira[info[0]] = int(info[1])
        
    print("R$ {:.2f}".format(preco_compra(venda_feira, compra_feira)))

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

# 1763

dicionario = {
    'brasil' : 'Feliz Natal!',
    'alemanha' : 'Frohliche Weihnachten!',
    'austria' : 'Frohe Weihnacht!',
    'coreia' : 'Chuk Sung Tan!',
    'espanha' : 'Feliz Navidad!',
    'grecia' : 'Kala Christougena!',
    'estados-unidos' : 'Merry Christmas!',
    'inglaterra' : 'Merry Christmas!',
    'australia' : 'Merry Christmas!',
    'portugal' : 'Feliz Natal!',
    'suecia' : 'God Jul!',
    'turquia' : 'Mutlu Noeller',
    'argentina' : 'Feliz Navidad!',
    'chile' : 'Feliz Navidad!',
    'mexico' : 'Feliz Navidad!',
    'antardida' : 'Merry Christmas!',
    'canada' : 'Merry Christmas!',
    'irlanda' : 'Nollaig Shona Dhuit!',
    'belgica' : 'Zalig Kerstfeest!',
    'italia' : 'Buon Natale!',
    'libia' : 'Buon Natale!',
    'siria' : 'Milad Mubarak!',
    'marrocos' : 'Milad Mubarak!',
    'japao'  : 'Merii Kurisumasu!',
    }
 
while True:
    try:
        pais = input()
        if pais in dicionario.keys():
            print(dicionario[pais])
        else:
            print('--- NOT FOUND ---')
 
    except EOFError:
        break

# 1953

while True:
    try:
        numero_alunos = int(input())
        epr = 0
        ehd = 0
        intruso = 0
        
        for i in range(numero_alunos):
            matricula, curso = input().split()
            if curso == 'EPR':
                epr += 1
            elif curso == 'EHD':
                ehd += 1
            else:
                intruso += 1
        
        print("EPR: {}".format(epr))
        print("EHD: {}".format(ehd))
        print("INTRUSOS: {}".format(intruso))
        
    except EOFError:
        break

# 1430

notas = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}
 
while True:
    entrada = str(input())
    if entrada == '*':
        break
    
    entrada = entrada.split('/')
    
    corretos = 0
    for compasso in entrada:
        soma = 0
        for nota in range(len(compasso)):
            soma += notas[compasso[nota]]
        if soma == 1:
            corretos += 1
    
    print(corretos)

# 1261

numero_palavras, num_desc_cargos = [int(x) for x in str(input()).split()]
 
dicionario = {}
 
for i in range(numero_palavras):
    palavra, dinheiro = input().split()
    dinheiro = int(dinheiro)
    
    dicionario[palavra] = dinheiro
 
for i in range(num_desc_cargos):
    descricao = ''
    while True:
        frase = input()
        if frase == '.':
            break
        descricao += frase + ' '
    
    descricao = descricao.split()
    
    salario = 0
    
    for j in descricao:
        if j in dicionario:
            salario += dicionario[j]
    print(salario)
