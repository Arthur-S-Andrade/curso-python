# Falamos de dicionários e quando abordamos o método .items(), vimos que ele gera tuplas, que são uma outra estrutura de dados. Vamos entender agora o que são as tuplas

# %%

dados_teo = [32, 1, "Casado", "dev golang"]
dados_teo

# %%

dados_teo.append("3241.43")
dados_teo

# %%

#Tuplas são listas imutáveis! E elas podem ser declaradas com os itens entre parênteses ou sem nada:

tupla_teo = (32, 1, 'Casado', 'dev golang')
#tupla_teo = 32, 1, 'Casado', 'dev golang'

print(type(tupla_teo))
print(tupla_teo)

#Se eu tiver um objeto dentro da tupla que é mutável (como uma lista, por exemplo), eu posso alterar o estado desse objeto (adicionando mais itens por exemplo) mas não posso mexer nele enquanto objeto da tupla (não posso excluir nem mexer de lugar, por exemplo)

# %%


