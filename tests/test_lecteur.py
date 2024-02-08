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
        self.assertTrue(porte.statut_ouverture)

    def test_detecter_badge_wrong(self):
        # ETANT DONNE un lecteur n'ayant pas détecté un badge
        lecteur = Lecteur()
        # ET une porte lui étant liée
        porte = Porte()
        moteur = MoteurOuverture(porte)
        # QUAND le moteur interroge le lecteur
        moteur.interroger(lecteur)
        # ALORS cette porte ne s'ouvre pas
        self.assertFalse(porte.statut_ouverture)

    def test_detecter_badge_double_portes(self):
        # ETANT DONNE un lecteur ayant détecté un badge
        lecteur = Lecteur()
        lecteur.detecter_badge()
        # ET deux portes lui étant liées
        porte = Porte(lecteur)
        porte2 = Porte(lecteur)
        moteur = MoteurOuverture(porte)
        moteur2 = MoteurOuverture(porte2)
        # QUAND les moteurs interrogent le lecteur
        moteur.interroger(lecteur)
        moteur2.interroger(lecteur)
        # ALORS ces deux portes s'ouvrent
        self.assertTrue(porte.statut_ouverture)
        self.assertTrue(porte2.statut_ouverture)

    def test_detecter_badge_bloque(self):
        # ETANT DONNE un lecteur ayant détecté un badge bloqué
        lecteur = Lecteur(True)
        lecteur.detecter_badge()
        # ET une porte lui étant liée
        porte = Porte()
        moteur = MoteurOuverture(porte)
        # QUAND le moteur d'ouverture interroge ce lecteur
        moteur.interroger(lecteur)
        # ALORS cette porte ne s'ouvre pas
        self.assertFalse(porte.statut_ouverture)



if __name__ == '__main__':
    unittest.main()