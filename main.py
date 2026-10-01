import streamlit as st
from datetime import datetime
from Auteur import Auteur
from adherent import Adherent
from livres import Livre
from biblio import Biblio

# Sauvegarde de l'instance de la bibliothèque dans la session Streamlit
if 'biblio' not in st.session_state:
    st.session_state.biblio = Biblio()

biblio = st.session_state.biblio


choix = st.sidebar.radio("Menu Bibliothèque", [
    "1. Ajouter livre",
    "2. Afficher tous les livres",
    "3. Ajouter adhérent",
    "4. Emprunter un livre",
    "5. Retourner un livre",
    "6. Afficher livre le plus emprunté",
    "7. Afficher emprunteurs actifs",
    "8. Date disponibilité livre",
    "9. Afficher tous les adhérents"
])

# AJOUTER LIVRE
if choix == "1. Ajouter livre":
    st.title("Ajouter un Livre")
    titre = st.text_input("Titre du livre")
    nom = st.text_input("Nom auteur")
    prenom = st.text_input("Prénom auteur")
    code = st.text_input("Code livre")
    total = st.number_input("Nombre total d'exemplaires", min_value=1, value=1)

    if st.button("Valider"):
        if titre and nom and prenom and code:
            auteur = Auteur(nom, prenom, code)
            livre = Livre(code, titre, auteur, int(total))
            biblio.ajouterLivre(livre)
            st.success("Livre ajouté.")
            st.write(livre.afficher())
        else:
            st.error("Veuillez remplir tous les champs.")


#  AFFICHER TOUS LES LIVRES
elif choix == "2. Afficher tous les livres":
    st.title("📚 Liste des livres")
    if not biblio.livres:
        st.warning("Aucun livre dans la bibliothèque.")
    else:
        for livre in biblio.livres:
            st.write(livre.afficher())

#  AJOUTER ADHÉRENT
elif choix == "3. Ajouter adhérent":
    st.title("Ajouter un Adhérent")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_choisie = st.date_input("Date d'adhésion")

    if st.button("Ajouter Adhérent"):
        if nom and prenom:
            date = datetime.combine(date_choisie, datetime.min.time())
            adherent = Adherent(nom, prenom, date)
            biblio.ajouterAdherent(adherent)
            st.success(f"Adhérent ajouté. Code : {adherent.getCode()}")
        else:
            st.error("Veuillez remplir le nom et le prénom.")


#  EMPRUNTER UN LIVRE
elif choix == "4. Emprunter un livre":
    st.title("Emprunter un livre")
    code_livre = st.text_input("Code du livre à emprunter (ex: L1)")
    code_adh = st.text_input("Code de l'adhérent (ex: A1)")

    if st.button("Valider l'emprunt"):
        livre = biblio.rechercherLivre(code_livre)
        if livre is None:
            st.error("Livre introuvable.")
        else:
            adherent = biblio.rechercherAdherent(code_adh)
            if adherent is None:
                st.error("Adhérent introuvable.")
            elif livre.livreDisponible():
                emprunt = biblio.ajouterEmprunt(adherent.getCode(), livre.code)
                if emprunt is not None:
                    st.success(f"Le livre {livre.titre} a été emprunté par {adherent.getNom()} {adherent.getPrenom()}.")
                    st.info(f"Code emprunt : {emprunt.code}")
                else:
                    st.error("Erreur lors de l'emprunt.")
            else:
                st.warning("Livre non disponible.")


#  RETOURNER UN LIVRE

elif choix == "5. Retourner un livre":
    st.title("Retourner un livre")
    codeE = st.number_input("Code emprunt", min_value=1, value=1)

    if st.button("Enregistrer le retour"):
        if biblio.retourEmprunt(int(codeE)):
            st.success("Retour enregistré.")
        else:
            st.error("Erreur: emprunt introuvable.")


# AFFICHER LIVRE LE PLUS EMPRUNTÉ

elif choix == "6. Afficher livre le plus emprunté":
    st.title("Livre le plus emprunté")
    livre = biblio.topEmprunts()
    if livre:
        st.success(f"Livre le plus emprunté : {livre.afficher()}")
    else:
        st.info("Aucun emprunt.")


#  AFFICHER EMPRUNTEURS ACTIFS

elif choix == "7. Afficher emprunteurs actifs":
    st.title("Emprunteurs actifs")
    emprunteurs = biblio.emprunteurs()
    if emprunteurs:
        for a in emprunteurs:
            st.write(a.afficher())
    else:
        st.info("Aucun emprunteur actif.")


#  DATE DISPONIBILITÉ LIVRE

elif choix == "8. Date disponibilité livre":
    st.title("Date de disponibilité d'un livre")
    codeL = st.text_input("Code livre")

    if st.button("Vérifier"):
        st.info(f"Date possible : {biblio.datePossibiliteEmprunt(codeL)}")
       
#  AFFICHER TOUS LES ADHÉRENTS

elif choix == "9. Afficher tous les adhérents":
    st.title("👥 Liste des Adhérents")
    
    # On vérifie si la liste d'adhérents existe dans l'objet biblio
    if not hasattr(biblio, 'adherents') or not biblio.adherents:
        st.warning("Aucun adhérent enregistré.")
    else:
        for adherent in biblio.adherents:
            st.write(f"**Code :** `{adherent.getCode()}` | **Nom :** {adherent.getNom()} {adherent.getPrenom()}")