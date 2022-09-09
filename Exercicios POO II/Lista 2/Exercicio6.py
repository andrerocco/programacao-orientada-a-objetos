lista_medias = []
maior_que_7 = 0
for i in range(10):
    notas = [float(x) for x in input(f"{i+1}. Digite 4 notas separados por espaço: ").split()]
    media = sum(notas)/4

    if media >= 7:
        maior_que_7 += 1
    
    lista_medias.append(media)

print(f"{maior_que_7} alunos com nota maior igual a 7.0")

