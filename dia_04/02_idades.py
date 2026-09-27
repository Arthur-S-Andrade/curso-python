# %%
idades = [17, 32, 56, 87]
#Em python, métodos são ações que um determinado objeto pode desempenhar. As listas têm alguns métodos assim como qualquer outro objeto em python. Para ver quais métodos um determinado objeto tem, basta escrever o nome do objeto seguido de . (sem espaço)

print(idades)

# %%

idades.append(32)

#.append é um método das listas que é capaz de adicionar um item na própria lista. Ou seja, diferente das strings, as listas são objetos MUTÁVEIS

print(idades)

# %%

idades = []

while True:
    idade = input("Entre com a idade: ")
    

    if idade == "":
        break

    idades.append(int(idade))

print(idades)
media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtd = len(idades)

#selecionar várias linhas para digitar a mesma coisa em todas elas: seleciona -> shift + alt + i -> home/end -> escreve o que quiser

#Com essas múltiplas seleções, se eu apertar "ctrl + shift + seta", eu seleciono a palavra inteira que está nessa direção da seta em relação ao cursor

#ctrl + shift + p -> abre a caixa lá em cima pra gente, por exemplo, passar tudo que está selecionado para maiúsculo digitando "upper", de "uppercase"

print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTD:", qtd)

# %%


