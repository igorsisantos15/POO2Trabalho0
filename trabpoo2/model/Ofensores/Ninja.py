from model.Guerreiro import Guerreiro


import Ofensor.py

class Ninja(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'Ninja'
        self.nacao = 'Japão'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        print "Energia: %s"  %self.getEnergia()
        print "%s (%s) ATACA!" %self.getNome(self),self.getTipo(self)
        guerreiro.setEnergia(self,guerreiro.getEnergia()-20)
