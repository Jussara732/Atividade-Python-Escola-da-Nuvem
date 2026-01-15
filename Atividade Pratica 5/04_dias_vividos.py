# Programa para calcular dias vividos de acordo com a data do dia 
from datetime import date

def calcular_dias_vividos():
    # 1. Interação: Pede os dados de nascimento
    dia = int(input("Em que dia você nasceu? (ex: 15): "))
    mes = int(input("Em que mês você nasceu? (ex: 01): "))
    ano = int(input("Em que ano você nasceu? (ex: 1990): "))
    
    # 2. Criação das datas: Transforma os números em objetos de data
    data_nascimento = date(ano, mes, dia)
    data_hoje = date.today() # Pega a data atual do computador
    
    # 3. Cálculo: A álgebra de datas no Python é direta (subtração)
    diferenca = data_hoje - data_nascimento
    
    # 4. Exibição: O .days extrai apenas o número de dias do resultado
    print("-" * 30)
    print(f"Hoje é dia: {data_hoje.strftime('%d/%m/%Y')}")
    print(f"Você já viveu aproximadamente {diferenca.days} dias!")

# Executa o programa
calcular_dias_vividos()