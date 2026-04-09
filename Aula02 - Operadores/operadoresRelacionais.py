# a = 'marco'
# b = 'Marco'

# print(a==b) # retorna False
# print(a!=b) # retorna True

# x = 10
# y = 5

# print (x / 2 < y) # retorna False
# print (x / 2 <= y) # retorna True

x = y = z = False
n1 = n2 = 0

print('Digite um número: ') # Os dois jeitos funcionam
n1 = int(input())
n2 = int(input('Digite um número: '))

x = n1 == n2
y = n1 != n2
z = n1 > n2


print('São iguais? ', x, '\n')
print('São diferentes? ' + str(y) + '\n') # concat com '+' tem que usar casting a fim de evitar erros
print('n1 é maior que n2? ', z, '\n')



