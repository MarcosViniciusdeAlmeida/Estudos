nome = input ('Digite seu nome: ')
idade = input ('Digite sua idade: ')

nome_da_pessoa = nome
idade_da_pessoa = idade

nada = bool(nome_da_pessoa)
nada_idade = bool(idade_da_pessoa)

if nada and nada_idade == 1:
    print (f'Seu nome é: {nome_da_pessoa}')
    print (f'Seu invertido é: {nome_da_pessoa[::-1]}')
    if ' ' in nome_da_pessoa:
        print (f'Seu nome contém espaços')
    else:
        print ('Seu nome não contém espaços')
    print (f'Seu nome tem {len (nome_da_pessoa)} letras')
    print (f'A primeira letra do seu nome é "{nome_da_pessoa [0:1:]}" ')
    print (f'A última  letra do seu nome é "{nome_da_pessoa [:-2:-1]}" ')
else:
    print ('Desculpe, você deixou os campos vazios.')
