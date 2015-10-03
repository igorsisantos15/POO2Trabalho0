__author__ = 'IGOR'
__author__ = 'IGOR'

__author__ = 'IGOR'
__author__ = 'IGOR'

class GerarResultado:
     __empate = 0
     __ofensores_nacao1 = None
     __ofensores_nacao2 = None
     __defensores_nacao1 = None
     __defensores_nacao2 = None
     __nomeNacao1 = None
     __nomeNacao2 = None
     __mortoOfensoresNacao1 = None
     __mortoDefensorNacao1 = None
     __mortoOfensoresNacao2 = None
     __mortoDefensorNacao2 = None
     def __init__ (self,ofensores_nacao1, ofensores_nacao2,nomeNacao1, nomeNacao2, defensores_nacao1, defensores_nacao2, mortoOfensoresNacao1,mortoDefensorNacao1 , mortoOfensoresNacao2 ,mortoDefensorNacao2):
        self.__empate = 0
        self.__ofensores_nacao1 = ofensores_nacao1
        self.__ofensores_nacao2 = ofensores_nacao2
        self.__defensores_nacao1 = defensores_nacao1
        self.__defensores_nacao2 = defensores_nacao2
        self.__nomeNacao1 = nomeNacao1
        self.__nomeNacao2 = nomeNacao2
        self.__mortoOfensoresNacao1 = mortoOfensoresNacao1
        self.__mortoDefensorNacao1 =  mortoDefensorNacao1
        self.__mortoOfensoresNacao2 = mortoOfensoresNacao2
        self.__mortoDefensorNacao2 = mortoDefensorNacao2
     def imprimir(self):
        if self.__ofensores_nacao1.size() == 0 and self.__defensores_nacao2.size() == 0:
            print "CASO RARO: EMPATE NA GUERRA! E A PAZ REINOU..."
            GerarResultado.empate = 1
        if self.__ofensores_nacao2.size() == 0 and self.defensores_nacao1.size() == 0:
            print "CASO RARO: EMPATE NA GUERRA! E A PAZ REINOU..."
            GerarResultado.__empate = 1
        if self.__ofensores_nacao1.size() == 0 and self.__empate == 0:
            print "A nacao vencedora foi: %s" %self.__nomeNacao2
            print  "A nacao perdedora foi: %s" %self.__nomeNacao1
            print "Acabaram os guerreiro ofensores"
            print "O membro da nação vencedora que transferiu o último ataque foi: %s" + self.__defensores_nacao2.getFirst().toString()
            print "O último membro da nação perdedora foi: %s " + self.__mortoOfensoresNacao1.toString()
        if self.__ofensores_nacao1.size() == 0 and self.__empate == 0:
            print "A nacao vencedora foi: %s" %self.__nomeNacao2
            print  "A nacao perdedora foi: %s" %self.__nomeNacao1
            print "Acabaram os guerreiro defensores"
            print "O membro da nação vencedora que transferiu o último ataque foi: %s" %self.__ofensores_nacao2.getFirst().toString()
            print "O último membro da nação perdedora foi: %s " %self.__mortoDefensorNacao1.toString()
        if self.__ofensores_nacao2.size() == 0 and self.__empate == 0:
            print "A nacao vencedora foi: %s" %self.__nomeNacao1
            print  "A nacao perdedora foi: %s" %self.__nomeNacao2
            print "Acabaram os guerreiro ofensores"
            print "O membro da nação vencedora que transferiu o último ataque foi: %s" %self.__defensores_nacao1.getFirst().toString()
            print "O último membro da nação perdedora foi: %s "  %self.__mortoOfensoresNacao2.toString()
        if self.__ofensores_nacao2.size() == 0 and self.__empate == 0:
            print "A nacao vencedora foi: %s" %self.__nomeNacao1
            print  "A nacao perdedora foi: %s" %self.__nomeNacao2
            print "Acabaram os guerreiro defensores"
            print "O membro da nação vencedora que transferiu o último ataque foi: %s" %self.__ofensores_nacao1.getFirst().toString()
            print "O último membro da nação perdedora foi: %s " %self.__mortoDefensorNacao2.toString()


