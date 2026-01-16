# Consulta cotação de moedas utilizando a AwesomeAPI
import requests
from datetime import datetime

def consultar_cotacao():
    print("\n" + "="*40)
    print("   CONSULTA DE MOEDAS (AwesomeAPI)   ")
    print("="*40)
    
    moeda = input("Digite o código da moeda (ex: USD, EUR, BTC, ARS, JPY, CHF, GBP): ").upper()

    # URL para converter a moeda escolhida para Real (BRL)
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        # Fazendo a requisição à API
        resposta = requests.get(url, timeout=10)
        
        # Verifica se a conexão foi bem-sucedida (Status 200)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        # A chave do dicionário retornado segue o padrão 'USDBRL', 'ARSBRL', etc.
        chave = f"{moeda}BRL"
        info = dados[chave]

        # Extraindo e convertendo os valores para números (float)
        valor_float = float(info['bid'])
        max_float = float(info['high'])
        min_float = float(info['low'])
        data_hora = info['create_date']

        # LÓGICA INTELIGENTE: 
        # Se a moeda valer menos que 1 centavo (0.01), mostra 4 casas decimais.
        # Caso contrário, mostra o padrão de 2 casas.
        decimais = 4 if valor_float < 0.01 else 2

        print(f"\nResultados para: {moeda} / BRL")
        print(f"-> Valor Atual: R$ {valor_float:.{decimais}f}")
        print(f"-> Máxima:      R$ {max_float:.{decimais}f}")
        print(f"-> Mínima:      R$ {min_float:.{decimais}f}")
        print(f"-> Atualizado em: {data_hora}")
        print("="*40)

    except requests.exceptions.RequestException:
        print(f"\n[!] Erro: Falha de conexão ou o código '{moeda}' não existe.")
    except KeyError:
        print(f"\n[!] Erro: A moeda '{moeda}' não pode ser convertida para Real.")

if __name__ == "__main__":
    consultar_cotacao()