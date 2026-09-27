# %%

idade = int(input("Olá! Digite a sua idade para que eu possa dizer se você pode beber álcool ou não:"))

if idade >= 70:
    print("Cuidado com a bebida!")
    print("Consulte seu geriatra")

elif idade >= 18:
    print("Você pode beber álcool")
    print("Beba com moderação!")

else:
    print("Você não pode beber álcool")
    print("Vá pra casa beber leite!")