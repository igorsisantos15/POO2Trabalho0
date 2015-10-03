
from model.Ofensores import *
from model.Ofensores.Chunku import Chunku
from model.Ofensores.Gunte import Gunte
from model.Ofensores.Ninja import Ninja
"""from model.Ofensores.Noktu import Noktu"""
from model.Ofensores.Samurai import Samurai
from model.Ofensores.Seak import Seak

__author__ = 'Italo'


class DAONacao(object):
    __arquivo1 = 'nacao1.txt'
    __arquivo2 = 'nacao2.txt'

    def getArquivo1(self):
        return self.__arquivo1

    def getArquivo2(self):
        return self.__arquivo2

    def leituraAtacantes(self,arquivo):

        tipo = nome = idade = peso = None
        ofensores = []


        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        linha = ARQ.readline()
        linha = ARQ.readline()
        while (linha != 'Defensores\n'):

                print linha
                dados = linha.split(' ')
                print dados
                tipo = int(dados[0])
                nome = dados[1]
                idade = int(dados[2])
                peso = int(dados[3])

                if(nacao == 'China'):
                    if(tipo == 1):
                        print('oi')
                        chunku = Chunku(nome,idade,peso)
                        ofensores.append(chunku)
                    if(tipo == 2):
                        gunte = Gunte(nome,idade,peso)
                        ofensores.append(gunte)
                    """if(tipo == 3):
                        noktu = Noktu(nome,idade,peso)
                        ofensores.append()"""

                if(nacao == 'Japao'):
                    if(tipo == 1):
                        samurai = Samurai(nome,idade,peso)
                        ofensores.append(samurai)
                    if(tipo == 2):
                        ninja = Ninja(nome,idade,peso)
                        ofensores.append(ninja)

                if(nacao == 'India'):
                    if(tipo == 1):
                        seak = Seak(nome,idade,peso)
                        ofensores.append(seak)

                linha = ARQ.readline()

    def leituraNome(self, arquivo):

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        ARQ.close()
        return nacao