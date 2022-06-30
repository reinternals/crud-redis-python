# - modulo necessário para realizar as operações de CRUD no redis.
import redis								  # pip install redis

# Função - CREATE.
def fCreate():
	chave = input('Insira a chave: ')
	valor = input('Insira o valor: ')
	conexao.set(f'{chave}',f'{valor}')
	fContinuar()

# Função - READ.
def fRead():
	chave = input('Insira a chave: ')
	print(conexao.get(chave))
	fContinuar();

# Função - UPDATE.
def fUpdate():
	chave = input('Insira a chave: ')
	valor = input('Insira o novo valor: ')
	conexao.set(f'{chave}',f'{valor}')
	fContinuar()

# Função - DELETE.
def fDelete():
	chave = input('Informe a chave: ')
	conexao.delete(chave)
	fContinuar()

# Função - close.
def fClose():
	conexao.connection_pool.disconnect()
	print('conexao encerrada com sucesso.\nBye!')
	exit()

# Função - continuar.
def fContinuar():
	vContinuar = input('deseja realizar outra consulta? s - sim. n - nao.')
	if vContinuar.lower() == 's':
		fMenu()
	elif vContinuar.lower() == 'n':
		fClose()
	else:
		print('Opcao invalida!')
		fContinuar()

# Função - Menu.
def fMenu():
	print('Escolha uma das opções abaixo.')
	print('1 - CREATE.\n2 - READ.\n3 - UPDATE.\n4 - DELETE.\n5 - SAIR.')
	escolha = input('Digite o numero da opcao: ')
	if escolha == '1':
		fCreate()
	elif escolha == '2':
		fRead()
	elif escolha == '3':
		fUpdate()
	elif escolha == '4':
		fDelete()
	elif escolha == '5':
		fClose()
	else:
		print('opcao invalida!')
		fContinuar()

# - Conexão com o redis.
conexao = redis.Redis(host='localhost', port=6379)

# - Chamada das funções.
fMenu()