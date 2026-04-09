# lista = [0, 3, 8, 9, 1, 4, 12, 16, 1]
# palavra = 'Marco'

# for item in lista:
#     print(item)

# for letra in palavra:
#     print(letra)

# range(valor_inicial, valor_final, incremento)
# valor final (sempre gera valor final - 1)

# for numero in range(1, 11): 
#     print(numero)

x = 85

for i in range(0, 101, 10):
    print(i)
    if(i > x):
        x *= i
        print(x)
        break

# continue = encerra a interação atual
# break = encerra o laço.