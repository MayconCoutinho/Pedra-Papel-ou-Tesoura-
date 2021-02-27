import random 
from time import sleep

cor1 = '\33[1;32m' 
cor0 = '\33[m'

combate_imagem = ('''


     ┌─┬─┐─┬─┐            
     │▒│▒|▒│▒│           
    ┌┴─┴─┐-┘─┘           
    │▒┌──┘▒▒▒│           
    └┐▒▒▒▒▒▒┌┘            
    　└┐▒▒▒▒┌┘
''',
''' 

      ┌─┌─┬─┐            
      │▒│▒|▒│─┐          
      │▒│▒|▒│▒│         
      │▒│▒|▒│▒│          
     ┌┴─┴─┐-┘─┘        
     │▒┌──┘▒▒▒│          
     └┐▒▒▒▒▒▒┌┘          
      └┐▒▒▒▒┌┘            
''' 
,'''

        ┌─┐　─┐
        │▒│ /▒/
        │▒│/▒/
        │▒ /▒/─┬─┐ 
        │▒│▒|▒│▒│
        │▒┌──┘▒▒▒│
        └┐▒▒▒▒▒▒┌┘
          └┐▒▒▒▒┌

''')

vs = (''' 



                 ⎯⎯      
          ╲  /  │⎯⎯                
           ╲/   ⎯⎯│            
                

''')
def regras(): 
    
    print(22*'                                                                                                                            ')
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
                                                                                            
def combate():

    c = computador-1
    j = jogador-1
    print(''' 
    
    MAQUINA: 
    {1}

    {2} 

    JOGADOR:
    {0}
    
    
    
    
    
    '''.format(combate_imagem[(j)],combate_imagem[(c)],vs))

def resultado_imagem(): 
    print('''
    
    
  -=-=-=-=-=-=-=-=-=-=-=-=-=

    {0}   
    
  -=-=-=-=-=-=-=-=-=-==-=-=  
    
    
    '''.format(resultado))

    
    
    
sair = False

while sair != True:

    sleep(4)
    regras() 

    jogadas = ['Pedra','Papel','Tesoura']

    jogador = int(input('----> '))
    confere_jogador = jogadas[(jogador-1)]

    computador = random.randint(1,3) 
    confere_computador = jogadas[(computador-1)]

    


    if jogador  == computador:
        resultado = ('\33[1;33m Empate 👌 \33[m')
        combate()
        sleep(3)
        resultado_imagem()

    elif jogador == 3:
        if computador == 1:
            resultado = ('\033[1;31m você perdeu!\033[m')
            combate()
            sleep(2)
            resultado_imagem()
        elif computador == 2:
            print('\33[0;32m Você ganhou! 🏆 \33[m')
            combate()
            sleep(2)
            resultado_imagem()

    elif jogador == 2:
        if computador == 1:
            resultado = ('\33[0;32m Você ganhou! 🏆 \33[m')
            combate()
            sleep(2)
            resultado_imagem()

        elif computador == 3:
            resultado = ('\33[1;31m Você perdeu! 👎 \33[m')
            combate()
            sleep(2)
            resultado_imagem()

    elif jogador == 1:
        if computador == 2:
            resultado = ('\33[1;31m Você perdeu! 👎\33[m')
            combate()
            sleep(2)
            resultado_imagem()

        elif computador == 3:
            resultado = ('\33[0;32m Você ganhou! 🏆 \33[m')
            combate()
            sleep(2)
            resultado_imagem()

    elif jogador == 0:
        print('Saindo ⌛..')
        sleep(3)
        print('Jogo finalizado')
        break
                    



                  