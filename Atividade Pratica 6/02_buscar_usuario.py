#programa que acessa a API Random User Generator para buscar um usuário fictício aleatório
import requests

def buscar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    
    try:
        # Fazendo a requisição GET para a API
        resposta = requests.get(url, timeout=10)
        
        # Verifica se a conexão foi bem-sucedida (Status Code 200)
        resposta.raise_for_status()
        
        # Converte o conteúdo JSON para um dicionário Python
        dados = resposta.json()
        
        # Navegando na estrutura dos dados (Resultados -> Primeiro item da lista)
        usuario = dados['results'][0]
        
        # Extraindo as informações solicitadas
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibindo os resultados
        print("--- Usuário Fictício Encontrado ---")
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        print("-" * 35)

    except requests.exceptions.RequestException as e:
        # Caso haja qualquer erro na conexão (URL errada, sem internet, etc)
        print(f"Falha na conexão: Não foi possível acessar a API.")
        print(f"Detalhes do erro: {e}")

# Executa a função
if __name__ == "__main__":
    buscar_usuario_aleatorio()