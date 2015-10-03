__author__ = 'Italo'

import Guerreiro.py
import Leitor.py

class Nacao(object):
    __ofensores = []
    __defensores = []
    __nomeNacao = None
    def __init__(self, arq):

        self.__ofensores = leitor.carregaOfensores(arq);
        self.__defensores = leitor.carregaDefensores(arq);
    def getNome(self):
        return self.__nomeNacao
    def setNome(self,nomeNacao):
        self.__nomeNacao = nomeNacao
