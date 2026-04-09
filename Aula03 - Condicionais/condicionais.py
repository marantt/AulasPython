# Simples, composto e encadeado

n1 = n2 = media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if(media >= 6): # Só if, condicional simples
    print('\nParabéns, você foi aprovado. \n')
elif(media >= 4): # condicional encadeada
    print('\nVocê está de recuperação. \n')
else: # if-else, condicional composto
    print('\nQue pena, você foi reprovado. \n')
print('Sua média é {}' .format(media))
    
