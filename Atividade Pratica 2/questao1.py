#Conversor de moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolar = valor_reais / taxa_dolar
euro = valor_reais / taxa_euro

print(f"Valor em Dólar: U$ {dolar:.2f}")
print(f"Valor em Euro: € {euro:.2f}")