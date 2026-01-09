#Programa para calcular o preço total de uma compra
produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3
# Calculo do preço total
preco_total = preco_unitario * quantidade
print("Recibo de Compra")
print(f"Produto: {produto}")
print(f"Preço por unidade: R$ {preco_unitario:}")
print(f"Quantidade: {quantidade}")
print(f"Preço total a pagar: R$ {preco_total:.2f}")
