# jogo blackjack
# 2020-04-18

import engine_cartas as ec
import random as r

# cria a classe deck de mesa partindo da engine_cartas.Baralho()
class DeckMesa(ec.Baralho):
    def __init__(self):
        self.cartas = []
    
    def combinar(self, baralho1, baralho2, baralho3, baralho4):
        self.baralhos = [baralho1.cartas, baralho2.cartas, baralho3.cartas, baralho4.cartas]
        for baralho in self.baralhos:
            for carta in baralho:
                self.cartas.append(carta)

    def corte(self):
        ponto_corte = r.randint(149,208)
        self.cartas = self.cartas[0:ponto_corte]
    
    def pontos(self):
        for carta in self.cartas:
            if carta.valor == 'as':
                carta.pontos = [1, 11]
            elif (carta.valor == '10') or (carta.valor == 'valete') or (carta.valor == 'dama') or (carta.valor == 'rei'):
                carta.pontos = 10
            else:
                carta.pontos = int(carta.valor)



class Banca(ec.Jogador):
    def __init__(self):
        self.nome = 'Banca'
        self.banco = 0
    
    def mostrar_mao_banca(self):
        return (f'A carta da {self.nome}: {self.mao[0].exibir()}')
          # exibe apenas a primeira carta da mao
    
    def mostrar_pontos_banca(self):
        return (f'Pontos da {self.nome}: {self.mao[0].pontos}')


# Inicializacao do jogo
print('BlackJack')
print('~~~ Bem vindo ao canto mais animado da CLI ~~~')
print('Jogo de BlackJack contra a banca, usando 4 baralhos')
nome_jogador = input(f'Qual o nome do jogador? ')
jogador1 = ec.Jogador(nome_jogador, 1000)  # cria o jogador
casa = Banca()  # cria a banca

#cria e inicializa o deck de cartas
brlh1 = ec.Baralho()
brlh2 = ec.Baralho()
brlh3 = ec.Baralho()
brlh4 = ec.Baralho()

deck = DeckMesa()
deck.combinar(brlh1, brlh2, brlh3, brlh4)
deck.embaralhar()
deck.corte()
deck.pontos()

# definir_pontos(deck.cartas)

while True:
    aposta_minima = 10

    aposta_jogador = 0
    print(f'A aposta minima para esta rodada e {aposta_minima} creditos')
    while aposta_jogador < aposta_minima:
        aposta_jogador = int(input('Qual e sua aposta? '))
    print('Apostas encerradas. As maos serao distribuidas agora.\n Cada jogador recebera 2 cartas.')

    jogador1.pegar_cartas(2, deck)
    casa.pegar_cartas(2, deck)

    print(casa.mostrar_mao_banca())
    print(casa.mostrar_pontos_banca())
    print(jogador1.mostrar_mao())
    print(jogador1.mostrar_pontos())

    jogada = input('''Defina sua jogada:\n
    1 - Parar\n
    2 - Desistir\n
    3 - Dobrar\n
    4 - Pedir
    ''')

    break
    
    
# carta1 = deck.cartas[0]
# print(carta1.valor)
# print(carta1.pontos)



# estao_jogando = True

# while estao_jogando:
#     print(f'Voce possui {jogador1.banco} creditos')
#     aposta = int(input('Quanto voce quer apostar?'))
#     jogador1.pegar_cartas(2)
#     casa.pegar_cartas(2)
#     jogador1.apostar(aposta)
#     casa.apostar()
# TODO: programar o sistema de apostas, usar função ou classe?
# TODO: programar o comportamento da banca dependendo do comportamento do jogador
# TODO: condicoes de ganhar ou perder
# TODO: condicoes de final de jogo