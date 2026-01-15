def verificar_palindromo(texto):
    # Filtra apenas letras e números, transformando em minúsculo
    texto_limpo = "".join(c.lower() for c in texto if c.isalnum())
    
    # Compara a string limpa com ela mesma invertida (Slicing)
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Entrada e exibição do resultado
entrada = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(entrada)

print(f"O resultado é: {resultado}")
    