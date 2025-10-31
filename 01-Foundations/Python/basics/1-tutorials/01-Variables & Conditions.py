
    #1- write a script python to calculate average
def average_():
    #mark inputs
    note1 = int(input("Entrez la premiere note: "))
    note2 = int(input("Entrez la deuxieme note: "))
    note3 = int(input("Entrez la troisieme note: "))
    # average  b
    average = (note1 + note2 + note3) / 3
    # afficher la moyenne
    print("La moyenne est " + str(average))


    #2- write a script to simulate paiement
def paiement_simulated():
    wallet = int(input("Entrez le montant de votre porte monaie: "))
    product_price = int(input("Entrez le prix du produit: "))
    qty = int(input("Entrez la quantité du produit: "))
    wallet = wallet - (product_price * qty)

    print("Achat en cours...")
    if wallet < 0:
        print("Vous n'avez pas suffisamment de fond pour effectuer ce paiement 😢😢😢")
    else :
        print("Achat effectué avec succes !!!! 👌👌👌")
        print("Solde apres achat = " + str(wallet))


    #3- passwordlenght verification
def password_verifiaction(password):
    if(len(password) < 8):
        print("Le mot de passe est trop court")
    elif(8<len(password)<16):
        print("Le mot de passe est moyen")
    else:
        print("Le mot de passe est parfait")

#Appel de fonction
if __name__ == '__main__':
    paiement_simulated()


    #4- checking available places
place_price = 0
price_pop_corn = 5
total = 0

age = int(input("Entrez votre age svp :"))
if age < 18:
    place_price = 7
    print("Vous etes mineur vous payez donc 7$")
else :
    place_price = 12
    print("Vous etes majeur vous payez 12$")

pop_corn = input("Voulez vous du pop corn :").lower()
if pop_corn == "oui" :
    total = place_price + price_pop_corn
    print(f"le pop corn coute {price_pop_corn}$")
elif str(pop_corn) == "non" :
    total = place_price
else :
    print("veuillez saisir oui ou non")
    total = place_price

print(f"💰 Le total à payer est de {total} $.")

    # Conditions n-aire
val = 2
res = ("ok","non")[val < 5]