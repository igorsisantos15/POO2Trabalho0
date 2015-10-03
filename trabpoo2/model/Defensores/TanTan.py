from model.Guerreiro import Guerreiro
from model.Ofensores.Ninja import Ninja
from model.Defensores import Defensor


class TanTan(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'Tantan'
        self.nacao = 'Japao'

    def defender(self, guerreiro, ofensores, defensores, ofensoresAdversarios):
        print "Energia: %" %self.getEnergia(self)
        print "%s (%s) DEFENDE!" %(self.getNome(self),self.getTipo(self))
        if self.getEnergia<=0:
            ninja = Ninja(self.getNome(),self.getIdade(),self.getPeso())
            ofensores.add(ninja)
            print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
            print "%s se transformou em ninja"
            defensores.remove(self)


