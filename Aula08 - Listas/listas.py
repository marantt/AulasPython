# # Listas representam uma sequencia de valores

# # Sintaxe: nome_lista = [valores]

# notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']

# # final = notas + dias # Concatenação de listas
# # notas[0] = 0 # Atribuição de um valor direto numa posição


# # print(final[4]) # Imprime o valor determinado na posição entre colchetes, o valor negativo retorna é procura de forma decrescente
# # print(final)
# # print(final[5:10]) # Seleciona um intervalo dentro da lista (slice)
# # print(len(final)) # Função len() determina o tamanho de uma lista
# # print(sorted(notas, reverse=True)) # Função sorted() ordena a lista mas não a altera, parâmetro reverse=True mostra o inverso da ordenação 

# # # É possível realizar operações com os valores das listas a partir de funções como sum(), min(), max()

# # print(sum(notas)) # Soma
# # print(max(notas)) # Maximo
# # print(min(notas)) # Minimo

# # nome_lista.append() insere um valor ao final da lista, enquanto nome_lista.pop() retira o valor podendo determinar a posição.

# notas.append(88)
# print(notas)
# notas.pop()
# print(notas)
# notas.pop(4)
# print(notas)

# # nome_lista.insert(posição, valor) insere um numero em uma posição determinada

# notas.insert(3, 99)
# print(notas)
# print(99 in notas) # verifica se o valor digitado está na lista, retornando true ou false


# for dia in dias: # percorrendo a lista
#     print(dia)
