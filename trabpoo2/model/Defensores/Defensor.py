
from model.Guerreiro import Guerreiro

__author__ = 'Italo'


class  Defensor (Guerreiro):

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        raise NotImplementedError("Ofensores devem implementar Atacar")
