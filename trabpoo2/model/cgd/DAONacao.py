

from model.Ofensores.Chunku import Chunku
from model.Ofensores.Gunte import Gunte
from model.Ofensores.Ninja import Ninja
from model.Ofensores.Noktu import Noktu

"""from model.Ofensores.Noktu import Noktu"""
from model.Ofensores.Samurai import Samurai
from model.Ofensores.Seak import Seak

from model.Defensores.MangaldeDefesa import MangaldeDefesa
from model.Defensores.MirkoConversor import MirkoConversor
from model.Defensores.MongeBarrier import MongeBarrier
from model.Defensores.MongeBomb import MongeBomb
from model.Defensores.MongeLeaf import MongeLeaf
from model.Defensores.MontordoEscudo import MontordoEscudo
from model.Defensores.TanTan import TanTan

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

                dados = linha.split(' ')
                tipo = int(dados[0])
                nome = dados[1]
                idade = int(dados[2])
                peso = int(dados[3])

                if(nacao == 'China\n'):
                    if(tipo == 1):
                        chunku = Chunku(nome,idade,peso)
                        ofensores.append(chunku)
                    if(tipo == 2):
                        gunte = Gunte(nome,idade,peso)
                        ofensores.append(gunte)
                    if(tipo == 3):
                        noktu = Noktu(nome,idade,peso)
                        ofensores.append()

                if(nacao == 'Japao\n'):
                    if(tipo == 1):
                        samurai = Samurai(nome,idade,peso)
                        ofensores.append(samurai)
                    if(tipo == 2):
                        ninja = Ninja(nome,idade,peso)
                        ofensores.append(ninja)

                if(nacao == 'India\n'):
                    if(tipo == 1):
                        seak = Seak(nome,idade,peso)
                        ofensores.append(seak)

                linha = ARQ.readline()
        return ofensores

    def leituraDefensores(self, arquivo):

        tipo = nome = idade = peso = None
        defensores = []


        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        linha = ARQ.readline()
        linha = ARQ.readline()
        while (linha != 'Defensores\n'):
            linha = ARQ.readline()

        linha = ARQ.readline()
        while linha!= '\n' and linha!= '':

            dados = linha.split(' ')
            nome = dados[1]
            idade = int(dados[2])
            peso = int(dados[3])

            if(nacao == 'China\n'):
                if(tipo == 1):
                    mangalDeDefesa = MangaldeDefesa(nome,idade,peso)
                    defensores.append(mangalDeDefesa)
                if(tipo == 2):
                    montorDoEscudo = MontordoEscudo(nome,idade,peso)
                    defensores.append(montorDoEscudo)
                if(tipo == 3):
                    mirkOConversor = MirkoConversor(nome,idade,peso)
                    defensores.append(mirkOConversor)

            if(nacao == 'Japao\n'):
                if(tipo == 1):
                    tantan = TanTan(nome,idade,peso)
                    defensores.append(tantan)

            if(nacao == 'India\n'):
                if(tipo == 1):
                    mongeLeaf = MongeLeaf(nome,idade,peso)
                    defensores.append(mongeLeaf)
                if(tipo == 2):
                    mongeBomb = MongeBomb(nome,idade,peso)
                    defensores.append(mongeBomb)
                if(tipo == 3):
                    mongeBarrier = MongeBarrier(nome,idade,peso)
                    defensores.append(mongeBarrier)
            linha = ARQ.readline()

        return defensores

    def leituraNome(self, arquivo):

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        ARQ.close()
        return nacao