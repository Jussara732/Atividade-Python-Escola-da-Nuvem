# Solicitando a idade ao usuário
idade = int(input("Digite a sua idade: "))

# Verificando se o número é inválido (menor que zero)
if idade < 0:
    print("Erro: digite um número válido.")
# Se for válido, seguimos com a classificação normal
elif idade <= 12:
    print("Categoria: Criança")
elif idade <= 17:
    print("Categoria: Adolescente")
elif idade <= 59:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")