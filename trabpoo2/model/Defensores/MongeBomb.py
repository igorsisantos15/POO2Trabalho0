from model.Guerreiro import Guerreiro

from model.Defensores import Defensor


class MongeBomb(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'MongeBomb'
        self.nacao = 'India'

    def defender(self, guerreiro, ofensores, defensores, ofensoresAdversarios):
        print "Energia: %" %self.getEnergia(self)
        print "%s (%s) DEFENDE!" %(self.getNome(self),self.getTipo(self))
        print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
        self.setEnergia(self,0)
        if self.getEnergia()<=0:
            print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
            defensores.remove(self)
        guerreiro.setEnergia(self,1)

