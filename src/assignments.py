from TeamScrap import TeamScrap
from colorama import Fore, Style
from datetime import datetime, timedelta
from crypt import Crypt
import ascii_art
import json

def clear_token():
	encrypted_token_file = open('token.txt', 'wb')
	encrypted_token_file.write(''.encode())
	encrypted_token_file.close()

def parse_teams_date_time(date_time):
	all_date_parsed = date_time.split('T')
	date_parsed = all_date_parsed[0].split('-')
	hour_parsed = all_date_parsed[1].replace('Z', '').split(':')

	return [date_parsed, hour_parsed]

def parse_date_time(date_time):
	all_date_parsed = str(date_time).split(' ')
	date_parsed = all_date_parsed[0].split('-')
	hour_parsed = all_date_parsed[1].split(':')

	return [date_parsed, hour_parsed]

def get_assignments():

	print(ascii_art.return_ascii())

	print('Tentando encontrar o Bearer token...\n')

	c = Crypt()

	encrypted_token_file = open('token.txt', 'rb')
	encrypted_token = encrypted_token_file.read()
	encrypted_token_file.close()

	if not encrypted_token:
		print(f'{Fore.YELLOW}Não conseguimos localizar seu token salvo em cache, digite manualmente{Style.RESET_ALL}')
		print('Digite o seu bearer token do Teams: ')
		bearer_token = str(input('')).strip()

		print('\n')
		print(Fore.YELLOW + '!' + Style.RESET_ALL)
		print(Fore.YELLOW + 'Não se preocupe, não enviaremos essa informação para nenhum local, apenas será encriptada na sua máquina como cache.' + Style.RESET_ALL)
		print(Fore.YELLOW + '!' + Style.RESET_ALL)
		print('\n')

		key_file = open('key.key', 'rb')
		key = key_file.read()
		key_file.close()

		if not key:
			c.generate_new_key()
			c.encrypt(bearer_token)
		else:
			c.encrypt(bearer_token)

		encrypted_token_file = open('token.txt', 'rb')
		encrypted_token = encrypted_token_file.read()
		encrypted_token_file.close()

		if not encrypted_token:
			print(f'{Fore.RED}Ocorreu um erro, tente novamente{Style.RESET_ALL}')

		original_token = c.decrypt(encrypted_token)
	else:
		try:
			original_token = c.decrypt(encrypted_token)
		except Exception as err:
			print(f'{Fore.RED}{err}{Style.RESET_ALL}')
			clear_token()
			exit()

		print(f'{Fore.BLUE}Seu token foi encontrado em cache!{Style.RESET_ALL}\n')

	print('Pegando assignments... (Isso pode demorar alguns minutos)\n')

	ts = TeamScrap(original_token)

	try:
		classes_assignments = ts.get_all_classes_assignments()
	except Exception as err:
		print(f'{Fore.RED}{err}{Style.RESET_ALL}\n')
		print(f'{Fore.RED}Verifique se o token não expirou ou está correto{Style.RESET_ALL}\n')
		clear_token()
		exit()
		
	overdue_assignments = 0

	print('=' * 100)
	message = ""
	for class_assignment in classes_assignments:
		created_date_time = class_assignment['assignmentInfo']['createdDateTime']
		[created_date_parsed, created_hours_parsed] = parse_teams_date_time(created_date_time)
		created_date_final = datetime(year=int(created_date_parsed[0]), month=int(created_date_parsed[1]), day=int(created_date_parsed[2]))
		bimester_init_date = datetime(year=int(2021), month=int(2), day=int(1))

		if created_date_final > bimester_init_date:
			print('\n')
			print('=' * 100)
			print(class_assignment)
			message += f"""\n\n📝 Tarefa: {class_assignment['assignmentInfo']['displayName']}
						\n📚 Disciplina: {class_assignment["classInfo"][0]["name"]}
						\n⏳ Data de entrega: {final_date_parsed[2]}/{final_date_parsed[1]}/{final_date_parsed[0]}
						às {final_hours_parsed[0]}:{final_hours_parsed[1]}:{final_hours_parsed[2]}"""

			if class_assignment['assignmentInfo']['allowLateSubmissions'] == true:
				message += "\n⏰ Aceita atrasos: ✅SIM✅"
			else:
				message += "\n⏰ Aceita atrasos: ❌NÃO❌"

			due_date_time = class_assignment['assignmentInfo']['dueDateTime']
			[date_parsed, hours_parsed] = parse_teams_date_time(due_date_time)

			date_init = datetime.now()
			date_final = datetime(year=int(date_parsed[0]), month=int(date_parsed[1]), day=int(date_parsed[2]), hour=int(hours_parsed[0]), minute=int(hours_parsed[1]), second=int(hours_parsed[2]))

			date_final -= timedelta(hours=3)

			[final_date_parsed, final_hours_parsed] = parse_date_time(date_final)

			remaining_date = date_final - date_init

			remaining_date_parsed = str(remaining_date).split(',')

			if len(remaining_date_parsed) > 1:
				remaining_days = int(remaining_date_parsed[0].strip().split(' ')[0])
				remaining_hours = remaining_date_parsed[1].strip().split(':')
			else:
				remaining_hours = remaining_date_parsed[0].strip().split(':')

			if int(remaining_days) < 0:
				message += "\n⚙️ Status: ⌛️VENCIDA⌛️"
			else:
				message += "\n⚙️ Status: 🏃CORRE QUE DÁ TEMPO🏃"

		else:
			pass

		print('\n') 
		print(message)
		return message