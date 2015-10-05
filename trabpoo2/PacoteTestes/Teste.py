from model.Defensores.MangaldeDefesa import MangaldeDefesa
from model.Ofensores.Chunku import Chunku
__author__ = 'Italo'

from model.cgd.DAONacao import DAONacao

__author__ = 'Italo'

class Testes(object):

    def testeCriarLutador(self,nome, idade, peso):

        lutador = Chunku(nome,idade,peso)
        print lutador.getNomeNacao()
        print lutador.getNome()
        print lutador.getIdade()
        print lutador.getPeso()
        print lutador.getTipo()
        print 'Lutador Criado com sucesso'

    def testeCriarDefensor(self,nome, idade, peso):

        defensor = MangaldeDefesa(nome,idade,peso)
        print defensor.getNomeNacao()
        print defensor.getNome()
        print defensor.getIdade()
        print defensor.getPeso()
        print defensor.getTipo()
        print 'Defensor Criado com sucesso'

    def testeLeitura(self):
        daoNacao = DAONacao()
        list1 = daoNacao.leituraAtacantes(daoNacao.getArquivo1())
        print len(list1)
        if(len(list1)>0):
            print 'LEITURA REALIZADA'

