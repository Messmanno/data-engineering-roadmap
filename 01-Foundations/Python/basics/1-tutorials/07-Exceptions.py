import  json

# while True:
#     try:
#         prixHT = int(input("Entrez le prix HT : "))
#         prixTTC = prixHT + prixHT * 0.2
#         print(prixTTC)
#         break
#     except ValueError:
#         print("Attention veuillez entrer un nombre")


# try:
#     with open("meals.txt","r+") as file :
#         print(file.readlines()[10])
#         file.close()
# except FileNotFoundError:
#     print("File not found")
# except IndexError as i:
#     print("Erreur d'index")
# finally:
#     print("fin de verification...")
#

class FileNotJsonFormatError(Exception):
     def __init__(self):
         self.message = "Filename must end with .json"


#fichier json
# def read_json_file(filename):
#     try:
#         if not filename.endswith(".json"):                     #verifier le bon fichier
#             raise Exception("Filename must end with .json")    #declencher une exception personnalisée
#         with open(filename, "r+") as file:
#             print(json.load(file))
#             file.close()
#     except Exception as e:
#         print(e)     #Capture de notre exception créée plus haut
#     except FileNotFoundError:
#         print("File not found")


#Gestion des exceptions personnalisées
def read_json_file(filename):
    try:
        if not filename.endswith(".json"):                     #verifier le bon fichier
            raise FileNotJsonFormatError                        #declencher une exception personnalisée
        with open(filename, "r+") as file:
            print(json.load(file))
            file.close()
    except FileNotJsonFormatError as e:
        print(e.message)     #Capture de notre exception créée plus haut
    except FileNotFoundError:
        print("File not found")
read_json_file("data.jsn")