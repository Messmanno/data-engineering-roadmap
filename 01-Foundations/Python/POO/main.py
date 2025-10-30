from Models.Player import Player
from Models.Weapon import Weapon

knife = Weapon("Couteau", 2)

player1 = Player("Pierre",100,3)
player2 = Player("Paul",100,5)
#Donne un couteau a player1
player2.set_weapon(knife)

player2.attack_player(player1)
print(f"{player2.get_pseudo()} attaque {player1.get_pseudo()}...")   #attack =5 + knife =2

print(f" {player1.get_pseudo()}, point d'attaque : {player1.get_attack()} et vie : {player1.get_health()}")
print(f" {player2.get_pseudo()}, point d'attaque : {player2.get_attack()} et vie : {player2.get_health()}")