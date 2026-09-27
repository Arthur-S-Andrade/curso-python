#Construa um programa que realiza um sorteio de um número entre 1 e 15
#O usuário terá 3 chances de acertar o valor
#A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado
#Caso o usuário acerte, dê os parabéns

from random import randint

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número: "))

        except ValueError as err:
            print("Valor Inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! O número deve estar entre 1 e 15")


def check_numbers(usuario, sorteio):
    if sorteio == usuario:
       print("Parabéns! Você acertou! O número era", numero_sorteio)
       return True

    elif usuario > sorteio:
        print("Número muito alto! Tente um número menor!")
        return False

    else:
        print("Número muito baixo! Tente um número maior!")
        return False


numero_sorteio = randint(1, 15)

for i in range(3):
   
   numero_usuario = get_input()
   if check_numbers(sorteio = numero_sorteio, usuario = numero_usuario):
       break

else:
    print("Suas tentativas acabaram! O número era", numero_sorteio)
#Else do for: caso o for seja encerrado sem um break, ele executa o bloco de código desse else 