# engine de cartas com jogador, banca, cartas e baralho
# 2020-04-18

import random

class Jogador():
    def __init__(self, nome, banco):
        self.nome = nome
        self.banco = banco
    
    def pegar_cartas(self, qtd_cartas, Baralho):
        self.qtd_cartas = qtd_cartas
        self.mao = []
        for item in range(self.qtd_cartas):
            self.mao.append(Baralho.dar_carta())
    
    def adicionar_cartas_mao(self, Baralho):
        self.mao.append(Baralho.dar_carta())
    
    def apostar(self, valor_aposta):
        self.valor_aposta = valor_aposta
        self.banco -= self.valor_aposta
    
    def mostrar_mao(self):
        self.mao_rodada = []
        for carta in self.mao:
            self.mao_rodada.append(carta.exibir())
        return (f'As cartas de {self.nome}: {self.mao_rodada}')
    
    def limpar_mao(self):
        del self.mao[:]  # deleta o conteudo da lista
    
    def mostrar_pontos(self):
        self.pontos_mao = 0
        for carta in self.mao:
            self.pontos_mao += carta.pontos
        return (f'Pontos de {self.nome}: {self.pontos_mao}')
    
    def mostrar_banco(self):
        return (f'Creditos de {self.nome}: {self.banco}')
    
    def ganhar(self, total_aposta):
        self.total_aposta = total_aposta
        self.banco += self.total_aposta


class Carta():
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        self.pontos = 0
    
    def exibir(self):
        return f'{self.valor} de {self.naipe}'


class Baralho():
    def __init__(self):
        self.cartas = []
        self.naipes = ['paus', 'ouros', 'copas', 'espadas']
        self.valores = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valete', 'dama', 'rei']
        self.construir()

    def construir(self):
        for naipe in self.naipes:
            for valor in self.valores:
                self.cartas.append(Carta(valor, naipe))
    
    def _exibir(self):
        for item in self.cartas:
            item.exibir()
    
    def embaralhar(self):
        for item in self.cartas:
            self.posicao_antiga = self.cartas.index(item)  # indice da carta
            self.cartas.insert(random.randint(0,len(self.cartas)), self.cartas.pop(self.posicao_antiga))
            # substitui a carta em um local aleatorio
    
    def dar_carta(self):
        return self.cartas.pop()
