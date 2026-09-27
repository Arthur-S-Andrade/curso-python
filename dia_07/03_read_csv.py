# %%

arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

#Aqui em vez de usar o método ".read()", que nos retorna todo o arquivo dentro de uma string, como estamos trabalhando com arquivos csv, nós usamos o método ".readlines()", que vai nos retornar cada linha da planilha (que chamamos de REGISTRO) como uma posição de uma lista "lines"

for l in lines:
    print(l)

#Aqui em cima, como nós temos cada registro em uma posição de uma lista, nós conseguimos utilizar o for para percorrer toda essa lista e printar cada registro separadamente por linha

# %%

#Para deixar a coisa mais interessante, nós podemos extrair desse arquivo csv os dados de forma organizada, criando um dicionário chamado "dados" onde as chaves serão "nome", "idade" e "profissao" e os valores serão cada um dos respectivos registros. 

dados = dict()

# Para isso nós vamos criar uma lista "chaves" e aplicar alguns métodos nela para preparar esses dados:

#primeiramente: Se pegarmos a primeira posição da lista e atribuir na lista chaves da seguinte forma "chaves = lines[0]", o retorno que teríamos seria "'nome;idade;profissao\n'"

#Para tirar o "\n" e fatiar os registros a partir dos separadores ";" mas tirando esses separadores da lista que vai ser gerada, nós vamos aplicar dois métodos na declaração chaves = lines[0]:

#O primeiro método é ".strip("\n")" e o segundo é ".split(";")"

chaves = lines[0].strip("\n").split(";")

#Depois disso, nós vamos pegar essa lista "chaves" e vamos percorrer com um laço "for" utilizando a variável temporária "c" para atribuir os valores dessa lista como chaves no meu dicionário "dados" e, ao mesmo tempo, criando listas vazias como valores para formar os pares chave-valor no meu dicionário "dados": 

for c in chaves:
    dados[c] = []

#agora vamos percorrer a lista lines a partir da segunda linha (a primeira linha é a das chaves)
for l in lines[1:]:

    #agora vamos pegar cada linha a partir da segunda e fatiar na lista "valores" a partir dos separadores ";" (retirando eles) e removendo os "\n" de todos os registros
    valores = l.strip("\n").split(";")

    #agora nós percorremos a variável temporária i (que é só um índice), começando em 0 considerando o número de valores da lista valores (que são 3). Ou seja, o índice i vai assumir os valores 0, 1 e 2 para cada um dos itens da lista valores
    for i in range(0, len(valores)):

        #agora nós vamos atribuir esses itens da lista "valores" justamente como valores no dicionário "dados" garantindo a ordem certa para formar os pares chave-valor da forma correta. Ou seja, quando "i" assumir valor 0, em "[chaves[i]]", nós estaremos nos referindo à chave "nome". A partir disso nós aplicamos o método ".append(valores[i])" nessa lista vazia que nós criamos dentro do dicionário como os valores de cada chave. Portanto, vai assumir o primeiro valor "Téo". Depois o "i" vai assumir valor 1, que é referente à chave "idade" e o valor a ser adicionado é 32. Depois o "i" vai assumir o valor 2, que é referente à chave "profissao" e o valor a ser adicionado vai ser "streamer". Depois dessa primeira iteração, o "laço-mãe" lá em cima ("for l in lines[1:]:") vai passar para o próximo registro e fazer esse mesmo passo a passo para adicionar os valores "Nah", "35" e "artesa" às respectivas chaves "nome", "idade" e "profissao". E assim sucessivamente
        dados[chaves[i]].append(valores[i])

dados

# %%

#com isso tudo feito, se eu quiser fazer a média de idade. Eu vou precisar buscar as idades dentro do dicionário, convertê-los para inteiros já que eles foram registrados como strings e aí aplicar a função para calcular a média

idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
print("A média de idades é", media)

# %%
