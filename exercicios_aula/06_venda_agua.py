escolha = input("""Bem vindo à minha barraca de água. Digite o número referente à sua opção: 
(1) Se quiser água natural
(2) Se quiser água com gás
""")

conta = 0
if escolha == "1":
    conta = 1.50
elif escolha == "2":
    conta = 2.50

if conta == 0:
    print("Valor inválido!")
else:
    print("Sua conta é: R$:", conta)
