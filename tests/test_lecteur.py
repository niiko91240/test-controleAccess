import unittest
from src.Lecteur import Lecteur
from src.MoteurOuverture import MoteurOuverture
from src.Porte import Porte


class TestMain(unittest.TestCase):

    def test_detecter_badge(self):
        # ETANT DONNE un lecteur ayant détecté un badge
        lecteur = Lecteur()
        lecteur.detecter_badge()
        # ET une porte lui étant liée
        porte = Porte()
        moteur = MoteurOuverture(porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger(lecteur)
        # ALORS cette porte s'ouvre
        self.assertTrue(lecteur.badge_detecte)



if __name__ == '__main__':
    unittest.main()