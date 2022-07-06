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