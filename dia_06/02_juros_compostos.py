# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
#Os tipos de dados (type hints) que estão explicitados ali não são obrigatórios mas são recomendáveis de serem colocados para tornar o código mais explícito para o usuário. Ali no final que tem a seta apontando para o float se refere ao return, que quando colocamos os tipos das outras variáveis o python já tinha inferido. Porém se na taxa o usuário colocar um int, o resultado do cálculo vai ser um int. Os type hints não forçam o usuário a utilizar o mesmo tipo de aquele tipo de dado, mas são dicas de qual tipo é o esperado para cada variável. Se tentar usar outro, vai dar erro na execução do código, não na escrita

#Para documentar a função, basta aqui no bloco de código referente a ela abrirmos 3 aspas simples ou duplas e escrevermos a docstring para documentar o que essa função realiza
    """juros_compostos é uma função que calcula o retorno financeiro de um investimento em função do aporte, da taxa de juros e do tempo de aplicação.
    - aporte: é um número inteiro que representa a quantidade de dinheiro investida
    - taxa: é um número float entre 0 e 1 que representa a taxa de juros no momento da aplicação
    - anos: é um número inteiro >=1 que representa o tempo (em anos) que o dinheiro ficará investido"""
    return aporte * (1 + taxa) ** anos

# %%

juros_compostos(aporte = 1000, taxa = 0.13, anos = 4)

# na hora de chamar a função, se quiser chamar sem definir os nomes das variáveis, é importante manter a ordem:
# juros_compostos(1000, 0.13, 4)
# Porém a recomendação é que se defina os nomes das variáveis e que se mantenha a ordem também (se definir os nomes das variáveis, não precisa da ordem, mas é recomendado)

# %%


