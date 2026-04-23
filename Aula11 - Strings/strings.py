# nome = 'Marco'

# letra = nome[1]
# print(letra)
# print(nome[1])
# print(len(nome)) # len() -> tamanho da string

# frase = 'Temos 5 espécies de animais diferentes em casa.'

# palavras = frase.split() # Segrega uma string em palavras, a regra se baseia nos espaços entre as palavras

# for i in palavras:
#     print(i)

# print('\n' + frase)
# print('\n' + palavras[0] + '\n' + palavras[1] + '\n' + palavras[2])

email = input('Digite seu email: ')
arroba = email.find('@') # Encontra um caracter em uma string

usuario = email[0:arroba]
dominio = email[arroba+1:]

print(f'Seu usuário é: ' + usuario + '\nE seu dominio é: ' + dominio)

email_alt = email.replace(email[arroba+1:], 'gmail.com') # .replace() altera o conteúdo da string

print(email_alt)

# .lstrip(), .rstrip() e .strip() retiram os espaços a mais na string
# respectivamente, do começo, do final e dos dois.
# .rjust(), .center(), .ljust() servem para alinhar o texto.
# .startswith() retorna se uma string começa com o parâmetro determinado. ** CASE SENSI**
# .endswith() retorna se uma string termina com o parâmetro determinado. ** CASE SENSI**

# Docstrings
'''
Docstring é uma documentaçao que podemos inserir
a fim de explicar um módulo, função, classe, etc.
Respeita deslocamento do texto e é multilinhas.
É recomendado para quando for necessário um texto longo.
É inserida a partir de 3 aspas ou apóstrofos consecutivos.
'''
