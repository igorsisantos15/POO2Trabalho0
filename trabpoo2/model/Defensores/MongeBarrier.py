from model.Guerreiro import Guerreiro

from model.Defensores import Defensor


class MongeBarrier(Defensor):
    __sobrenome = None
    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'MongeBarrier'
        self.nacao = 'India'
        self.__parteNome = None
        self.__nivelEnergetico = 100

    def getParteNome(self):
        return self.__parteNome

    def setParteNome(self,parteNome):
        self.__parteNome = parteNome

    def getNivelEnergetico(self):
        return self.__nivelEnergetico

    def setNivelEnergetico(self,nivelEnergetico):
        self.__nivelEnergetico = nivelEnergetico

    def defender(self, guerreiro, ofensores, defensores, ofensoresAdversarios):
        print "Energia: %" %self.getEnergia(self)
        print "%s (%s) DEFENDE!" %(self.getNome(self),self.getTipo(self))
        if (self.getEnergia() <= 0) and (self.getNivelEnergetico() != 1):
            self.__meiaEnergia = None
            __meiaEnergia = self.__nivelEnergetico /2
            for i in range(2):
                nome = "MongeBarrierGerado" + self.__sobrenome
                self.__parteNome = self.__parteNome + 1
                self.__sobrenome = self.__parteNome
                self.__nome = self.__nome + self.__sobrenome
                mongeBarrier = MongeBarrier(nome,self.getIdade(), self.getPeso())
                mongeBarrier.setNivelEnergetico(self,self.__meiaEnergia)
                defensores.add(mongeBarrier)
            print "%s (%s) Morreu" %(self.getNome(),self.getTipo())
            defensores.remove(self)
            for p in defensores:
                print defensores.toString()
        if(self.getEnergia()<=0):
            defensores.remove(self)
        print "Energia pos defesa: %d" %self.getEnergia(self)
