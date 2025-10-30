from Player import Player

class Warrior(Player):
    def __init__(self, pseudo,health,attack):
        super().__init__(pseudo,health,attack),
        # self.pseudo = pseudo
        # self.health = health
        # self.attack = attack
        self.armor = 0
        print(f"Bienvenue au guerrier{pseudo}, point d'attaque : {attack} et vie : {health}")

    # def get_pseudo(self):
    #     return self.pseudo
    # def get_health(self):
    #     return self.health
    # def get_attack(self):
    #     return self.attack
    def get_armor_point(self):
        return self.armor

    def damage(self,damage):
       if self.armor > 0:
           self.armor -= 1
           damage = 0
       super().damage(damage)

    #def attack_player(self, target_player):
    #    target_player.damage(self.attack)

    def blade(self):
        self.armor = 3
        print("Les points de l'armure ont été rechargés a 3")


#creation des deux guerriers
warrior1 = Warrior("Darkwarrior",100,3)
warrior2 = Warrior("Redwarrior",100,5)
#chargement de l'armure du guerrier warrior1
warrior1.blade()
#warrior2 attaque warrior1 qui a son armure chargé a bloc
print(warrior2.pseudo, warrior2.health,warrior2.armor,warrior2.attack)
print(warrior1.pseudo, warrior1.health,warrior1.armor,warrior1.attack)
warrior2.attack_player(warrior1)
print(f"{warrior2.pseudo} attaque {warrior1.pseudo}")
print(warrior2.pseudo, warrior2.health,warrior2.armor,warrior2.attack)
print(warrior1.pseudo, warrior1.health,warrior1.armor,warrior1.attack)



