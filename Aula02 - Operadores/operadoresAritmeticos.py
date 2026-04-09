x = y = z = a = b = c = d = e = f = 0

# input() exibe na tela uma mensagem e captura o que o user digita, retorna por padrão dados do tipo str.
# casting é a transformção dos dados em um tipo especifico, ex: int(), str(), float()

x = int(input('Digite um numero: ')) 
y = int(input('Digite um numero: ')) 

z = x + y # soma
a = x - y # subtracao
b = x / y # divisao real
c = x // y # divisao inteira
d = x % y # modulo
e = x ** y # potencia
f = x ** 0.5 # raiz quadrada


print('A soma dos valores é', z)
print('A subtração dos valores é', a)
print('A divisao real dos valores é', b)
print('A divisao inteira dos valores é', c)
print('O modulo dos valores é', d)
print('A potencia dos valores é', e)
print('A raiz quadrada do valor é', f)

