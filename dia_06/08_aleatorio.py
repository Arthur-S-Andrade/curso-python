# %%

#a biblioteca random é uma biblioteca famosa para nos ajudar a gerar números aleatórios e fazer escolhas aleatórias entre uma série de objetos

import random

# %%

#o Método randint() por exemplo gera um número aleatório dentro de um range específico que nós estabelecemos nos argumentos da função, por exemplo:

random.randint(1,10)

# %%

#na biblioteca random também temos o método choice(), que vai fazer escolhas aleatórias entre objetos de uma sequência não vazia:

x = ["Téo", "Maria", "José", "Ana", "João"]

random.choice(x)
