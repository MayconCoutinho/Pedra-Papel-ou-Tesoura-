import random 
from time import sleep

cor1 = '\33[1;32m' 
cor0 = '\33[m'
def regras(): 
    print(24*'                                                                                                                            ')
    print(''' 
    Digite:
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        {1}[ 1 ]{0} Para pedra.   {1}[ 2 ]{0} Para papel.   {1}[ 3 ]{0} Para tesoura. 


                           ┌─┌─┬─┐            ┌─┐　─┐
                           │▒│▒|▒│─┐          │▒│ /▒/
     ┌─┬─┐─┬─┐             │▒│▒|▒│▒│          │▒│/▒/
     │▒│▒|▒│▒│             │▒│▒|▒│▒│          │▒ /▒/─┬─┐ 
    ┌┴─┴─┐-┘─┘            ┌┴─┴─┐-┘─┘          │▒│▒|▒│▒│
    │▒┌──┘▒▒▒│            │▒┌──┘▒▒▒│          │▒┌──┘▒▒▒│
    └┐▒▒▒▒▒▒┌┘            └┐▒▒▒▒▒▒┌┘          └┐▒▒▒▒▒▒┌┘
    　└┐▒▒▒▒┌┘             └┐▒▒▒▒┌┘            └┐▒▒▒▒┌



        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        \33[1;31m[ 0 ] Para sair do jogo. \33[m

        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
        '''.format(cor0,cor1))
                                                                                            

sair = False



while sair != True:
    regras() 

    jogadas = ['Pedra','Papel','Tesoura']

    jogador = int(input('----> '))
    confere_jogador = jogadas[(jogador-1)]

    computador = random.randint(1,3) 
    confere_computador = jogadas[(computador-1)]


    if jogador  == computador:
        print('\33[1;33m Empate  \33[m')
        print('computador jogou: {}'.format(confere_computador))
        print('Jogador jogou: {}'.format(confere_jogador))

    elif jogador == 3:
        if computador == 1:
            print('\033[1;31m você perdeu!\033[m')
            print('Computador jogou: {}'.format(confere_computador))
            print('Jogador jogou: {}'.format(confere_jogador))

        elif computador == 2:
            print('\33[0;32m Você ganhou!\33[m')
            print('Computador jogou: {}'.format(confere_computador))
            print('Jogador jogou: {}'.format(confere_jogador))

    elif jogador == 2:
        if computador == 1:
            print('\33[0;32m Você ganhou!\33[m')
            print('Computador jogou: {}'.format(confere_computador))
            print('Jogador jogou: {}'.format(confere_jogador))

        elif computador == 3:
            print('\33[1;31m Você perdeu! \33[m')
            print('Computador jogou: {}'.format(confere_computador))
            print('Jogador jogou: {}'.format(confere_jogador))
    elif jogador == 1:
        if computador == 2:
            print('\33[1;31m Você perdeu! \33[m')
            print('Computador jogou: {}'.format(confere_computador))
            print('Jogador jogou: {}'.format(confere_jogador))
        elif computador == 3:
            print('\33[0;32m Você ganhou! \33[m')
            print('Computador jogou: {}'.format(confere_computador))
            print('Jogador jogou: {}'.format(confere_jogador))
    elif jogador == 0:
        print('Saindo ...')
        sleep(3)
        print('Jogo finalizado')
        break
                    



                  