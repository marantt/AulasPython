import random

# Semelhante as listas porém são imutáveis.

# tupla = () -> como declarar uma tupla

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
numerosP = (2, 3, 5, 7)

soma = halogenios + numerosP

print(halogenios)
print(soma)
print(numerosP.count(5)) # determina quantas vezes um valor determinado aparece na tupla

# É possível declarar uma lista a partir de uma tupla, o inverso também é valido.

grupo1 = list(halogenios)
print(grupo1)

grupo2 = []

for _ in range(10):
    grupo2.append(random.randint(1,1000))

grupo3 = tuple(grupo2)
print(grupo2, '\n', grupo3)

