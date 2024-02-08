from src.Lecteur import Lecteur


class Porte:

    def __init__(self, statut_ouverture=False):
        self.statut_ouverture = statut_ouverture

    def ouvrir(self):
        self.statut_ouverture = True