from model.cgd.DAONacao import DAONacao
from model.Nacao import Nacao
import  random


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

    def imprimir(self):
        print self.__nacao1


    def lutar(self,defensor,ofensor,defensorAdversario, ofensorAdversario,ofensores_nacao1,percorreOfensores2, defensores_nacao1, ofensores_nacao2, percorreDefensores, defensores_nacao2, percorreDefensores2):
        __sorteio = random.randint(0,2)
        __trocaAtaque = 2

        while ofensores_nacao1.size() != 0 and defensores_nacao1.size() != 0 and ofensores_nacao2.size() != 0 and defensores_nacao2.size() != 0:
            if (__sorteio == 0 or trocaAtaque == 0):
                trocaAtaque = 0
                while (self.ofensores_nacao1.size() != 0 and defensores_nacao1.size() != 0
                        and ofensores_nacao2.size() != 0 and defensores_nacao2.size() != 0
                        and trocaAtaque == 0):

                    defensorAdversario = percorreDefensores2.next()
                    __loop = 0
                    while ((defensorAdversario.getEnergia() > 0) and (ofensores_nacao1.size() > 0)):
                        percorreOfensores = ofensores_nacao1.iterator()
                        __loop = __loop + 1
                        if (ofensores_nacao1.size() == 1):
                            mortoOfensoresNacao1 = ofensores_nacao1.getFirst()
                        ofensor = percorreOfensores.next()
                        print "\<<<==== Ofensor: %s X Defensor: %s ===>>>" %(ofensor.getNome(),defensorAdversario.getNome())
                        ofensor.atacar(defensorAdversario, ofensores_nacao1, defensores_nacao1, defensores_nacao2)
                        defensorAdversario.defender(ofensor, defensores_nacao2, ofensores_nacao2, ofensores_nacao1)
                        if (ofensor.getEnergia() > 0):
                            ofensores_nacao1.addLast(ofensor)
                            ofensores_nacao1.removeFirst()
                    trocaAtaque = 1

                    percorreOfensores.hasNext
                    percorreDefensores.hasNext
                    percorreOfensores2.hasNext
                    percorreDefensores2.hasNext
            if (__sorteio == 1 or __trocaAtaque == 1):
                __trocaAtaque = 1;
                percorreOfensores = ofensores_nacao1.iterator()
                percorreDefensores = defensores_nacao1.iterator()
                percorreOfensores2 = ofensores_nacao2.iterator()
                percorreDefensores2 = defensores_nacao2.iterator()
                while (ofensores_nacao1.size() != 0 and defensores_nacao1.size() != 0 and ofensores_nacao2.size() != 0 and defensores_nacao2.size() != 0and trocaAtaque == 1):
                    defensorAdversario = percorreDefensores.next();
                    while ((defensorAdversario.getEnergia() > 0) and (ofensores_nacao2.size() > 0)):
                        percorreOfensores2 = ofensores_nacao2.iterator()
                        ofensor = percorreOfensores2.next()
                        if (ofensores_nacao2.size() == 1):
                            mortoOfensoresNacao2 = ofensores_nacao2.getFirst()
                        print "\<<<==== Ofensor: %s X Defensor: %s ===>>>" %(ofensor.getNome(),defensorAdversario.getNome())
                        ofensor.atacar(defensorAdversario, ofensores_nacao2, defensores_nacao2, defensores_nacao1)
                        defensorAdversario.defender(ofensor, defensores_nacao1, ofensores_nacao1, ofensores_nacao2)
                        if (ofensor.getEnergia() > 0):
                            ofensores_nacao2.addLast(ofensor)
                            ofensores_nacao2.removeFirst()
                    trocaAtaque = 0
                    percorreOfensores.hasNext()
                    percorreDefensores.hasNext()
                    percorreOfensores2.hasNext()
                    percorreDefensores2.hasNext()

            if ofensores_nacao1.size() == 1:
                mortoOfensoresNacao1 = ofensores_nacao1.getFirst()
            if defensores_nacao1.size() == 1:
                mortoDefensoresNacao1 = defensores_nacao1.getFirst()
            if (ofensores_nacao2.size() == 1):
                mortoOfensoresNacao2 = ofensores_nacao2.getFirst()
            if (defensores_nacao2.size() == 1):
                mortoDefensoresNacao2 = defensores_nacao2.getFirst()






