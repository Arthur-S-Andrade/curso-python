# Funções que nós já utilizamos desde o dia 1: print(), input(), sum(), len()... Essas são funções que já foram implementadas por alguém. Alguém criou e "disse" ao python o que elas fazem

#Vamos agora entender como nós podemos criar uma nova função "f(x)" no python. Para isso, vamos precisar utilizar o "def"

# %%

def f(x):
    resultado = 1 + x
    #posso colocar direto 1 + x nesse caso sem a variável resultado por ser mt simples. Mas pra funções mais complexas pode ser importante utilizar as variáveis dentro da função
    return resultado

# %%

f(10)

# %%
