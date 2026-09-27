#API é, basicamente, uma forma de estabelecer a comunicação entre sistemas. Vamos agora entender como consumir dados de uma API utilizando o exemplo de uma url que verifica CEPS: "https://viacep.com.br/ws/19060100/json/"

#Primeiramente, para conseguir consumir os dados de uma API nós vamos precisar importar a biblioteca "requests"
# %%
import requests #p/ realizar requisições na web
import json #p/ tratar listas / dicionarios para arquivos json
from tqdm import tqdm #exibe uma barra de progresso e a velocidade no terminal

import pandas as pd #dando um "gostinho" do que o pandas pode fazer pra nos ajudar com os dados

# %%
ceps = [
    "01519000", 
    "13329120", 
    "21870370", 
    "14400760", 
    "21645522", 
    "13600110", 
    "21051090", 
    "09656000", 
    "53420160", 
    "01311902", 
    "13476863", 
    "19060100", 
    "58038200"
]

url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
# checa o status da resposta. Se for "<Response [200]", significa que a resposta foi OK! A requisição foi aceita
        dados.append(resposta.json())
        #Para acessar os dados do conteúdo que está nessa url, nós usamos o método "resposta.json" pois nós já sabemos que p que essa API devolve está no formato de json, de dicionário. E isso nós colocamos dentro da lista vazia "dados":

dados

#A API pode devolver uma lista de dicionários também em vez de um dicionário apenas por exemplo. O que ela vai fazer é pegar o JSON e converter pela estrutura que ele "conhece" no python. NORMALMENTE, é um dicionário mesmo

# %%

#mostrando algumas utilidades incríveis do pandas para lidar com dados!

dataset = pd.DataFrame(dados) #pega os dados e coloca num dataframe

dataset.to_csv("ceps.csv", sep=";") #gera um csv de nome "ceps.csv" utilizando ";" como separadores

# %%

#Com a lista completa com os ceps coletados, nós vamos gerar um arquivo e salvar ele

with open("ceps.json", "w", encoding="UTF-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

    #o argumento "ensure_ascii=False" é pra que ele  ignore a tabela ascii como padrão de encoding para que assim a gente possa utilizar o encoding utf-8
