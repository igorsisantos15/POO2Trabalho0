__author__ = 'Italo'

import Nacao.py

class Batalha(object):

    __nacao1 = [];
    __nacao2 = [];


    def __init__(self, arq1, arq2):

        self.__nacao1 = Nacao(arq1);
        self.__nacao2 = Nacao(arq2);

    def lutar(self):
