import os
import random
import shutil
# 1ere methode
# file = open("students.txt","w+")  ouverture ou creation d'un fichier students.txt
# file.write("Mes\n")               ecriture dans le fichier
# file.write("Mer\n")               " "
# file.write("Fort\n")              " "
# file.close()                      fermeture

students_list = ["mes","mer","ka",'tie']
# # 2e methode
# # w+ va ecraser le contenu de l'ancien fichier tandis que a+ va ecrire a la suite du contenu du fichier
# with open("students.txt", "w+") as file:
#     for student in students_list:
#         file.write("Hello " + student + "\n")
#     file.close()

# if os.path.exists("meals.txt"):
# #Proposer le menus
#     with open("meals.txt","r+") as file:
#         meal_list = file.readlines()
#         meal_random_choice = random.choice(meal_list)
#         print(f"Je vous proposeaujourd'hui le repas : {meal_random_choice}")
#         #for menu in file:
#         #    print(menu)
#         file.close()
# else:
#     print("File not found")
#

#Deplacer un fichier
source = os.path.abspath("meals.txt")
destination = os.path.abspath("../2-exercises/meals.txt")

shutil.copy(source,destination)

print(f"Source : {source}")
print(f"Destination : {destination}")