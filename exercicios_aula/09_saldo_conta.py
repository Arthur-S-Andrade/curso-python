saldo_total = 0

while True:
    saldo = input("Entre com o saldo:")

    if saldo == "":
        break

    saldo_total += float(saldo)

print("O saldo total é de R$:", saldo_total)