# %%

#Existem algumas bibliotecas do python que já possuem algumas funções definidas, fazendo com que a gente não precise criar algumas funções. Por exemplo, existe a biblioteca math, que vai apresentar vários métodos já criados para realizar operações matemáticas, como raiz quadrada, potenciação etc que não são nativas do python mas como ele é muito utilizado para data science e analytics, pessoas já criaram essas funcionalidades e colocaram nessa biblioteca

#Para importar essa biblioteca, fazemos da seguinte forma:

import math

# %%

#uma vez que já importamos a biblioteca, para utilizar os recursos dela nós chamamos a biblioteca e digitamos ponto, para que a gente possa visualizar os métodos disponíveis naquela biblioteca. Por exemplo quando falamos em potenciação:

math.pow(2, 4)


# %%

#eu não preciso necessariamente importar uma biblioteca inteira. Posso importar apenas algum ou alguns recurso(s) específico(s) que eu queira. Por exemplo, se eu quiser importar apenas a funcionalidade que retorna o valor de pi e a que retorna o valor de e, eu posso fazer da seguinte forma:

from math import pi, e

# %%

#a partir desse momento, se eu quiser o valor de pi, eu não preciso necessariamente utiliar math.pi para obter o valor de pi. Basta eu declarar o pi, que o valor de pi será retornado para mim:

pi



# %%

#da mesma forma, a partir desse momento, se eu quiser o valor, de e, basta declarar o e:

e

#Se eu tentar declarar "pow", por exemplo sem a biblioteca, eu não conseguiria pois eu não importei esse método separado. Então para utilizá-lo, eu preciso declarar "math.pow()"

# %%
#além disso, eu posso atribuir um alias à biblioteca que eu importo se eu quiser estabelecer um padrão de nome mais curto, por exemplo. Então se eu quiser utilizar o alias "mh" para a biblioteca "math" para não precisar escrever "math" toda hora, é só eu fazer da seguinte forma:

import math as mh


# %%

print(mh.sqrt(16))

# %%
