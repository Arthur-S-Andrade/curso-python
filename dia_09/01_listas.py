# %%

#vamos criar uma lista em que os elementos são os números de 1 a 100 como a gente aprendeu até agora:

x = []
for i in range (1, 101):
    x.append(i)

x

# %%

#agora vamos mostrar uma nova forma de fazer exatamente a mesma coisa porém utilizando apenas uma linha. Essa forma se chama "List Comprehension", e basicamente é uma forma simplificada para criar uma lista baseada num range iterável

y = [i for i in range(1, 101)]
y

# %%

# Podemos utilizar o list comprehension de diversas formas. Por exemplo, até mesmo utilizando uma função pra definir se o número é par (retorna booleano):

def par(x):
    return x % 2 == 0

z = [par(i) for i in range(1,101)]
z

# %%

# também poderia utilizar essa mesma função como filtro para mostrar apenas os números pares de 1 até 100:

w = [i for i in range(1,101) if par(i)]
w

# %%

# analogamente, também poderia utilizar essa mesma função como filtro para mostrar apenas os números ímpares de 1 até 100:

n = [i for i in range(1,101) if not par(i)]
n

# %%
