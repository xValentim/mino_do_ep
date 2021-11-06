from funcoes import *
import random

try:
    with open('text.txt', 'r', encoding='utf-8') as arquivo:
        texto_inicial = arquivo.read()
except:
    texto_inicial = 'Vamos começar!!'
print(texto_inicial)

num_de_jogadores = int(input('Quantos jogadores? (2-4)'))


