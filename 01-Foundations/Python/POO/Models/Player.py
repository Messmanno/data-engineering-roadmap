class Player:
    def __init__(self, pseudo,health,attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
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
        damage = self.attack
        # si le joueur a une arme
        if self.hasWeapon():
            damage += self.weapon.get_damage_amount()

        target_player.damage(damage)

    #méthode pour changer l'arme d'un joueur
    def set_weapon(self, weapon):
        self.weapon = weapon

    # méthode pour verifier si le joueur a une arme
    def hasWeapon(self):
        return self.weapon is not None