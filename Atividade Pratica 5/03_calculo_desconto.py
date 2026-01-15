# Programa para calcular o preço final de um produto após aplicar um desconto500
def calcular_preco_final():
    # d - Interação com usuário: Pede os valores e converte para decimal (float)
    preco_base = float(input("Digite o preço original do produto: R$ "))
    porcentagem = float(input("Digite a porcentagem de desconto: "))
    
    # a - Cálculo de desconto: Multiplica o preço pela taxa (ex: 10/100 = 0.1)
    valor_desconto = preco_base * (porcentagem / 100)
    
    # b - Preço final: Subtrai o desconto do valor original
    preco_final = preco_base - valor_desconto
    
    # c - Formatação: O :.2f garante as 2 casas decimais (centavos)
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final a pagar: R$ {preco_final:.2f}")

# Chamada da função para o programa rodar
calcular_preco_final()