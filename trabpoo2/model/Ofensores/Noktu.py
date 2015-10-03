from model.Guerreiro import Guerreiro
from model.Defensores import MangaldeDefesa
import Ofensor.py


class Noktu(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso)
        self.tipo = 'Noktu'
        self.nacao = 'China'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        print "Energia: %s"  %self.getEnergia()
        print "%s (%s) ATACA!" %self.getNome(self),self.getTipo(self)
        guerreiro.setEnergia(self, guerreiro.getEnergia()-5)
        nome = "MangalGerado" + self.__sobrenome
        self.__parteNome = self.__parteNome + 1
        self.__sobrenome = self.__parteNome
        self.__nome = self.__nome + self.__sobrenome
        __idade = 30
        __peso = 90
        mangaldeDefesa = MangaldeDefesa(nome,self.__idade,self.__peso)
        defensores.add(mangaldeDefesa)
        print "defensor gerado: %s %s" %(defensores.getLast(),defensores.toString())
        if self.getEnergia()<=0:
            print "%s (%s) Morreu" %(self.getNome(self),self.getTipo(self))
            ofensores.remove(self)



