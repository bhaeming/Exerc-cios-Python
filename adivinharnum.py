from time import sleep
from random import randint
tentativa=0
computador = randint(0,10)
print('Vou pensar em um número de 0 a 10')
sleep(1)
print('Pensando....')
sleep(1)
acertou = False
while not acertou:
    tentativa += 1
    jogador = int(input('Qual número eu pensei?'))
    if jogador == computador:
       acertou = True
       print('Parabéns, você acertou, utilizando {} tentativas'.format(tentativa))
    elif jogador > computador:
       print('É menor que {}'.format(jogador))
    else:
       print('É maior que {}'.format(jogador))