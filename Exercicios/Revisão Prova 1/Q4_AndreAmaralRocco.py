# Andre Amaral Rocco

def calcular(t, ultimo_t):
    if t-ultimo_t <= 10 and ultimo_t != 0:
        return t - ultimo_t
    else:
        return 10

n = int(input())
tempo_total = 0
ultimo_tempo = 0

for i in range(n):
    tempo = int(input())
    tempo_total += calcular(tempo, ultimo_tempo)
    ultimo_tempo = tempo

print(tempo_total)