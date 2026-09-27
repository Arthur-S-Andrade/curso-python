# %%

#Vamos imaginar que eu tenho 2 variáveis ("A" e "B") e que eu queira trocar os valores delas. Ou seja. Eu quero que A agora valha o que B valia e vice-versa:

A = 1
B = 5

print(A)
print(B)

# %%

#Poderia fazer dessa forma, logicamente:

C = A
A = B
B = C
print(A)
print(B)

# %%

#Porém, no Python, nós podemos fazer isso de forma simplificada:

A, B = B, A
print(A)
print(B)

# %%

#Se em vez de "A, B = B, A", nós tivéssemos feito "nova = A, B", nós veríamos que o que acontece é que esse "nova" é uma tupla, onde o primeiro item é o valor de A e o segundo é o valor de B

# O que o unpack ("A, B = B, A") faz é, justamente, que no meio do processo é como se ele criasse esse item novo que seria essa tupla, fazendo um unpack dela e reatribuindo os itens dessa tupla intermediária ao A e ao B, invertendo eles

# %%

#vamos imaginar um outro cenário. Se eu criar uma tupla "a, b" onde os valores são 1 e 2 e eu quiser adicionar dps um valor 3, eu teria que redeclarar essa tupla como "a, b, c = 1, 2, 3", e assim sucessivamente para cada valor que eu quiser add

#Para contemplar essas novas adições sem ter que ficar redeclarando adicionando novas variáveis, é só eu declarar "a, b, *resto", onde esse "*resto" vai ser uma lista com todos os outros valores que porventura possam ser adicionados

a, b, *resto = 1, 2, 3, 4, 5, 6, 7, 87, 78457, 3462, 345
print(a, b, resto)

# Isso é bom se eu quiser apenas os dois primeiros valores. 

#%%

# Se eu quiser os dois últimos, é só declarar "*resto, a, b"

*resto, a, b = 1, 2, 3, 4, 5, 6, 7, 87, 78457, 3462, 345
print(a, b, resto)

# %%

#Se eu quiser o primeiro e o último, é só declarar "a, *resto, b"

a, *resto, b = 1, 2, 3, 4, 5, 6, 7, 87, 78457, 3462, 345
print(a, b, resto)

# %%

# Isso é importante pq é exatamente o que a gente estava fazendo quando utilizamos o "*args" durante o curso. Então, por exemplo, se eu quiser criar uma função soma onde os itens que forem adicionados devem ser somados com os iniciais, eu posso utilizar exatamente esse conceito de unpacking com o "*args":

def soma(a, *args):
    total = a + sum(args)
    return total

soma(1, 2, 4, 3, 7, 2)

# %%

#O contrário também funciona. Se eu tiver uma função "soma_quatro(a,b,c,d)" em que eu vou somar essas 4 variáveis eu posso utilizar o unpacking para chamar essa função se eu tiver uma lista de 4 valores e quiser executar a soma deles. Pois se eu tentar aplicar essa função na lista, vai dar erro. Então eu utilizo o unpack para passar os valores da lista, e não a lista em si:

def soma_quatro(a,b,c,d):
    return a+b+c+d

values = [1, 2, 3, 4]
soma_quatro(*values)

# %%

#Da mesma forma para a função soma que nós definimos mais acima. Se eu tentar aplicar essa função à lista values, vai dar problema. Então eu chamo a função utilizando "*values" como argumento

soma(*values)

# %%
