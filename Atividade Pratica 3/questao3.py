# Solicitando os dados
temp = float(input("Digite o valor da temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

# Lógica de conversão
if origem == destino:
    resultado = temp
elif origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    elif destino == "K":
        resultado = temp + 273.15
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    elif destino == "K":
        resultado = (temp - 32) * 5/9 + 273.15
elif origem == "K":
    if destino == "C":
        resultado = temp - 273.15
    elif destino == "F":
        resultado = (temp - 273.15) * 9/5 + 32
else:
    print("Unidade inválida!")
    resultado = None

# Exibindo o resultado
if resultado is not None:
    print(f"A temperatura convertida é: {resultado:.2f} {destino}")