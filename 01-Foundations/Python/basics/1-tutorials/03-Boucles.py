# for : pour un valeur de depart jusqu'a une valeur d'arrivéé
for i in range(1, 6):
    print(f"Vous etes le client n°{i}")


# for each : pour chaque element d'une liste on effectuer ne action
blackliste = ["mes", "quoi"]
listes = ['mes','mer','pour','quoi']
for element in listes :
    if element in blackliste :
        print(f"Impossible d'envoyer eun email a cette personne : {element}")
        break     #continue
    print(f"email envoyé a {element}")


#while : tant que la condition est vraie execeuter un bloc d'instruction