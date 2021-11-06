import random
def cria_pecas():
    pecas = []
    for i in range(7):
        for j in range(i, 7):
            pecas.append([i, j])
    random.shuffle(pecas)
    return pecas

def inicia_jogo(n, pecas):
    dicionario = {'jogadores':{}}
    for i in range(n):
        dicionario['jogadores'][i] = pecas[i*7:(i+1)*7]
        aux = list(pecas[(i+1)*7::])
    dicionario['monte'] = aux
    dicionario['mesa'] = []
    return dicionario

def verifica_ganhador(status):
    for jogador in status:
        if status[jogador] == []:
            return jogador
    return -1

def soma_pecas(pecas):
    pontos = 0
    for peca in pecas:
        pontos += peca[0] + peca[1]
    return pontos

def posicoes_possiveis(mesa, pecas):
    if mesa == []:
        return list(range(len(pecas)))
    possiveis = []
    pontas_da_mesa = [mesa[0][0], mesa[-1][1]]
    for i in range(len(pecas)):
        if pecas[i][0] in pontas_da_mesa or pecas[i][1] in pontas_da_mesa:
            possiveis.append(i)
    return possiveis

def adiciona_na_mesa(peca, mesa):
    if mesa == []:
        mesa = [peca]
        return mesa
    ponta_esquerda = mesa[0][0]
    ponta_direita = mesa[-1][1]
    if peca[1] == ponta_esquerda:
        mesa = [peca] + mesa
    elif peca[0] == ponta_esquerda:
        peca = [peca[1], peca[0]]
        mesa = [peca] + mesa
    elif peca[0] == ponta_direita:
        mesa = mesa + [peca]
    else:
        peca = [peca[1], peca[0]]
        mesa = mesa + [peca]
    return mesa
    