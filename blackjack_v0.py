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


# cria classe banca
class Banca(ec.Jogador):
    def __init__(self):
        self.nome = 'Banca'
        self.banco = 0
    
    def mostrar_mao_banca(self):
        return (f'A carta da {self.nome}: {self.mao[0].exibir()}')
          # exibe apenas a primeira carta da mao
    
    def mostrar_pontos_banca(self):
        return (f'Pontos da {self.nome}: {self.mao[0].pontos}')
    
    def mostrar_pontos_bj(self):
        self.pontos_mao = 0
        for carta in self.mao:
            if carta.valor == 'as': # se a carta e um as tem dois valores, [1, 11]
                if self.pontos_mao < 22:
                    self.pontos_mao += carta.pontos[1]
                else:
                    self.pontos_mao += carta.pontos[0]
            else:
                self.pontos_mao += carta.pontos
        return (f'Pontos de {self.nome}: {self.pontos_mao}')
    

class Jogador(ec.Jogador):
    def mostrar_pontos_bj(self):
        self.pontos_mao = 0
        for carta in self.mao:
            if carta.valor == 'as': # se a carta e um as tem dois valores, [1, 11]
                if self.pontos_mao <= 21:
                    self.pontos_mao += carta.pontos[1]
                else:
                    self.pontos_mao += carta.pontos[0]
            else:
                self.pontos_mao += carta.pontos
        return (f'Pontos de {self.nome}: {self.pontos_mao}')


# Inicializacao do jogo
print('BlackJack')
print('~~~ Bem vindo ao canto mais animado da CLI ~~~')
print('Jogo de BlackJack contra a banca, usando 4 baralhos\nA casa paga 3:2')
nome_jogador = input(f'Qual o nome do jogador? ')
jogador1 = Jogador(nome_jogador, 1000)  # cria o jogador
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

n_jogada = 1
aposta_minima = 10
esta_jogando = True
while esta_jogando:
    n_jogada += 1
    aposta_jogador = 0
    print(f'Voce possui {jogador1.banco} creditos.')
    print(f'A aposta minima para esta rodada e {aposta_minima} creditos')
    while aposta_jogador < aposta_minima:
        aposta_jogador = int(input('Qual e sua aposta? '))
    jogador1.apostar(aposta_jogador)
    print('Apostas encerradas. As maos serao distribuidas agora.\nCada jogador recebera 2 cartas.')

    jogador1.pegar_cartas(2, deck)
    casa.pegar_cartas(2, deck)


    print(casa.mostrar_mao_banca())
    print(casa.mostrar_pontos_banca())
    casa.mostrar_pontos_bj()  # sem o print nao retorna nada e contabiliza os pontos
    print(jogador1.mostrar_mao())
    print(jogador1.mostrar_pontos_bj())

    jogada = 1  # seta jogada
    while True:
        jogada = int(input('''Defina sua jogada:
        1 - Parar
        2 - Desistir
        3 - Dobrar
        4 - Pedir
        5 - Sair
        Sua jogada:'''))
        if jogada == 1:
            break
        elif jogada == 2:
            print(casa.mostrar_mao())
            print(casa.mostrar_pontos_bj())
            print(jogador1.mostrar_banco())
            jogador1.limpar_mao()
            casa.limpar_mao()
            break
        elif jogada == 3:
            jogador1.apostar(aposta_jogador)
            aposta_jogador += aposta_jogador
            print(f'A aposta agora e de {aposta_jogador}')
            jogador1.adicionar_cartas_mao(deck)
            print(jogador1.mostrar_mao())
            print(jogador1.mostrar_pontos_bj())
        elif jogada == 4:
            jogador1.adicionar_cartas_mao(deck)
            print(jogador1.mostrar_mao())
            print(jogador1.mostrar_pontos_bj())
        elif jogada == 5:
            esta_jogando = False
            break

        if jogador1.pontos_mao > 21:  # retira o jogador do loop e joga pro proximo pra finalizar o jogo
            break
        

    while True:
        if jogada == 2 or jogada == 5:
            break
        elif jogador1.pontos_mao > 21:  # se o jogador estorou
            print('Estourou! Voce perdeu a jogada.')
            print(casa.mostrar_mao())
            jogador1.limpar_mao()
            print(jogador1.mostrar_banco())
            break
        print(casa.mostrar_mao())
        print(casa.mostrar_pontos_bj())
        while casa.pontos_mao <= 16:  # enquanto a casa nao chegar a 16 pontos
            casa.adicionar_cartas_mao(deck)
            print(casa.mostrar_mao())
            print(casa.mostrar_pontos_bj())  # mostra automaticamente a mao e os pontos ate a condicao ser obedecida
        if casa.pontos_mao > 21 and jogador1.pontos_mao <= 21:  # se a casa estorou e o jogador nao
            aposta_jogador = aposta_jogador * 1.5
            print(f'A {casa.nome} estorou!')
            print(f'Voce ganhou {aposta_jogador}.')
            jogador1.ganhar(aposta_jogador)
            print(jogador1.mostrar_banco())
        elif (casa.pontos_mao == jogador1.pontos_mao) or (casa.pontos_mao > 21):  # se ambos empataram ou estouraram
            print(f'Empate')
            print(casa.mostrar_mao())
            print(casa.mostrar_pontos_bj())
            jogador1.ganhar(aposta_jogador)
            break
        elif casa.pontos_mao < jogador1.pontos_mao:  # se o jogador ganhou
            aposta_jogador = aposta_jogador * 1.5
            print(f'Voce ganhou!')
            print(f'Voce ganhou {aposta_jogador} creditos.')
            jogador1.ganhar(aposta_jogador)
            print(jogador1.mostrar_banco())
        elif casa.pontos_mao > jogador1.pontos_mao :  # se a casa ganhou
            print(f'Voce perdeu!')
            print(casa.mostrar_mao())
            print(casa.mostrar_pontos_bj())
            break
        print('A jogada acabou.')
        print(jogador1.mostrar_banco())
        break
    if jogador1.banco <= 0:
        print(f'O jogo terminou. O jogador {jogador1.nome} esta sem dinheiro.')
        print(f'Foram jogadas {n_jogada} rodadas.')
        break
    elif len(deck.cartas) < 11:
        print(f'O jogo terminou. Nao ha cartas suficientes para mais uma jogada.')
        print(f'Foram jogadas {n_jogada} rodadas.')
        print(jogador1.mostrar_banco())
        break
    else:
        jogador1.limpar_mao()
        casa.limpar_mao()
        continue

# TODO: programar o sistema de apostas, usar função ou classe?
# TODO: programar o comportamento da banca dependendo do comportamento do jogador
# TODO: condicoes de ganhar ou perder
# TODO: condicoes de final de jogo