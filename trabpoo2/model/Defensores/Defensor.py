
from model.Guerreiro import Guerreiro

__author__ = 'Italo'


class  Defensor (Guerreiro):

    def defender(self, guerreiro, ofensores, defensores, defensoresAdversarios ):
        raise NotImplementedError("Ofensores devem implementar Atacar")
