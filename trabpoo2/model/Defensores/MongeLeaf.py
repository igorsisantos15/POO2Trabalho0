from model.Guerreiro import Guerreiro

from model.Defensores import Defensor


class MongeLeaf(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'MongeLeaf'
        self.nacao = 'India'

    def defender(self, guerreiro, ofensores, defensores, ofensoresAdversarios):
        print "Energia: %" %self.getEnergia(self)
        print "%s (%s) DEFENDE!" %(self.getNome(self),self.getTipo(self))
        if guerreiro.getTipo() == "Ninja":
            self.setEnergia(self,self.getEnergia()+ 20)
            guerreiro.setEnergia(self,guerreiro.getEnergia(self)-1)
        if guerreiro.getTipo() == "Chunku":
            self.setEnergia(self,self.getEnergia()+ 5)
            guerreiro.setEnergia(self,guerreiro.getEnergia(self)-1)
        print "Energia pos defesa: %d" %self.getEnergia(self)
        if self.getEnergia()<=0:
            print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
            defensores.remove(self)

