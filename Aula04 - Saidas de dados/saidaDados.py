# Sintaxe:
# print(objetos, argumentos)

# mensagem = 'Função print()'
# print(mensagem, end = '') # Por padrão o print() faz quebra de linha
# print(' Aula de Python') # Desfazer quebra de linha com end = ''.

# nome = 'Marco Silva'
# curso = 'ADS'
# print('Olá', nome, 'você é estudante do curso de', curso)
# print('Olá ' + nome + ' você é estudante do curso de ' + curso + '.')

# mensagem = 'Olá ' + nome + ' você é estudante do curso de ' + curso + '.'

# print(mensagem)

# string.format(argumentos)

# nome = input('Digite o seu nome: ')
# idade = int(input('Digite a sua idade: '))

# msg_format = 'O seu nome é {0} e você tem {1} anos.' .format(nome, idade)

# print(msg_format)

# fString

# nome = input('Digite o seu nome: ')
# peso = float(input('Digite o seu peso: '))
# altura = float(input('Digite a sua altura: '))


# msg_format1 = f'Olá, meu nome é {nome}, peso {peso:.2f}kg e tenho {altura:.2f}m de altura.'

# print(msg_format1)

# x = y = 0.0

# x = float(input('Digite o divisor: '))
# y = float(input('Digite o dividendo: '))

# msg_format2 = f'A divisão entre {y:.2f} e {x:.2f} resulta em {y / x:.2f}.'

# print(msg_format2)

# Caracteres de escape:
# \n = quebra de linha
# \t = tabulação 
# \ + caractere especial para exibir no print, exemplo: \'