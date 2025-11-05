#Lecture et nettoyage du fichier
class Struct_data:
    def __init__(self, x):
        self._nom = x[0]
        self._isin = x[1]
        self._symbol = x[2]
        self._market = x[3]
        self._currency = x[4]
        self._openPrice = float(x[5])
        self._hightPrice = x[6]
        self._lowPrice = x[7]
        self._lastPrice = x[8]
        self._mic = x[9]


line_count = 0
dicts = {}
with open("Euronext_Equities_2025-11-04.csv", "r+") as file :
    for line in file :              #recupere chaque ligne
        if line_count >= 4:         #verifie si nous sommes a la ligne 5
            x = line.replace('"','').split(";")     #split toutes les lignes avec des sep = ; pour les transformer en lists
            if not '-' in x :               #recuperer les lignes avec des valeurs non manquantes (- représente une valeure manquante)
                dicts[x[1]] = Struct_data(x)
                #print(x)                #affiche les listes
        line_count += 1             #incremente le nombre de lignes

print(dicts['FR0010557264']._openPrice)
#on se rend compte que les noms qui possèdent des espaces sont entourés de "" (ex : "YOUNITED FIN. WARR")
#on utilisera la fonction replace (voir le bloc if)
#on se rend compte que lorsqu'on parcourt notre boucle et affiche les données, ils ne sont pas sauvegardés
#on crée donc un dictionnaire qui apres la verification de la ligne stocke dans un dictionnaire(key:code isbn ; valeur : la ligne vérifiée)
#on veut nommer les colonnes pour faciliter les recherches : on va creer une classe qui va nommer nos colonnes et si possible les typer :
# on peut acceder de la maniere suivante : dicts[key].name_column
