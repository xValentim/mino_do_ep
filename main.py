from funcoes import *
import random

try:
    with open('text.txt', 'r', encoding='utf-8') as arquivo:
        texto_inicial = arquivo.read()
except:
    texto_inicial = 'Vamos começar!!'
print(texto_inicial)

num_de_jogadores = int(input('Quantos jogadores? (2-4)'))

continua = True
while continua:
    todas_as_pecas = cria_pecas()
    status_do_jogo = inicia_jogo(num_de_jogadores, todas_as_pecas)
    # Sorteia jogador inicial:
    i_0 = random.randint(0, num_de_jogadores - 1)
    sequencia_natural = list(range(num_de_jogadores))
    sequencia = sequencia_natural[i_0::] + sequencia_natural[0:i_0]
    while verifica_ganhador(status_do_jogo['jogadores']) == -1:
        for i in sequencia:
            # mostra a mesa
            print('MESA: ', status_do_jogo['mesa'])
            print('\n')
            if i == 0:
                continue
            else:
                continue

