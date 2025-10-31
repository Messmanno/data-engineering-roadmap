
# def decorateur(func):
#     def wrapper():
#         print("avant")
#         func()
#         print("apres")
#     return wrapper
#
# @decorateur
# def say_hello():
#     print("hello")
#
# say_hello()
#



def is_admin(func):
    def wrapper(role):
        if role == "admin":
            func()
        else:
            print("vous n'avez pas le permission")
    return wrapper

@is_admin
def creer_fichier():
        print("Fichier creer")
@is_admin
def modifier_fichier():
        print("Fichier modifier")
@is_admin
def supprimer_fichier():
        print("Fichier supprimer")


creer_fichier('user')
modifier_fichier('user')
supprimer_fichier('admin')