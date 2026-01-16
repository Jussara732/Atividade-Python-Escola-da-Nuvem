#programa que gera senhas aleatórias com letras, números e símbolos
import random
import string

def gerar_senha(tamanho):
    # Definindo os conjuntos de caracteres
    letras = string.ascii_letters  # Letras maiúsculas e minúsculas
    numeros = string.digits         # Números de 0 a 9
    simbolos = string.punctuation   # Símbolos como !@#$%...

    # Combinando todos os caracteres em uma única base
    todos_os_caracteres = letras + numeros + simbolos

    # Gerando a senha aleatoriamente
    # random.choices seleciona 'tamanho' caracteres da nossa base
    senha_lista = random.choices(todos_os_caracteres, k=tamanho)
    
    # Transformando a lista em uma string única
    senha_final = "".join(senha_lista)
    
    return senha_final

# --- Interface com o usuário ---
print("--- Gerador de Senhas Seguras ---")

try:
    tamanho_desejado = int(input("Digite o tamanho da senha (ex: 12): "))
    
    if tamanho_desejado < 4:
        print("Aviso: Senhas muito curtas não são seguras. Recomendamos pelo menos 8 caracteres.")
    
    senha = gerar_senha(tamanho_desejado)
    
    print("-" * 30)
    print(f"Sua nova senha é: {senha}")
    print("-" * 30)

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros para o tamanho.")