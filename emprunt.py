from datetime import datetime, timedelta
from livres import Livre
from adherent import Adherent

class Emprunt:
  _compteur = 0 

  def __init__(self, livre, adherent):#la classe emprunt n'est pas un livre ni un adherent, il utilise le livre et ;'adherent donc on les passe comme des attributs, il prend 2 objets (objet livre de la classe livre et adherent de la classe adherent)
    Emprunt._compteur += 1# en incremente pour chaque nouvel emprunt
    self.code = Emprunt._compteur # recoit un numero unique
    self.livre = livre 
    self.adherent = adherent
    self.date_emprunt = datetime.now() # en stocke la date et l'heure actuelles
    self.date_retour_prevue = self.date_emprunt + timedelta(days=3) # calcule la date de retour prevue 3jrs apres
    self.date_retour_effective = None # initialiseation de la date de retour: none signifie que le livre n'est pas encore rendu
    livre.nb_ex_dispo -= 1 # diminue le nombre d'exemplaires disponible car 1 est en cours d'emprunt

  def retour(self): # on appelle retour lorsque le livre est rendu  
    self.date_retour_effective = datetime.now() #alors on enregistre la date actuelle
    self.livre.nb_ex_dispo += 1 #puis en rend le livre au stock +1

  def etatEmprunt(self):
    if self.date_retour_effective:# si cette date nest pas none => recoit une valeur lorsque on apelle retour
       return "rendu"
    elif datetime.now() > self.date_retour_prevue:# si l'adherent a depasser la date prevu
        return "non rendu"
    else:
        return "en cours"
livre1 = Livre("بساتين عربستان","oumaima anbarek",4, 10)
adherent1 = Adherent("Ahmed", "ali", "2024-03-24")

# Création d’un emprunt
emprunt1 = Emprunt(livre1, adherent1)#execution de la methode init de la classe emprunt

print(f"Code emprunt : {emprunt1.code}")
print(f"Livre emprunté : {emprunt1.livre.titre}")
print(f"Adhérent : {emprunt1.adherent.getNom()}")
print(f"Date emprunt : {emprunt1.date_emprunt}")
print(f"Date retour prévue : {emprunt1.date_retour_prevue}")
print(f"État de l'emprunt : {emprunt1.etatEmprunt()}")
print(f"Exemplaires restants : {livre1.nb_ex_dispo}")