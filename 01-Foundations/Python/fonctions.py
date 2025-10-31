def welcom():
    print("Welcome to the Roadmap")
    resultat = 5
    print(resultat)

def next_year():
    global year
    print(f"Année en cours {year}")
    year += 1
    print(f"Année suivante {year}")

year = 2025
#fonction de maximum
def max(n,m):
    if n>m:
        return n
    else:
        return m

print(max(2,5))

#**********************************TP*******************************
#Ecrire une fonction pour calculer le nombre de voyelle dans un mot entré par le user

def get_number_of_voyel(mot) :
    voyelle = ["a","e","i","u","o","y"]
    i = 0
    for lettre in mot :
        if lettre in voyelle:
            i += 1

    return i

word = input("entrez un mot").lower()
print(get_number_of_voyel(word))


#*******************ou cette fonction optimisée qui gere les majuscules*********
def get_number_of_voyel(mot):
    voyelles = {"a", "e", "i", "o", "u", "y"}
    return sum(1 for lettre in mot if lettre.lower() in voyelles)

word = input("entrez un mot")
print(get_number_of_voyel(word))