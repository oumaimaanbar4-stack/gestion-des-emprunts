from biblio import Biblio
from Auteur import Auteur
from livres import Livre

code_livre = input("Code du livre à emprunter (ex: L1): ")
biblio = Biblio()  # crée l'objet bibliothèque

auteur1 = Auteur("Coelho", "Paulo", "A1")
livre1 = Livre("L1", "L'Alchimiste", auteur1, 5, 5)

biblio.ajouterLivre(livre1)  # ajoute le livre dans la bibliothèque

print([livre.code for livre in biblio.livres])  # doit afficher ['L1']

code_livre = input("Code du livre à emprunter (ex: L1): ")
livre_trouve = biblio.rechercherLivre(code_livre)
if livre_trouve is None:
    print("Livre introuvable.")
else:
    print(f"Livre trouvé: {livre_trouve.titre}")
