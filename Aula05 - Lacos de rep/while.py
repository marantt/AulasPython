# While()

num = 1

# while(num <= 10):
#     print(num)
#     num += 2

# print('Laço encerrado!')

nome = None # variavel vazia

while True:
    print('Digite seu nome ou \'Sair\' para parar: ')
    nome = input()

    if(nome == 'Sair' or nome == 'sair'):
        print('Até logo!')
        break
    
    print(f'Bem-vindo, {nome}!')
