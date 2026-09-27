
fruta = input("Entre com o nome da fruta:").upper()

frutas = {
    "PERA":"R$1,25",
    "GOIABA": "R$2,15",
    "ABACAXI": "R$3,20",
    "JACA": "R$5,80",
    "LARANJA": "R$0,65",
    "LIMÃO": "R$1,25",
    "MAÇÃ": "R$1,50",
    "BANANA": "R$2,75",
    "UVA": "R$1,90"
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor válido!")

#selecionar várias linhas para digitar a mesma coisa em todas elas: seleciona -> shift + alt + i -> home/end -> escreve o que quiser

#Com essas múltiplas seleções, se eu apertar "ctrl + shift + seta", eu seleciono a palavra inteira que está nessa direção da seta em relação ao cursor

#ctrl + shift + p -> abre a caixa lá em cima pra gente, por exemplo, passar tudo que está selecionado para maiúsculo digitando "upper", de "uppercase"