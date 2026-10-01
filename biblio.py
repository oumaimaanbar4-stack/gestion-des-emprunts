from emprunt import Emprunt
from livres import Livre
class Biblio:
  def __init__(self):
    self.livres = []
    self.adherents = []
    self.emprunts = []

  def ajouterLivre(self, livre):
    self.livres.append(livre)

  def ajouterAdherent(self, adherent):
    self.adherents.append(adherent)

  def rechercherAdherent(self, code):
    for adherent in self.adherents:#parcours chaque adherent dans la liste self.adherents
        if adherent.getCode() == code:  
            return adherent
    return None


  def rechercherLivre(self, code):
    for livre in self.livres:
        if livre.code == code:
            return livre
    return None

  def ajouterEmprunt(self, codeA, codeL):
    adherent = self.rechercherAdherent(codeA)# on cherche adherent avec codeAdherent/ retourne soit un objet adherent soit None
    livre = self.rechercherLivre(codeL)# on cherche code livre
    if not adherent: #verifie si l'adherent avec le code donne existe, Vrai si adherent est None
        print("Adhérent introuvable.")
        return None
    if not livre:
        print("Livre introuvable.")
        return None
    if not livre.livreDisponible():
        print("Aucun exemplaire disponible.")
        return None 

    nouveau_emprunt = Emprunt(livre, adherent)
    self.emprunts.append(nouveau_emprunt)
    return nouveau_emprunt

  def retourEmprunt(self, codeEmprunt):#gerer le retour
    for emprunt in self.emprunts:
        if emprunt.code == codeEmprunt:
            if emprunt.date_retour_effective is None:#si le livre n'a pas encore ete retourner
                emprunt.retour()# si oui en appele la methode retour(), qui retourne True
                return True
            else:
                return False
  

  def topEmprunts(self):
    if not self.emprunts:#si la liste est vide
        return None
    
    compteur = {}# dictionnaire compteur/ compte le combre d'emprunts pour chaque livre
    for e in self.emprunts:#en parcours tous les objets emprunts dans la liste
        livre = e.livre #recupere l'objet livre associe a chaque emprunt e
        if livre in compteur:#si ce livre existe deja dans le dictionnaire compteur 
            compteur[livre] += 1# on incremante sa valeur
        else:
            compteur[livre] = 1# on enregistre la premiere apparition d'un livre id=>livre
    
    # Trouver le livre du livre le plus emprunté
    top_livre = None
    max_count = 0
    for livre, count in compteur.items():# on parcourt chaque livre et son nombre d'emprunts dans le dictionnaire compteur.
        if count > max_count:# si le nombre d'emprunts est sup a max_count
            max_count = count#mis a jour max count
            top_livre = livre# le nouveau livre le plus emprunte
    return top_livre# a la fin on retourne l'objet livre
  
  def emprunteurs(self):#le but est savoir les adherents qui ont un livre non encore rendu.
    emprunteurs_set = set()# est une methode en python/ une liste ou un dictionnaire, mais sans doublons
    for e in self.emprunts:#on parcourt tous les emprunts effectues.
        if e.etatEmprunt() != "rendu":#si l'etat d'emprunts est differents de rendu 
            emprunteurs_set.add(e.adherent)#=> on ajoute l'adherent dans le set
    return list(emprunteurs_set)# renvoie la liste

  def datePossibiliteEmprunt(self, codeL):# quand le livre est disponible pour lemprunt
    livre = self.rechercherLivre(codeL)#cherche le livre avec codeL pour obtenir l'objet livre
    if livre is None:
        return "Livre introuvable"
    
    if livre.livreDisponible():#si le livre a encore des exemplaires disponibles, on peut l'emprunter tout de suite
        return "Disponible maintenant"
    
    dates_retour = []#on cree une liste vide pour stocker les dates prevu de retour des exmplaires 
    for e in self.emprunts:
        if e.livre.code == codeL and e.date_retour_effective is None:#si le code du livre emprunte correspond au code du livre qu'on cherche(codeL) et si le livre n'a pas encore ete retourne/ le livre est toujours emprunte
            dates_retour.append(e.date_retour_prevue)# on ajout la date de retour prevue a cette liste vide
    
    if len(dates_retour) > 0: # si la liste des dates_retour contient au moins une date
        return min(dates_retour)  # retourne la date la plus petite alors la date le plus proche
    else:
        return "Aucune date prévue"
    




 