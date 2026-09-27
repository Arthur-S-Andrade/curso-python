# %%

lista = [1, 2 ,3, 3, 2, 1, 1, 1, 1, 1, 5, 6, 7, 7, 6, 5]

numero = input("Entre com um número: ")
numero = int(numero)

qtd = 0
for i in lista:
    if numero == i:
        qtd += 1

print("O número", numero, "aparece", qtd, "vezes na lista!")


# %%
