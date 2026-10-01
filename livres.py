from Auteur import Auteur
class Livre:
  def __init__(self, code, titre, auteur, nb_ex_total):
    self.code = code
    self.titre = titre
    self.auteur = auteur  # instance de Auteur
    self.nb_ex_total = nb_ex_total
    self.nb_ex_dispo = nb_ex_total

  def livreDisponible(self):#Renvoie True si au moins un exemplaire est disponible, sinon False.
    return self.nb_ex_dispo > 0

  def afficher(self):#Retourne une chaîne contenant les informations du livre : code, titre, nom et prénom de l’auteur et le nombre d’exemplaires
    return f"{self.code} - {self.titre} - Auteur: {self.auteur.getNom()} {self.auteur.getPrenom()} - Disponible: {self.nb_ex_dispo}/{self.nb_ex_total}"
if __name__ == '__main__': # ici j'ai crée 3 livres avec des titres, auteurs et quantités
  try:
    total = int(input("Nombre total d'exemplaires: "))
    dispo = int(input("Nombre d'exemplaires disponibles: "))
  except ValueError:
    print("Erreur: entrez un nombre valide.")
  else: 
   auteur1 = Auteur("Coelho","Paulo",1)
   auteur2 = Auteur("Saint-Exupéry", "Antoine", 2)
   auteur3 = Auteur("Rowling", "J.K.", 3)

   livre1 = Livre("L1", "L'Alchimiste", auteur1, 5)
   livre2 = Livre("L2", "Le Petit Prince", auteur2, 6)
   livre3 = Livre("L3", "Harry Potter à l'école des sorciers", auteur3, 10)
  
   print(livre1.afficher())#affiche leurs informations grace à la methode Afficher
   print(livre2.afficher())   
   print(livre3.afficher())