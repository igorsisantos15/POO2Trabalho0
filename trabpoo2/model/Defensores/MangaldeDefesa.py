
from model.Guerreiro import Guerreiro
from model.Defensores import Defensor


class MangaldeDefesa(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'MangaldeDefesa'
        self.nacao = 'China'


    def defender(self, guerreiro, ofensores, defensores, ofensoresAdversarios):
        print "Energia: %" %self.getEnergia(self)
        print "%s (%s) DEFENDE!" %(self.getNome(self),self.getTipo(self))

        guerreiro.setEnergia(self,self.getEnergia(self)-2)

        print "Energia pos defesa: %d" %self.getEnergia(self)

        if guerreiro.getEnergia(self) <= 0:
            print "%s (%s) morreu" %(self.getNome(self),self.getTipo(self))
            guerreiro.setEnergia(self,0)
            defensores.remove(self)
        for p in defensores:
            print defensores.toString()

