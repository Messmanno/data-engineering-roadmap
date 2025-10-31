from statistics import mean

eleves = {
    'Paul': {'note' : 12, 'appreciation' : 'passable'},
    'Lea': {'note' : 15, 'appreciation' : 'bien'},
    'Thom': {'note' : 17, 'appreciation' : 'Tres bien'},
}

#print(eleves['Paul'])
#print(eleves.get('Paul',"prenom introuvabe !!!"))

print(eleves['Paul']['note'])

for key, value in eleves.items():
    print(key, value['note'], value['appreciation'])

#Ajouter
eleves['Manno'] = {
    'note' : 12, 'appreciation' : 'passable',
}

#Supprimer
del eleves['Manno']

#verifier qu'une valeur existe
if 'Thom' in eleves.keys():
    print(list(eleves.keys())[2] + "existe")

print(eleves)
# #boucle  d'affichage
# for key in eleves:
#     print(eleves[key])
#     print(key)
#
# for value in eleves.values():
#     print(value)
#
# for prenom, note in eleves.items():
#     print(prenom, note)
#
# #moyenne de classe
# average = sum(eleves.values()) / len(eleves.values())
# print(average)
