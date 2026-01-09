#Calculadora de desconto
Nome_produto = "Camiseta"
Preco_original = 50.00
Percentual_desconto = 20

Valor_desconto = Preco_original * (Percentual_desconto / 100)
Preco_final = Preco_original - Valor_desconto

print(f"Produto: {Nome_produto}")
print(f"Preço original: R$ {Preco_original:.2f}")
print(f"Desconto: {Percentual_desconto}%")
print(f"Valor do desconto: R$ {Valor_desconto:.2f}")
print(f"Preço final: R$ {Preco_final:.2f}")