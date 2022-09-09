total = 0
print("Adicione as notas")
for i in range(4):
    total += float(input(f"{i+1}. Nota: "))

print("Media = {}".format(total/4))