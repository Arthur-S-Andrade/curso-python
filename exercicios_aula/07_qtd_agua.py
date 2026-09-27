escolha = input("""Bem vindo à minha barraca de água. Digite o número referente à sua opção: 
(1) Se quiser água natural - R$ 1.50
(2) Se quiser água com gás - R$ 2.50
""")

valor_item = 0
if escolha == "1":
    valor_item = 1.50
elif escolha == "2":
    valor_item = 2.50


if valor_item == 0:
    print("Valor incorreto!")

else:
    qtd = int(input("Digite quantas garrafas de água você vai querer:"))

    valor_final = valor_item*qtd

    print("Ok! O valor final fica: R$", valor_final)
