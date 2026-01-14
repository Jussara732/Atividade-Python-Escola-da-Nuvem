# Criar um código que serve para analisar números digitados pelo usuario é par ou impar
pares = 0
impares = 0

try:
    for i in range(1, 6):
        numero = int(input(f"Digite o {i}º número: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

except ValueError:
    # Caso o usuário digite algo que não seja um número inteiro
    print("Erro: Por favor, digite apenas números inteiros.")

finally:
    # Este bloco SEMPRE será executado, independentemente de erro ou não
    print(f"\nAnálise concluída!")