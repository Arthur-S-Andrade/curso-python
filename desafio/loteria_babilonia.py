#Construa um programa que realiza um sorteio de um número entre 1 e 15
#O usuário terá 3 chances de acertar o valor
#A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado
#Caso o usuário acerte, dê os parabéns


# ------------------------- MINHA SOLUÇÃO -----------------------

from random import randint

sorteio = randint(1, 15)
tentativas = 0
while True:

    try:
#o "try" aqui vai testar o input. Se ele não for um int, o except vai capturar esse erro pro programa não quebrar e o "continue" vai ignorar o resto do programa e voltar para o while la em cima
        chute = int(input("Entre com o seu palpite:"))
    except ValueError as err:
        print("Valor Inválido! Digite um número:")
        continue

    if chute < 1 or chute > 15:
        print("Valor Inválido! o valor deve ser entre 1 e 15")
        continue

    tentativas += 1

    if chute == sorteio:
        print("Parabéns! Você acertou! o número era", sorteio)
        break

    elif chute > sorteio:
        print("O número sorteado é menor que o seu palpite. Tente novamente!")

    else:
        print("O número sorteado é maior que o seu palpite. Tente novamente!")

    if tentativas == 3:
        print("Você alcançou o máximo de tentativas! O número sorteado era", sorteio)
        break

# ----------------------------------------------------------------