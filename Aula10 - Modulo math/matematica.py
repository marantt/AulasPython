import random as rd
import math

# Funções builtin

# valores = []
# flutuantes = []

# for _ in range(10):
#     valores.append(rd.randint(1,10))

# for _ in range(10):
#     flutuantes.append(rd.uniform(0, 100))

# print(valores)
# print(max(valores))
# print(min(valores))

# b = -5

# print(abs(b)) # retorna valor absoluto
# print(pow(valores[0], valores[1])) # pontecia entre dois argumentos, 1º é a base e o 2 º o expo
# print(round(flutuantes[0], 3)) # Aredonda uma variavel, primeiro argumento é a variável e o segundo quantas casas

# https://docs.python.org/library/math.html

x, y = 8, 100

raiz_quadrada = math.sqrt(x)
print(math.ceil(raiz_quadrada)) # Inteiro arredondado pra cima
print(math.floor(raiz_quadrada)) # Inteiro arredondado pra baixo

logaritmo = math.log10(y) # log na base 10
print(logaritmo)