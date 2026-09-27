# %%

# O laço for vai percorrer os elementos de um objeto!
nome = "Teodoro Calvo"

for letra in nome: #letra é uma variável temporária existente só dentro do laço que vai nos permitir percorrer os elementos do objeto em questão (no caso, a variável nome)
    print(letra)

# %%

numero = 2
max_numero = 100

for i in range(1, max_numero+1): #coloca +1 pq esse número do intervalo à direita é aberto. então se quero que vá até 100, preciso colocar 101
    print(numero, "x", i, "=", numero * i)
# %%

for i in range(4, 101):
    if i % 4 == 0:
        print(i)
# %%
