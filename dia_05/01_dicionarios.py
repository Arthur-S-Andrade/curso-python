# %%

lista = [2, 132, "Teo", ["ds", "de", "da"], True]

lista[2]

# %%

# Dicionários: São conjuntos de pares chave/valor

# sintaxe: nome do dicionário = {"chave": "valor", "chave": "valor"}

# As chaves nos dicionários podem ser dos tipos STRING, INTEIRO ou FLOAT (muito raro usar float. Evitar usar float)

# Os valores nos dicionários podem ser de qualquer tipo

dados_teo = {
    "sobrenome": "Calvo", 
    "nome": "Téo", 
    "filhos": True, 
    "formação": ["estatística", "bigdata datascience"], 
    "cargos":[
        {"nome": "ds jr.", "empresa":"tapps"}, 
        {"nome": "ds pl.", "empresa": "sas"}, 
        {"nome": "ds sr", "empresa": "boticario"}, 
        {"nome": "ds espec", "empresa": "via varejo"},
    ]
}

print(dados_teo)

# Para acessar um valor dentro de um dicionário, nós escrevemos o nome seguido de colchetes e, dentro deles, escrevemos a chave referente ao valor que nós queremos exibir. Por exemplo:

print(dados_teo["formação"][-1])
print(dados_teo["cargos"][-1]["empresa"])

#Os dicionários são muito utilizados em chamadas de API. E essa forma de acessar dados em dicionários (exemplos em cima desse comentário) são muito utilizados quando utilizamos o Pandas para manipulação e análise de dados

# %%

dados_teo["estado civil"] = "casado"

# %%

print(dados_teo)
# %%

#Método para visualizar quais são as chaves do dicionários: .keys()

print("Chaves:", dados_teo.keys())

#Método para visualizar quais são os valores do dicionários: .values()

print("Valores:", dados_teo.values())

#Método para visualizar quais são os pares chave-valor do dicionários: .items()

#Nesse método ele vai retrnar uma lista onde os itens são tuplas de dois posições, onde os primeiros itens serão as chaves e os segundos serão os valores associados a cada chave respectivamente

print("Itens:", dados_teo.items())

# %%

#Esse conteúdo é muito interessante, por exemplo, para juntar com o conteúdo de laços for (laços que percorrem listas e também percorrem dicionários). Eu posso, por exemplo criar um laço for para percorrer um dicionário e retornar as chaves e os valores:

for i in dados_teo:
    print(i, "->", dados_teo[i])

#Se a gente printasse apenas o i, o que teríamos de retorno seriam apenas as chaves. Quando fazemos dessa forma como está em cima desse comentário, utilizamos a variável temporária i para percorrer o dicionário retornando as chaves e, também, utilizamos esse i para acessar os valores referentes a cada uma das chaves que ela assumir o valor a cada iteração do laço

# %%

#Além dessa forma, também podemos utilizar o método .items() para acessar os valores de dicionários da seguinte forma:

for [chave, valor] in dados_teo.items():
    print(chave, "->", valor)

# %%

#Repetindo o dicionário aqui pq fechei o modo interativo sem querer!

dados_teo = {
    "sobrenome": "Calvo", 
    "nome": "Téo", 
    "filhos": True, 
    "formação": ["estatística", "bigdata datascience"], 
    "cargos":[
        {"nome": "ds jr.", "empresa":"tapps"}, 
        {"nome": "ds pl.", "empresa": "sas"}, 
        {"nome": "ds sr", "empresa": "boticario"}, 
        {"nome": "ds espec", "empresa": "via varejo"},
    ]
}

print(dados_teo)

# %%

dados_teo["estado civil"] = "casado"


# %%

print(dados_teo)


# %%

for i in dados_teo:
    print(i, "->", dados_teo[i])

# %%

for chave, valor in dados_teo.items():
    print(chave, "->", valor)

    
# %%
