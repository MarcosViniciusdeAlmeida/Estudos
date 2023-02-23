"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_escrito = input ('Digite um número inteiro: ')

# if numero_escrito.isdigit(): 
#     numero_inteiro = int (numero_escrito)
#     if numero_inteiro % 2 == 0:
#         print (f'O número {numero_inteiro} é par ')
#     else:
#         print (f'O número {numero_inteiro} é impar')
# else:
#     print ('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input ('Diga a hora que está lendo isso:  ')

if hora.isdigit ():
     hora_int = int (hora)
     if hora_int <= 11:
         print ('Bom Dia!')
     elif hora_int <= 17 :
         print ('Boa Tarde!')
     else:
         print ('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input ('Diga seu primeiro nome: ')

# contagem = len (nome)

# if contagem <= 4:
#     print ('Seu nome é curto')
# elif contagem <= 6:
#     print ('Seu nome é normal')
# else:
#     print ('Seu nome é muito grande')