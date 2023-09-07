import itertools
import time

# Função para gerar a wordlist
def generate_wordlist(start, final, chars, repeat_chars, file_name):
    try:
        print("\n\033[1;32m [!] Gerando a wordlist [!]\n")

        arq = open(file_name + ".txt", 'w')
        buffer = []  # Buffer para armazenar palavras antes de escrevê-las

        then = time.time()

        used_combinations = set()

        for i in range(start, final + 1):
            for j in itertools.product(chars, repeat=i):
                temp = ''.join(j)
                if repeat_chars == 'N':
                    if temp not in used_combinations and len(set(temp)) == len(temp):
                        used_combinations.add(temp)
                        buffer.append(temp)  # Adicione à lista de buffer
                else:
                    buffer.append(temp)  # Adicione à lista de buffer

                if len(buffer) >= 1000:  # Escreva em lotes de 1000 palavras
                    arq.write('\n'.join(buffer) + '\n')
                    buffer = []

        # Certifique-se de escrever qualquer coisa restante no buffer
        arq.write('\n'.join(buffer) + '\n')

        arq.close()

        now = time.time()
        print("\033[1;32m [!] Finalizado [!]")
        print("\033[1;32m O processo durou: ", now - then, " segundos.")

    except IOError as e:
        print(f"Erro ao abrir o arquivo: {e}")

# Função para obter a escala a ser usada
def get_scale():
    while True:
        escala = input('\033[1;92m[!] Escolha uma escala [ex: "1 a 15" = 1:15] [!] : ')
        try:
            start, final = map(int, escala.split(':'))
            if start < 1 or final < start:
                print("Intervalo de escala inválido. Tente novamente.")
                continue
            return start, final
        except ValueError:
            print("Entrada inválida. Use o formato '1:15'. Tente novamente.")

# Função para criar uma lista pessoal de informações
def create_personal_list():
    info = []
    while True:
        str_info = input(f"\n\033[1;96m[*] Informação {len(info)+1} : ")
        info.append(str_info)

        print('\n\033[1;35m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

        moreinfo = input("\n\033[1;92m[*] Quer acrescentar mais informação? [Y/N] [*] : ").strip().upper()

        print('\n\033[1;35m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

        if moreinfo != 'Y':
            break
    return info

# Função principal
def main():
    print('\n\033[1;35m------------------------------------------\n\n\033[1;31m T H 3  W 3 3 L \033[32m3.0\033[1;31m| WORDLIST GENERATOR\n\n\033[1;96m~ by: Ydr0l\n\n\033[1;35m------------------------------------------\n')

    while True:
        start, final = get_scale()

        print('\n\033[1;35m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

        personal_list = input("\n\033[1;92m[?] Quer criar uma lista pessoal ? [Y/N] [?] : ").strip().upper()

        info = []

        if personal_list == 'Y':
            info = create_personal_list()

        info_str = ''.join(info)

        chars = list(info_str)  # Inicialize chars com as informações pessoais

        if input('\n\033[36m[?] Quer usar o alfabeto? [Y/N] [?] : ').strip().upper() == 'Y':
            chars.extend('abcdefghijklmnopqrstuvwxyz')

        if input('\n\033[36m[?] Quer usar caracteres maiúsculos? [Y/N] [?] : ').strip().upper() == 'Y':
            chars.extend([c.upper() for c in info_str if c.islower() and c.upper() not in chars])

        if input('\n\033[36m[?] Quer usar caracteres especiais? [Y/N] [?] : ').strip().upper() == 'Y':
            chars.extend('!\][/?.,~-=";:><@#$%&*()_+\' ')

        if input('\n\033[36m[?] Quer usar caracteres numéricos? [Y/N] [?] : ').strip().upper() == 'Y':
            chars.extend('1234567890')

        repeat_chars = input('\n\033[36m[?] Quer permitir caracteres repetidos? [Y/N] [?] : ').strip().upper()

        file_name = input('\n\033[1;91m[!] Qual o nome da sua wordlist? [!] : ').strip()

        generate_wordlist(start, final, chars, repeat_chars, file_name)

        if input("\n\033[1;92m[?] Deseja criar outra wordlist? [Y/N] [?] : ").strip().upper() != 'Y':
            break

if __name__ == "__main__":
    main()
