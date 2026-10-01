import personne
class Auteur(personne.Personne):

  def __init__(self, nom, prenom, code):
    super().__init__(nom, prenom)
    self._code = code
 
  def getCode(self):
    return self._code
  
  def setCode(self, code):
    self._code = code
   
  def afficher(self):
    return f"code:{self._code}   {super().afficher()}"
  
if __name__ == '__main__': # si je suis dans le fichier principale
 auteur = Auteur("Anbarek", "oumaima", 1)  
 print(auteur.afficher())