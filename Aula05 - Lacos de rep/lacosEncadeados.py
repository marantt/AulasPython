import random

# for contOut in range(1, 6):
#     print(f'\nRodada: {contOut}')
#     for contIn in range(5, 0, -1):
#         print(f'Valor: {contIn}')

# print('\nFim dos laços.')


for a in range(1, 6):
    print(f'\nConjunto {a}')
    for b in range(2):
        num = random.randint(1,100)
        print(f'Valor: {num}')

