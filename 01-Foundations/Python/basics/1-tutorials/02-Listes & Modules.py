#import statistics
from statistics import mean
from random import shuffle
#Tp Calculons

# notes = [
#     8, 12, 10,
#     9, 4, 20
# ]
# moyenne = mean(notes)
# print(f"la moyenne est {moyenne}")
#
# #liste melangée
# shuffle(notes)
# print(notes)
#
# #Decouper du texte en liste
# text = input("Entrez du texte sous la forme (email-pseudo-mdp ").split("-")
# print(text)


# #Creation de liste
# online_players = ["Graven", "Cool", "Manno"]
#
# # Afficher
# print(online_players)
#
# # Modifier
# online_players[0] = "Gravenilvec"
# # Inserer a une position precise
# #online_players.insert(0, "Mayo")
#
# # Ajouter a la fin
# online_players.append("Messmanno")
#
# # Ajouter plusieyrs a la fin
# online_players.extend(["Gogo","Gaga","Gugu"])
# print(online_players)
#
# # Supprimer un element
#     #del online_players[3]
#     #online_players.remove("Manno")
#     #online_players.pop(1)
#
# #Vider la liste
# #online_players.clear()
#
# print(online_players)

#************************TP GENERATEUR DE PHRASE******************
#Demandons une chaine de caractere de la forme "mot1/mot2/mot3/mot4 etc et la transformer en liste
texte =  input("Entrez du texte de la forme mot1/mot2/mot3/mot4 : ").split("/")
print(texte)
#Melangeons cette liste
shuffle(texte)
print(texte)
#Si le nombre de mot est inferieur a 5 Afficher les deux premiers mots
if len(texte) < 5 :
    print(texte[0:1])
#Sinon afficher les 3 derniers mots
else:
    print(texte[len(texte)-1], texte[len(texte)-2], texte[len(texte)-3])
