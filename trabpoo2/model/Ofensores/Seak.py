from model.Guerreiro import Guerreiro

from model.Ofensores.Ofensor import Ofensor


class Seak(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'Seak'
        self.nacao = 'India'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        print "Energia: %s"  %self.getEnergia()
        print "%s (%s) ATACA!" %self.getNome(self),self.getTipo(self)
        guerreiro.setEnergia(self,guerreiro.getEnergia()-25)
        if self.getEnergia()<=0:
            print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
            ofensores.remove(self)