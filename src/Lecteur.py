class Lecteur:
    def __init__(self, badge_detecte=False, bloque=False):
        self.badge_detecte = badge_detecte
        self.bloque = bloque

    def detecter_badge(self):
        self.badge_detecte = True

    def bloquer(self):
        self.bloque = True
        
    def debloquer(self):
        self.bloque = False