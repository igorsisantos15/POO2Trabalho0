from model.Guerreiro import Guerreiro

from model.Defensores import Defensor


class MontordoEscudo(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'MontordoEscudo'
        self.nacao = 'China'
        self.setEnergia(150)

    def defender(self, guerreiro, ofensores, defensores, ofensoresAdversarios):
        print "Energia: %" %self.getEnergia(self)
        print "%s (%s) DEFENDE!" %(self.getNome(self),self.getTipo(self))
        if self.getEnergia<=0:
            print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
            defensores.remove(self)
            guerreiro.setEnergia(self,0)
            ofensoresAdversarios.remove(guerreiro)
        if guerreiro.getNome() == "Dalai":
           for p in ofensoresAdversarios:
                print ofensoresAdversarios.toString()