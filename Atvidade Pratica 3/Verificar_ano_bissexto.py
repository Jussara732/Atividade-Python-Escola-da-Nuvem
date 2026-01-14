# Solicitando o ano ao usuário
ano = int(input("Digite o ano que deseja verificar: "))

# Lógica para determinar se o ano é bissexto
# 1. Divisível por 4 e NÃO divisível por 100
# 2. OU divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto.")