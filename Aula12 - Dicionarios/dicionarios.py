# Dicionarios são similares a arrays associativos, hashmaps, structs em C, etc.

# aluno = {
#     'ra':'0001',
#     'nome': 'Marco Silva',
#     'idade': 24,
#     'sala': '13B'
# }

# print(f'RA: {aluno['ra']}')
# print(f'Nome: {aluno['nome']}')
# print(f'Idade: {aluno['idade']}')
# print(f'Sala: {aluno['sala']}')
# print(f'O dicionário possui {len(aluno)} \"categorias\".')

funcionario = {
    'cod': '',
    'cargo': '',
    'nome': '',
    'salario': '',
    'setor': ''
}

funcionario['cod'] = input('Digite o codigo do funcionario: ')
funcionario['cargo'] = input('Digite o cargo do funcionario: ')
funcionario['nome'] = input('Digite o nome do funcionario: ')
funcionario['salario'] = input('Digite o salario do funcionario: ')
funcionario['setor'] = input('Digite o setor do funcionario: ')

print(f'Segue abaixo os dados do funcionário: \n' + str(funcionario))

# Atualizar uma entrada
funcionario['cargo'] = 'Gerente adm.'
print(str(funcionario))

# Adicionar uma entrada
funcionario['dataEntrada'] = 2021
print(str(funcionario))

# Excluir itens
del funcionario['dataEntrada']
print(str(funcionario))

# Excluir todos os dados
funcionario.clear()
print(str(funcionario))

# Excluir totalmente o dicionário
# del funcionario

# .items, .values e . keys acessam os dados de um dicionario, items mostra todas as chaves e valores individualmente, values somente os valores
# e keys as chaves. Convém manipuá-los com um laço for. 

      
    









