# Consulta CEP utilizando a API ViaCEP
import requests

def consultar_cep():
    print("--- Consulta de Endereço (ViaCEP) ---")
    cep = input("Digite o CEP (apenas números): ")

    # A URL do ViaCEP aceita o CEP e o formato de retorno (json)
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        
        # Verifica se houve erro de conexão (ex: 404 ou 500)
        resposta.raise_for_status()
        
        dados = resposta.json()

        # O ViaCEP retorna um campo "erro" se o CEP for válido mas não existir
        if "erro" in dados:
            print("Erro: O CEP digitado não foi encontrado na base de dados.")
        else:
            # Exibindo os dados formatados
            print(f"\nResultado para o CEP {cep}:")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro:     {dados.get('bairro', 'N/A')}")
            print(f"Cidade:     {dados.get('localidade', 'N/A')}")
            print(f"Estado:     {dados.get('uf', 'N/A')}")
            print("-" * 30)

    except requests.exceptions.RequestException:
        print("Falha na conexão: Verifique sua internet ou se o CEP tem 8 dígitos.")

if __name__ == "__main__":
    consultar_cep()