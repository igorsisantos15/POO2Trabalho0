__author__ = 'Italo'



class Nacao(object):
    __nome = None
    __ofensores = []
    __defensores = []


    def setOfensores(self, ofensores):
        self.__ofensores = ofensores

    def setDefensores(self, defensores):
        self.__defensores = defensores

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
