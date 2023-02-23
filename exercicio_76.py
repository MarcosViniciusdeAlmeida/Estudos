"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = input ('Diga a palavra secreta: ')

qtd_letras_secreta = len(palavra_secreta)

i = 0 #tentativas

letra_certa = ''

while True:
    i += 1
    letra_digitada = input ('Diga uma letra que acha que está na palavra secreta: ')
    if len(letra_digitada) == 1:

        for letra_digitada in palavra_secreta:
            if letra_digitada in letra_certa:
                print (letra_digitada)
            else:
                print ('*')
            letra_digitada = ''
        
    if letra_digitada in palavra_secreta:
        letra_certa += letra_digitada
    else:  
        letra_digitada== ''
    if len(letra_digitada) >1:
        print ('Digite apenas uma letra.')
