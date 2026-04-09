import random as rd

# valor = rd.randint(0, 1000) # numero inteiro aleatorio entre dois numeros.

# print(valor)

valores = [] 

for _ in range(15):
    while 1:
        valor = rd.randint(1, 25)
        if valor not in valores:
            valores.append(valor)
            break

print(valores)
    