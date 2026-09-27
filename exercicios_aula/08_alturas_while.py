count = 1
soma = 0
while count <= 4:
    altura = float(input("digite a altura em metros aqui:"))
    count += 1 #Dava pra definir o count como 4 e usar o while enquanto fosse > 0 e fazer o count -= 1 aqui. Seria uma lógica regressiva em vez de progressiva 
    soma += altura

print("A soma das alturas é:", soma, "m")