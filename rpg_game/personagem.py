class Personagem():
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def perde_vida(self):
        self.health -= 10
        self.health = health