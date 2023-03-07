import itertools
import time

def linha():
    print('\n\033[1;35m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

info = []

print('\n\033[1;35m------------------------------------------\n\n\033[1;31m T H 3  W 3 3 L \033[32m2.0\033[1;31m| WORDLIST GENERATOR\n\n\033[1;96m~ by: Ydr0l\n\n\033[1;35m------------------------------------------\n')

escala = input('\033[1;92m[!] Escolha uma escala [ex: "1 a 15" = 1:15] [!] : ')
start = int(escala.split(':')[0])
final = int(escala.split(':')[1])

linha()

personal_list = str(input("\n\033[1;92m[?] Quer criar uma lista pessoal ? [Y/N] [?] : ")).upper()

if personal_list == 'Y':
    while True:
        str_info = input(f"\n\033[1;96m[*] Informação {len(info)+1} : ")
        info.append(str_info)

        linha()

        moreinfo = str(input("\n\033[1;92m[*] Quer acrescentar mais informação? [Y/N] [*] : ")).upper()

        linha()

        if moreinfo != 'Y':
            break

info_str = ''.join(info)
chars = []
chars_str = ''

chars.extend(list(info_str))
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
repeat_chars = str(input('\n\033[36m[?] Quer permitir caracteres repetidos? [Y/N] [?] : ')).upper()

file_name = input('\n\033[1;91m[!] Qual o nome da sua wordlist? [!] : ')
arq = open(file_name+".txt", 'w')

then = time.time()

print("\n\033[1;32m [!] Gerando a wordlist [!]\n")

used_combinations = set()

for i in range(start, final+1):
    for j in itertools.product(chars, repeat=i):
        temp = ''.join(j)
        if repeat_chars == 'N':
            if not any(c in temp for c in used_combinations) and len(set(temp)) == len(temp):
                used_combinations.add(temp)
                arq.write(temp + '\n')
        else:
            arq.write(temp + '\n')

arq.close()

now = time.time() 
print("\033[1;32m [!] Finalizado [!]")
print("\033[1;32m O processo durou: ", now-then, " segundos.")