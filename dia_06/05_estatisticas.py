# %%

def soma(a:float, b:float, *args)->float:
    valores = [a+b] + list(args)
    return sum(valores)
# *args é um argumento coringa (não precisa ser args, pode ser qualquer nome) para utilizar quando nós não sabemos quantos argumentos serão utilizados. Pode ser 0 ou pode ser uma porrada. Utilizando ele nesse caso, nós conseguimos garantir que se eu quiser criar mais inputs de valores ali e incluí-los na chamada da função, eu posso adicionar normalmente e isso não vai quebrar meu código. Mesma coisa para a função media

def media(a: float, b:float, *args)-> float:
    return soma(a,b, *args)/(len(args)+2)
#posso reutilizar a função soma aqui. Essa é uma das vantagens de você determinar responsabilidades mais "atômicas" para as suas funções. É mais fácil de você conseguir reaproveitá-las dentro de outras funções no seu código

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
d = float(input("Entre com o valor de d: "))
e = float(input("Entre com o valor de e: "))

print("a soma de a e b é:", soma(a, b, c, d, e))
print("a média entre a e b é:", media(a,b, c, d, e))

# %%
