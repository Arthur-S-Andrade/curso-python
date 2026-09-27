# %%

#Agora que já vimos como pegar arquivos txt já escritos e trazer para o python, vamos aprender como escrever novos arquivos a partir do python

#primeiro eu escrevo o que eu quiser que tenha no arquivo e atribuo a uma variável. Por exemplo, aqui vamos atribuir a uma variável chamada "txt":
txt = "Meu novo arquivo! Testando se os acentos estão disponíveis: çaáàsd"

#depois eu determino qual o nome do arquivo que eu quero criar:
nome_arquivo = "historia_02.txt"

#agora vamos utilizar a mesma função "open" com o "with", porém nos argumentos do "with" vamos adicionar o "mode" com o valor "w", de "write". Por padrão, esse argumento quando oculto assume valor "r", de "read":
with open(nome_arquivo, mode="w", encoding="UTF-8") as open_file:
    open_file.write(txt)

#Se eu quiser editar esse arquivo adicionando mais texto, em vez do "mode="w"",nós vamos utilizar "mode="a"". Dessa forma, o que a gente atribuir na variável txt lá em cima será adicionado após a string que já foi previamente escrita. Para não ficar tudo junto uma coisa na outra. Ao final de cada string que eu adicionar no arquivo eu adiciono um "\n", que vai ser uma quebra de linha, criando uma nova linha vazia pra próxima coisa que for adicionada

# %%
