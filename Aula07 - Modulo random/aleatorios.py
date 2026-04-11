import random as rd

# valor = rd.randint(0, 1000) # numero inteiro aleatorio entre dois numeros.

# print(valor)

# print('Gerar 5 números aleatórios entre 1 e 50.\n')

# for i in range(5):
#     n = rd.randint(1,25)
#     print(f'Número gerado: {n}')

# valor = rd.random() # numero flutuante aleatorio por padrão entre 0 e 1.
# valor2 = rd.uniform(1,100) # numero flutuante aleatorio definido pelo dev

# print(f'Número gerado: {valor * 10:.2f}')
# print(f'Número gerado: {round(valor * 10,2)}') # função round() para arredondamento.
# print(f'Número gerado: {round(valor2,2)}')

valores = [] 

for _ in range(15): # '_' convenção do python pra não usar o contador quando este é irrelevante
    while 1:
        valor = rd.randint(1, 25)
        if valor not in valores:
            valores.append(valor)
            break

n = rd.choice(valores) # Sortear um número em uma lista.
m = rd.sample(valores, 5) # Sorteio de números em uma lista, primeiro arg é a lista e o segundo a quantidade de números.

print(f'A lista é: \n' + str(valores))

l = rd.shuffle(valores) # função rd.shuffle() embaralha a lista.

print('A lista embaralhada: \n' + str(valores)  + '\nE o número sorteado foi: \n' + str(n) + '\nE os números sorteados foram: \n' + str(m))
    