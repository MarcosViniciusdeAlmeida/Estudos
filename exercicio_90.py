"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista 
não permita que o programa quebre com
erros de indices inexistentes na lista
"""

itens_de_compra = []

while True:
    print ('Selecione uma opção')
    variavel_1 = input('[i]nserir [a]pagar [l]istar:')

    if variavel_1 == 'i':
        item_adicionar = input ('Que item gostaria de adicionar? ')
        itens_de_compra.append(item_adicionar)

    try:
        if variavel_1 == 'a':  
            item_apagar = input ('Que item gostaria de apagar? ')
            del itens_de_compra[int(item_apagar)]
    except:
        print (f'O índice {item_apagar} não esta disponível.')    
    if variavel_1 == 'l':
        for indice, item in enumerate(itens_de_compra): 
          print (indice, item)