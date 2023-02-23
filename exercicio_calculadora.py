""" Calculadora com While  """

primeiro_numero = input ('Diga o primeiro número: ')
segundo_numero = input ('Diga o segundo número: ')
operacao = input ('Diga o simbolo da operação que deseja: ')

if primeiro_numero.isdigit() and segundo_numero.isdigit():
    float_segundo = float (segundo_numero)
    float_primeiro = float (primeiro_numero)
    operador_duplicado = len(operacao)
    while operacao == '+' and operador_duplicado == 1:
        soma = float_primeiro + float_segundo
        print (f'{soma}')
        break
    while operacao == '-' and operador_duplicado == 1:
        subtração = float_primeiro - float_segundo
        print (f'{subtração}')
        break
    while operacao == '/' and operador_duplicado == 1:
        divisao = float_primeiro / float_segundo
        print (f'{divisao}')
        break
    while operacao == '*' and operador_duplicado == 1:
        multiplicacao = float_primeiro * float_segundo
        print (f'{multiplicacao}')
        break
    if operador_duplicado >= 2:
        print (f'Você usou como operadores {operacao=}, usar somente um operador.')

else:
    print (f'{primeiro_numero=}, {segundo_numero=} e  {operacao=} não é um digito válido.')