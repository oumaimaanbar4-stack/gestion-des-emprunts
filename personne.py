class Personne:#c’est un modèle pour créer des objets représentant une personne avec un nom et un prénom.
  def __init__(self, nom, prenom):#Constructeur : méthode spéciale appelée automatiquement lors de la création d’une instance de Personne.
    self.__nom = nom
    self.__prenom = prenom

  def getNom(self):#Permet d’accéder au nom de la personne.
    return self.__nom

  def getPrenom(self):
    return self.__prenom

  def setNom(self, nom):#Prend un paramètre nom et met à jour l’attribut.
    self.__nom = nom

  def setPrenom(self, prenom):
    self.__prenom = prenom

  def afficher(self):#retourne une chaîne de caractères formatée avec le nom et prénom.
    return f"Nom:{self.__nom} | Prenom:{self.__prenom}"

if __name__ == '__main__': # si je suis dans le fichier principale
  p1 = Personne("Alaoui", "karim") #Un objet est une instance concrète d'une classe. C’est une entité qui a des données (attributs) et peut effectuer des actions (méthodes).
  p2 = Personne("Rim", "Safae")   
  p1.afficher()
  p2.afficher() 

