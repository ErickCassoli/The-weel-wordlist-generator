import itertools


ban = '''
                                                    '''

print('\n------------------\n\n T H 3  W 3 3 L \033[32m1.0\033[m | WORDLIST GENERATOR\n\n~ by: Ydr0l\n\n------------------\n')

escala = input('\033[36m[!] Escolha uma escala [ex: "1 a 15" = 1:15] : ')
start = int(escala.split(':')[0])
final = int(escala.split(':')[1])

personal_list = str(input("\n\033[36m[?] Quer criar uma lista pessoal ? [Y/N]: ")).upper()
if personal_list == 'Y':
	first_name = str(input("\n\033[36m[*] Primeiro nome: "))
	last_name = str(input("\n\033[36m[*] Segundo nome: "))
	birthday = str(input("\n\033[36m[*] Dia de nascimento: "))
	month = str(input("\n\033[36m[*] Mês: "))
	year = str(input("\n\033[36m[*] Ano: "))
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] Qual o nome da sua wordlist?: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Quer usar caracteres maiusculos? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Quer usar caracteres especiais? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Quer usar caracteres numericos? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()