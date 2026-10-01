from datetime import datetime
from personne import Personne 
class Adherent(Personne):
  _cpt = 0#Sert à générer un identifiant unique pour chaque adhérent (auto-incrémenté).

  def __init__(self, nom, prenom, dateAdhesion):#Constructeur : méthode appelée à la création d’un objet Adherent.
    super().__init__(nom, prenom)#Appel du constructeur de la classe parente Personne/ super() permet d’éviter de réécrire le code de la classe parent.
    Adherent._cpt +=1
    self._code = f"A{Adherent._cpt}" #le code est A...
    self._dateAdhesion = dateAdhesion

  def getCode(self):
    return self._code
  
  def afficher(self):
    return f"code: {self._code}♦ Nom:{self.getNom()} Prenom:{self.getPrenom()} Date:{self._dateAdhesion.strftime('%d %m %y')}"


if __name__ == '__main__': # si je suis dans le fichier principale
  p1 = Adherent("Alaoui", "karim", datetime(2025,4, 10)) 
  p2 = Adherent("Rim", "Safae", datetime(2025,6, 1))   
  print(p1.afficher())
  print(p2.afficher()) 