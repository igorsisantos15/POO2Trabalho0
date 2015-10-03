from model.Guerreiro import Guerreiro

from model.Ofensores.Ofensor import Ofensor

class Chunku(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'Chunku'
        self.nacao = 'China'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        print "Energia: %s"  %self.getEnergia()
        print "%s (%s) ATACA!" %self.getNome(self),self.getTipo(self)
        if guerreiro.getNomeNacao(self) == "India":
            guerreiro.setEnergia(self,guerreiro.getEnergia(self)-5)
        if guerreiro.getNomeNacao(self) == "Japao":
            guerreiro.setEnergia(self,guerreiro.getEnergia(self)-10)

        if self.getEnergia(self) <= 0:
           print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
           ofensores.remove(self)


