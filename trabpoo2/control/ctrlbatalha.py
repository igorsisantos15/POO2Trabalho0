from model.Batalha import Batalha
from view import GerarResultado
class CtrlBatalha(object):

    def iniciarBatalha(self):

        batalha = Batalha()
        gerarResultado = GerarResultado()
        batalha.carregar()
        batalha.imprimir()
        batalha.lutar(self)
        gerarResultado.imprimir()


