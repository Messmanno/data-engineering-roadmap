# 1. Two Sum

# Étant donné un tableau d'entiers nums et un entier target, renvoyez les indices des deux nombres tels que leur somme soit égale à target.
# Vous pouvez supposer que chaque entrée possède exactement une solution, et que vous ne pouvez pas utiliser deux fois le même élément.
# Vous pouvez renvoyer la réponse dans n'importe quel ordre.

# Exemple :
#
# Entrée : nums = [2,7,11,15], cible = 9
#  Sortie : [0,1]
#  Explication : Parce que nums[0] + nums[1] == 9, nous renvoyons [0, 1].

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionnaire pour stocker les valeurs déjà vues et leurs indices
        seen = {}

        # Parcours du tableau
        for i, num in enumerate(nums):
            # Calcul du complément nécessaire pour atteindre la cible
            complement = target - num

            # Si le complément existe déjà dans le dictionnaire,
            # cela signifie qu'on a trouvé les deux nombres
            if complement in seen:
                return [seen[complement], i]

            # Sinon, on stocke la valeur actuelle et son indice
            seen[num] = i

        # Si aucune paire n'est trouvée
        return []


# --- Tests ---
if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]  # Cas normal
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]  # Cas classique
    assert sol.twoSum([3, 3], 6) == [0, 1]  # Cas avec doublons
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]  # Cas négatif
    print("✅ Tous les tests sont passés avec succès !")


