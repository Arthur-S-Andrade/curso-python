# %%

#No python, nós podemos importar arquivos txt. E isso é muito importante e pode ser muito útil para nós. Para fazer isso, nós vamos utilizar um passo a passo:

#Definir o nome do arquivo (aqui utilizamos só o nome pois ele está no mesmo diretório do arquivo python. Senão precisaríamos utilizar o path inteiro)

nome_arquivo = "historia.txt"

#Utilizar o "with" com a função "open()" e atribuir à variável conteúdo o método ".read()" para que a gente possa obter o arquivo, abrir em modo de leitura, ler os dados e fechar o arquivo de forma automática

with open(nome_arquivo, encoding="UTF-8") as open_file:
    conteudo = open_file.read()
print(conteudo)

#na chamada da função open eu especifiquei o "encoding" como "UTF-8" pois no encoding padrão "cp1252" não estava reconhecendo alguns caracteres como "ç" e acentos

# %%

#Forma alternativa e menos usual de fazer isso (pq pode dar ruim e esquecer de fechar o arquivo e ter risco de corromper. Com o "with" não tem esse risco)

#Utilizar a função open para abrir o arquivo em formato de leitura

#open_file = open(nome_arquivo)

#Agora que nós já obtivemos o arquivo, para podermos acessar o conteúdo (ler os dados) do arquivo vamos utilizar a função read():

#conteudo = open_file.read()
#print(conteudo)

#Depois de lermos os dados do arquivo, é importante que a gente feche o arquivo para garantir que ele não corrompa:

#open_file.close()
