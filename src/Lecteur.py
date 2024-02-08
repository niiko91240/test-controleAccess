class Lecteur:
    def __init__(self, badge_detecte=False):
        self.badge_detecte = badge_detecte

    def detecter_badge(self):
        self.badge_detecte = True