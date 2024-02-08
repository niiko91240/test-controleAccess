from .Lecteur import Lecteur
from .Porte import Porte

class MoteurOuverture:
    def __init__(self, porte: Porte):
        self._porte = porte
    def interroger(self, lecteur):
        if lecteur.badge_detecte and not lecteur.bloque:
            self._porte.ouvrir()