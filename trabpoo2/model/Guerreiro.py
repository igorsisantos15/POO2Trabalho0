__author__ = 'Italo'


class Guerreiro (object):
    __nome = None
    __idade = None
    __peso = None
    __energia = 100
    __tipo = None

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def getNome(self):
        return self.__peso

    def setNome(self, nome):
         self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
         self.__idade = idade

    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
         self.__peso = peso

    def getEnergia(self):
        return self.__energia

    def setEnergia(self, energia):
         self.__energia = energia

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
         self.__tipo = tipo

    def toString(self):
        return "Tipo %s => %s - Idade: %d - Peso: %d - Energia: %d" %(self.getTipo(),self.getNome(),self.getIdade(),self.getPeso(),self.getEnergia())






