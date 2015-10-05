from random import randint
from model.cgd.DAONacao import DAONacao
from model.Nacao import Nacao
from view.Telabatalha import TelaBatalha

__author__ = 'Italo'


class Batalha(object):

    __nacao1 = None
    __nacao2 = None


    def __init__(self):
        self.__nacao1 = Nacao()
        self.__nacao2 = Nacao()

    def carregar(self):

        daoNacao = DAONacao()

        self.__nacao1.setNome(daoNacao.leituraNome(daoNacao.getArquivo1()))
        self.__nacao2.setNome(daoNacao.leituraNome(daoNacao.getArquivo2()))

        self.__nacao1.setOfensores(daoNacao.leituraAtacantes(daoNacao.getArquivo1()))
        self.__nacao2.setOfensores(daoNacao.leituraAtacantes(daoNacao.getArquivo2()))

        self.__nacao1.setDefensores(daoNacao.leituraDefensores(daoNacao.getArquivo1()))
        self.__nacao2.setDefensores(daoNacao.leituraDefensores(daoNacao.getArquivo2()))




    def lutar(self):

        sorteio = randint(1,2)
        vezAtaque = None


        if sorteio == 1:
            vezAtaque = 1
        else:
            vezAtaque = 2

        while self.__nacao1.sizeOfensor()!= 0 and self.__nacao1.sizeDefensores()!=0 and self.__nacao2.sizeOfensor()!=0 and self.__nacao2.sizeDefensores()!=0:


            if vezAtaque == 1:

                nacaoAtaque = self.__nacao1
                nacaoDefesa = self.__nacao2
                ofensor = self.__nacao1.getLutador()
                ofensoresAtacantes = self.__nacao1.getOfensores()
                defensoresAtacantes = self.__nacao1.getDefensores()

                ofesoresDefesa = self.__nacao2.getOfensores()
                defensoresDefesa = self.__nacao2.getDefensores()
                defensor = self.__nacao2.getDefensor()

                proxAtaque = 2

            else:

                nacaoAtaque = self.__nacao2
                nacaoDefesa = self.__nacao1
                ofensor = self.__nacao2.getLutador()
                ofensoresAtacantes = self.__nacao2.getOfensores()
                defensoresAtacantes = self.__nacao2.getDefensores()

                ofesoresDefesa = self.__nacao1.getOfensores()
                defensoresDefesa = self.__nacao1.getDefensores()
                defensor = self.__nacao1.getDefensor()

                proxAtaque = 1


            while defensor.getEnergia()>0 and len(ofensoresAtacantes)>0:
                ofensor.atacar(defensor,ofensoresAtacantes,defensoresAtacantes,defensoresDefesa)
                defensor.defender(ofensor,defensoresDefesa,ofesoresDefesa,ofensoresAtacantes)

                print ofensor.getEnergia()

                if(ofensor.getEnergia()>0):
                    nacaoAtaque.adcionarOfensor(ofensor)
                    ofensor = None

                ofensor = nacaoAtaque.getLutador()

            vezAtaque = proxAtaque

    def gerarResultados(self):

        tela = TelaBatalha()
        empate = 0


        if self.__nacao1.sizeOfensor() == 0 and self.__nacao2.sizeDefensores() == 0 or self.__nacao2.sizeOfensor() == 0 and self.__nacao1.sizeDefensores() == 0:
            tela.menssagem("EMPATE - A PAZ REINOU")

            empate = 1


        if self.__nacao1.sizeOfensor() == 0 and empate == 0:

            tela.menssagem("A nacao vencedora foi %s" %self.__nacao2.getNome())
            tela.menssagem("A nacao perdedora foi %s" %self.__nacao1.getNome())
            tela.menssagem("Acabaram os guerreiros ofensores")

        if self.__nacao1.sizeDefensores() == 0 and empate == 0:
            tela.menssagem("A nacao vencedora foi: %s" %self.__nacao2.getNome())
            tela.menssagem("A nacao perdedora foi: %s"%self.__nacao1.getNome())
            tela.menssagem("Acabaram os guerreiro defensores")

        if self.__nacao2.sizeOfensor == 0 and empate == 0:
            tela.menssagem("A nacao vencedora foi: %s" %self.__nacao1.getNome())
            tela.menssagem("A nacao perdedora foi: %s"  %self.__nacao2.getNome())
            tela.menssagem("Acabaram os guerreiro ofensores")

        if self.__nacao2.sizeDefensores() == 0 and empate == 0:
            tela.menssagem("A nacao vencedora foi: %s" %self.__nacao1.getNome())
            tela.menssagem("A nacao perdedora foi: %s"  %self.__nacao2.getNome())
            tela.menssagem("Acabaram os guerreiro defensores")






