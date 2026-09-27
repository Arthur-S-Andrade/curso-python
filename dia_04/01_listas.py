# %%

#listas são conjuntos de elementos

# a sintaxe para definir uma lista é a seguinte: 
# lista = [elemento1, elemento 2, ...]

idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)

# %%

#Listas podem ter dados de diferentes tipos dentro delas:

teo = ["Teo", "Calvo", 32, True, " Casado", 2342.98]
print(teo)

# %%

#Quando se quer saber o tipo de um elemento, de uma variável, nós podemos fazer isso:

type(teo)

# %%

#elementos nas listas tem seus respectivos índices. Que começam em 0. Ou seja, o primeiro elemento está no índice 0, o segundo no índice 1, e assim por diante. Para acessar um elemento específico, utilizamos seu índice:

print(teo[3])
# %%

idades = [28, 42, 43, 35, 39, 28, 38, 42, 34]

print("soma idades:", sum(idades))

print("qtd idades:", len(idades))

print("média idades:", sum(idades)/ len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

# %%

teo = ["Teo Calvo", 32, True, " Casado",
       ["estagiario", "ds jr", "ds pl", "ds sr", "head"],
       [1500, 4000, 4550, 6500, 10000] 
       ["Ana", "Maria", "Claudia"]]

print("Tamanho da lista Teo:", len(teo))

print(teo[6][0])
exs = teo[6]
primeira_ex = exs[0]
print(primeira_ex)
# %%

tamanho = len(teo)
pos = tamanho - 1

exs = teo[pos]

teo[pos][len(exs) - 1]

# %%

teo[-1][-2]

# %%

teo
# %%
# Fatiamento -> pega um conjunto de elementos da lista. a notação é a seguinte:

teo[0:4]

# Nesse caso, vamos pegar os 4 primeiros elementos da lista

# Quando eu faço o fatiamento a partir do início, não preciso colocar o 0, posso ocultar o início e colocar apenas "[:4]"


# %%
teo = ["Teo Calvo", 
       32, 
       True, 
       " Casado",
       ["estagiario", "ds jr", "ds pl", "ds sr", "head"],
       [1500, 4000, 4550, 6500, 10000], 
       ["Ana", "Maria", "Claudia"]]

cargos = teo[4]
print(cargos[-2:])

# Quando eu faço o fatiamento até o final, não preciso colocar até a posição -1 ou até o último índice. Eu posso ocultar o fim da lista e colocar apenas "[-2:]"

# %%

salarios = teo[5]
salarios[::-1]

# Isso funciona pq a sintaxe completa do fatiamento é "teo[ start : stop : step ]" .

# O step é como eu quero navegar nessa lista. O padrão é de 1 em 1. Mas se eu quiser ir de 2 em 2, é só colocar o 2 ali. E, como vimos, se quiser ir de trás pra frente pegando todos, é só colocar o -1


# %%
