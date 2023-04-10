import itertools   # importa o módulo itertools para criar as combinações de caracteres
import time        # importa o módulo time para medir o tempo de execução

def linha():        # define uma função para imprimir uma linha de separação
    print('\n\033[1;35m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

info = []           # define uma lista vazia para armazenar as informações pessoais

# Imprime um cabeçalho com informações sobre o programa
print('\n\033[1;35m------------------------------------------\n\n\033[1;31m T H 3  W 3 3 L \033[32m3.0\033[1;31m| WORDLIST GENERATOR\n\n\033[1;96m~ by: Ydr0l\n\n\033[1;35m------------------------------------------\n')

# Solicita ao usuário que escolha uma escala para a geração de palavras
escala = input('\033[1;92m[!] Escolha uma escala [ex: "1 a 15" = 1:15] [!] : ')
start = int(escala.split(':')[0])  # define o valor inicial da escala
final = int(escala.split(':')[1])  # define o valor final da escala

linha()  # imprime uma linha de separação

# Solicita ao usuário que escolha se quer criar uma lista pessoal de informações
personal_list = str(input("\n\033[1;92m[?] Quer criar uma lista pessoal ? [Y/N] [?] : ")).upper()

# Se o usuário escolher criar uma lista pessoal, solicita as informações e as adiciona à lista 'info'
if personal_list == 'Y':
    while True:
        str_info = input(f"\n\033[1;96m[*] Informação {len(info)+1} : ")
        info.append(str_info)

        linha()

        moreinfo = str(input("\n\033[1;92m[*] Quer acrescentar mais informação? [Y/N] [*] : ")).upper()

        linha()

        if moreinfo != 'Y':
            break

# Concatena as informações pessoais em uma única string
info_str = ''.join(info)

chars = []           # define uma lista vazia para armazenar os caracteres para a geração de palavras
chars_str = ''       # define uma string vazia para armazenar os caracteres selecionados

# Solicita ao usuário que selecione os tipos de caracteres para a geração de palavras
if str(input('\n\033[36m[?] Quer usar o alfabeto? [Y/N] [?] : ')).upper() == 'Y':
    chars.extend(list('abcdefghijklmnopqrstuvwxyz'))
    chars_str = ''.join(chars)
if str(input('\n\033[36m[?] Quer usar caracteres maiusculos? [Y/N] [?] : ')).upper() == 'Y':
    chars.extend(list(info_str.upper()))
    if chars_str == '':
        chars.extend(list(chars_str.upper()))
if str(input('\n\033[36m[?] Quer usar caracteres especiais? [Y/N] [?] : ')).upper() == 'Y':
    chars.extend(list('!\][/?.,~-=";:><@#$%&*()_+\' '))
if str(input('\n\033[36m[?] Quer usar caracteres numericos? [Y/N] [?] : ')).upper() == 'Y':
    chars.extend(list('1234567890'))
# Recebe a entrada do usuário para permitir ou não caracteres repetidos na wordlist
repeat_chars = str(input('\n\033[36m[?] Quer permitir caracteres repetidos? [Y/N] [?] : ')).upper()

# Recebe a entrada do usuário para o nome do arquivo de saída e o abre em modo de escrita
file_name = input('\n\033[1;91m[!] Qual o nome da sua wordlist? [!] : ')
arq = open(file_name+".txt", 'w')

# Inicia o temporizador para calcular o tempo gasto na geração da wordlist
then = time.time()

# Imprime uma mensagem para indicar o início do processo de geração da wordlist
print("\n\033[1;32m [!] Gerando a wordlist [!]\n")

# Conjunto para armazenar as combinações já usadas
used_combinations = set()

# Loop que gera as combinações e as escreve no arquivo
for i in range(start, final+1):
    for j in itertools.product(chars, repeat=i):
        temp = ''.join(j)
        if repeat_chars == 'N':
            # Verifica se a combinação já foi utilizada e se não há caracteres repetidos na combinação atual
            if not any(c in temp for c in used_combinations) and len(set(temp)) == len(temp):
                used_combinations.add(temp)
                arq.write(temp + '\n')
        else:
            arq.write(temp + '\n')

# Fecha o arquivo
arq.close()

# Finaliza o temporizador e imprime uma mensagem indicando a conclusão do processo de geração da wordlist
now = time.time() 
print("\033[1;32m [!] Finalizado [!]")
print("\033[1;32m O processo durou: ", now-then, " segundos.")
