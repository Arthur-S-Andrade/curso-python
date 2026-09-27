# %%

def par_impar(n:int):
    """par_impar é uma função que diz se o número digitado pelo usuário é par ou ímpar.
    - n: número inteiro digitado pelo usuário"""

    if n % 2 == 0:
        print(n, "é par!")
    else:
        print(n, "é ímpar!")

    #Se eu fosse usar esse resultado em algum outro momento do código, em vez de usar o print na função, poderia colocar "return é par" e "return é impar". E aí lá fora dps do input declarar uma variável resultado que vai receber esse return tipo "resultado = par_impar(n)", e aí o print do final seria "print("o valor", n, "é", resultado)"

n = input("Entre com um número: ")
n = int(n)

par_impar(n)

# O ideal é que as funções tenham uma e somente uma funcionalidade de fato. Se essa função foi definida para dizer se um número é par ou ímpar, é só isso que ela vai fazer. Então o ideal é realmente que o input esteja fora da função. Se uma função começa a fazer muita coisa, o ideal seria dividir em várias funções
