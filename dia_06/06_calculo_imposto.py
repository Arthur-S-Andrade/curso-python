# da mesma forma que nós vimos o *args, existe também o **kwargs, que é parecido, mas em vez de se comportar como uma tupla ou lista como o *args, ele se comporta como um DICIONÁRIO. Ou seja, ele vai servir pra quando nós precisarmos contemplar a possibilidade de adicionar indefinidamente argumentos nomeados, do tipo chave-valor

# %%

def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

# %%

impostos_gerais = {
    "municipal":0.01,
    "estadual":0.005,
    "nacional":0.001
}

calc_imposto(100, 0.03, **impostos_gerais, internacional=0.00001)

#Utilizamos o ** aqui no dicionário impostos_gerais pelo mesmo motivo que utilizamos lá no **kwargs. Esses asteriscos significam que o dicionário está sendo "quebrado" e o que vai ser levado em consideração vão ser os pares chave-valor contidos nele

#Nesse exemplo, se eu quisesse adicionar os impostos "municipal", "estadual" e "nacional" nominalmente um por um nos argumentos da chamada da função, eu tbm poderia. Mas utilizando o dicionário "impostos_gerais", eu consigo chamar a função de forma mais simples
