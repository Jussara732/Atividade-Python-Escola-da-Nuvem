#Calcular Gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    # O cálculo da gorjeta
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta
# Inetração com o usuário (entrada de dados)
valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta que deseja deixar (ex: 10, 15, 20): "))
# Cálculo da gorjeta
gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
# Exibindo o resultado
print(f"O valor da gorjeta é: R$ {gorjeta}")