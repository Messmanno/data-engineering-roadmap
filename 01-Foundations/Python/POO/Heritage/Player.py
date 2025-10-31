class Player:
    def __init__(self, pseudo,health,attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print(f"Bienvenue {pseudo}, point d'attaque : {attack} et vie : {health}")

    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack

    def damage(self,damage):
        self.health = self.health - damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)

player1 = Player("Manno",100,3)
player1.damage(5)
print(player1.get_pseudo(),player1.get_health())