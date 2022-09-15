import itertools
import time
    
def linha():
	print('\n\033[1;35m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def en():
    info = []
    num = 1
    chrs = ''

    print('\n\033[1;35m------------------------------------------\n\n\033[1;31m T H 3  W 3 3 L \033[32m2.0\033[1;31m| WORDLIST GENERATOR\n\n\033[1;96m~ by: Ydr0l\n\n\033[1;35m------------------------------------------\n')

    escala = input('\033[1;92m[!] Choose a scale [ex: "1 to 15" = 1:15] [!] : ')
    start = int(escala.split(':')[0])
    final = int(escala.split(':')[1])

    linha()

    personal_list = str(input("\n\033[1;92m[?] Want to create a personal list ? [Y/N] [?] : ")).upper()

    linha()

    if personal_list == 'Y':
    
	    moreinfo = 'Y'

	    while moreinfo == 'Y':

		    str(info.append(input(f"\n\033[1;96m[*] Information {num} : ")))

		    linha()

		    moreinfo = str(input("\n\033[1;92m[*] Want to add more information? [Y/N] [*] : ")).upper()

		    linha()
		    num = num + 1

    for inf in info :
	    chrs = ''.join([chrs, inf])

    chrs_alfabetic = 'abcdefghijklmnopqrstuvwxyz'
    chrs_up = chrs.upper()
    chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
    chrs_numerics = '1234567890'

    file_name = input('\n\033[1;91m[!] What is the name of your wordlist? [!] : ')
    arq = open(file_name, 'w')
    if str(input('\n\033[36m[?] Want to use the alphabet? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_alfabetic])
    if str(input('\n\033[36m[?] Want to use uppercase characters? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_up])
    if str(input('\n\033[36m[?] Want to use special characters? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_specials])
    if str(input('\n\033[36m[?] Want to use numeric characters? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_numerics])

    then = time.time() 

    print("\n\033[1;32m [!] Generating the wordlist [!]")

    for i in range(start, final+1):
	    for j in itertools.product(chrs, repeat=i):
		    temp = ''.join(j)

		    arq.write(temp + '\n')
    arq.close()

    now = time.time() 
    print("\033[1;32m [!] Finished [!]")
    print("\033[1;32mO Process lasted: ", now-then, " Seconds.")

def pt():
    info = []
    num = 1
    chrs = ''

    print('\n\033[1;35m------------------------------------------\n\n\033[1;31m T H 3  W 3 3 L \033[32m2.0\033[1;31m| WORDLIST GENERATOR\n\n\033[1;96m~ by: Ydr0l\n\n\033[1;35m------------------------------------------\n')

    escala = input('\033[1;92m[!] Escolha uma escala [ex: "1 a 15" = 1:15] [!] : ')
    start = int(escala.split(':')[0])
    final = int(escala.split(':')[1])

    linha()

    personal_list = str(input("\n\033[1;92m[?] Quer criar uma lista pessoal ? [Y/N] [?] : ")).upper()

    linha()

    if personal_list == 'Y':
    
	    moreinfo = 'Y'

	    while moreinfo == 'Y':

		    str(info.append(input(f"\n\033[1;96m[*] Informação {num} : ")))

		    linha()

		    moreinfo = str(input("\n\033[1;92m[*] Quer acrescentar mais informação? [Y/N] [*] : ")).upper()

		    linha()
		    num = num + 1

    for inf in info :
	    chrs = ''.join([chrs, inf])

    chrs_alfabetic = 'abcdefghijklmnopqrstuvwxyz'
    chrs_up = chrs.upper()
    chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
    chrs_numerics = '1234567890'

    file_name = input('\n\033[1;91m[!] Qual o nome da sua wordlist? [!] : ')
    arq = open(file_name, 'w')
    if str(input('\n\033[36m[?] Quer usar o alfabeto? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_alfabetic])
    if str(input('\n\033[36m[?] Quer usar caracteres maiusculos? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_up])
    if str(input('\n\033[36m[?] Quer usar caracteres especiais? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_specials])
    if str(input('\n\033[36m[?] Quer usar caracteres numericos? [Y/N] [?] : ')).upper() == 'Y':
	    chrs = ''.join([chrs, chrs_numerics])

    then = time.time() 

    print("\n\033[1;32m [!] Gerando a wordlist [!]")

    for i in range(start, final+1):
	    for j in itertools.product(chrs, repeat=i):
		    temp = ''.join(j)

		    arq.write(temp + '\n')
    arq.close()

    now = time.time() 
    print("\033[1;32m [!] Finalizado [!]")
    print("\033[1;32mO Processo durou: ", now-then, " segundos.")

lingua = str(input('\n\033[36m[?] Choose a language: 1 or 2 [EN-US/PT-BR] [?] : ')).upper()

if lingua == '1'
    pt()
if lingua == '2'
    en()
