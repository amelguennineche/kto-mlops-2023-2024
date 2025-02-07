message = "C'est mon premier script !!!"
print(message)

je_change_de_type = 1
print(type(je_change_de_type))
je_change_de_type = "coucou"
print(type(je_change_de_type))

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0
for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
    else:
        print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(more_than_seven))

def saluer(nom: str) -> str:
    return "Bonjour " + nom

print(saluer("Alice"))  # Affiche : Bonjour Alice

"""
Count names with more than seven letters
"""
def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(prenoms=prenoms)))

import unittest

NAME_LENGTH_LIMIT = 7
"""
    Compte le nombre de prénoms ayant plus de NAME_LENGTH_LIMIT lettres.
    Args:
        names_list (List[str]): Liste des prénoms.
    Returns:
        int: Nombre de prénoms de plus de NAME_LENGTH_LIMIT lettres.
    """
def count_long_names(prenom_list: list[str]) -> int :
    counter_long_names = sum(1 for prenom in prenom_list if len(prenom) > NAME_LENGTH_LIMIT)
    for prenom in prenom_list:
        comparaison = "supérieur" if len(prenom) > NAME_LENGTH_LIMIT else "inférieur ou égal"
        print(f"{prenom} est un prénom avec un nombre de lettres {comparaison} à {NAME_LENGTH_LIMIT}")
    return counter_long_names

class TestNamesMethod(unittest.TestCase):
     def count_long_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_long_names(prenom_list=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()
