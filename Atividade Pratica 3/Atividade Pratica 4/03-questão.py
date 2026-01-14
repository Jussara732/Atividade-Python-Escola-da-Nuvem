# vereficador de senhas
senha = input("Digite a senha: ")
tem_numero = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
        break

# Este bloco decide: OU aparece erro, OU aparece sucesso (nunca os dois)
if len(senha) < 8 or not tem_numero:
    print("ERRO: A senha deve ter pelo menos 8 caracteres e conter um número.")
else:
    print("Senha validada com sucesso! Ela é segura.")
