# Solicitando os dados ao usuário

peso = float(input("Digite o seu peso (ex: 70.5): "))
altura = float(input("Digite a sua altura (ex: 1.75): "))

# Cálculo do IMC: peso dividido pela altura ao quadrado
imc = peso / (altura * altura)

# Verificando a classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibindo o resultado final formatado
print(f"Seu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")