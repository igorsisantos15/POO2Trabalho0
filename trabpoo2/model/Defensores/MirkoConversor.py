from model.Guerreiro import Guerreiro

from model.Defensores import Defensor
from model.Ofensores import Gunte

class MirkoConversor(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'MirkoConversor'
        self.nacao = 'China'

    def defender(self, guerreiro, ofensores, defensores, ofensoresAdversarios):

        print "Energia: %" %self.getEnergia(self)
        print "%s (%s) DEFENDE!" %(self.getNome(self),self.getTipo(self))

        if guerreiro.getTipo(self) == "Samurai":
            print "% se transforma em Gun Te" %guerreiro.getNome(self)
            gunte = Gunte(self.getNome(), self.getIdade(), self.getPeso());
            ofensores.add(gunte)
            guerreiro.getEnergia(self,0)
            ofensoresAdversarios.remove(self)


        guerreiro.setEnergia(self,self.getEnergia(self)-2)

        print "Energia pos defesa: %d" %self.getEnergia(self)

        if guerreiro.getEnergia(self) <= 0:
            print "%s (%s) morreu" %(self.getNome(self),self.getTipo(self))
            defensores.remove(self)