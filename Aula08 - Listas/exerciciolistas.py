# Crie um script que peça para o user digitar o nome de 5 bebidas, armazenando em uma lista. Exiba na tela os elementos da lista
# em ordem alfabética, um por lista, usando um laço de repetição for

bebidas = []

for _ in range(5):
        bebidas.append(input('Digite sua bebida favorita: '))

bebidas.sort()

for bebida in bebidas:
    print(bebida)