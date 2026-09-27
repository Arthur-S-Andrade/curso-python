
dados = {}
while True:
    frase = input("Entre com a frase (Se quiser parar, aperte ENTER):")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

for i, j in dados.items():
    print(i, "->", j, "vez(es)!")
#for i in dados:
#   print(i, "->", dados[i], "vez(es)!")