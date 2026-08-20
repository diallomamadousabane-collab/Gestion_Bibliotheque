"""
Application de gestion de bibliothèque
Point d'entrée principal
"""

from services.bibliotheque import Bibliotheque
from exceptions.exceptions import (
    LivreIndisponibleError,
    LivreNonTrouveError,
    AdherentNonTrouveError,
    EmpruntNonTrouveError
)


def afficher_menu_principal():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("GESTION DE BIBLIOTHÈQUE")
    print("="*50)
    print("1.  Ajouter un livre")
    print("2.  Modifier un livre")
    print("3.  Supprimer un livre")
    print("4.  Rechercher un livre")
    print("5.  Afficher les livres")
    print("6.  Ajouter un adhérent")
    print("7.  Afficher les adhérents")
    print("8.  Modifier un adhérent")
    print("9.  Supprimer un adhérent")
    print("10. Emprunter un livre")
    print("11. Retourner un livre")
    print("12. Afficher les emprunts")
    print("13. Sauvegarder les données")
    print("14. Quitter")
    print("="*50)


def ajouter_livre(bib):
    """Ajoute un nouveau livre"""
    print("\n--- AJOUTER UN LIVRE ---")
    try:
        id_livre = input("ID du livre: ").strip()
        titre = input("Titre: ").strip()
        auteur = input("Auteur: ").strip()
        annee = input("Année de publication: ").strip()
        genre = input("Genre: ").strip()
        
        bib.ajouter_livre(id_livre, titre, auteur, annee, genre)
    except Exception as e:
        print(f"Erreur: {e}")


def modifier_livre(bib):
    """Modifie un livre"""
    print("\n--- MODIFIER UN LIVRE ---")
    try:
        id_livre = input("ID du livre à modifier: ").strip()
        print("(Laissez vide pour ne pas modifier)")
        titre = input("Nouveau titre (optionnel): ").strip() or None
        auteur = input("Nouvel auteur (optionnel): ").strip() or None
        annee = input("Nouvelle année (optionnel): ").strip() or None
        genre = input("Nouveau genre (optionnel): ").strip() or None
        
        bib.modifier_livre(id_livre, titre, auteur, annee, genre)
    except Exception as e:
        print(f"Erreur: {e}")


def supprimer_livre(bib):
    """Supprime un livre"""
    print("\n--- SUPPRIMER UN LIVRE ---")
    try:
        id_livre = input("ID du livre à supprimer: ").strip()
        confirmation = input("Êtes-vous sûr? (oui/non): ").strip().lower()
        if confirmation == "oui":
            bib.supprimer_livre(id_livre)
        else:
            print("Suppression annulée")
    except Exception as e:
        print(f"Erreur: {e}")


def rechercher_livre(bib):
    """Recherche un livre"""
    print("\n--- RECHERCHER UN LIVRE ---")
    print("1. Par ID")
    print("2. Par titre")
    print("3. Par auteur")
    
    choix = input("Votre choix: ").strip()
    
    try:
        if choix == "1":
            id_livre = input("ID du livre: ").strip()
            livre = bib.rechercher_livre_par_id(id_livre)
            print(f"\nRésultat: {livre}\n")
        elif choix == "2":
            titre = input("Titre (ou partie du titre): ").strip()
            resultats = bib.rechercher_livres_par_titre(titre)
            if resultats:
                print("\nRésultats:")
                for livre in resultats:
                    print(livre)
                print()
            else:
                print("Aucun livre trouvé")
        elif choix == "3":
            auteur = input("Auteur (ou partie du nom): ").strip()
            resultats = bib.rechercher_livres_par_auteur(auteur)
            if resultats:
                print("\nRésultats:")
                for livre in resultats:
                    print(livre)
                print()
            else:
                print("Aucun livre trouvé")
        else:
            print("Choix invalide")
    except Exception as e:
        print(f"Erreur: {e}")


def ajouter_adherent(bib):
    """Ajoute un nouvel adhérent"""
    print("\n--- AJOUTER UN ADHÉRENT ---")
    try:
        id_adherent = input("ID de l'adhérent: ").strip()
        nom = input("Nom: ").strip()
        prenom = input("Prénom: ").strip()
        telephone = input("Téléphone: ").strip()
        email = input("Email: ").strip()
        
        bib.ajouter_adherent(id_adherent, nom, prenom, telephone, email)
    except Exception as e:
        print(f"Erreur: {e}")


def modifier_adherent(bib):
    """Modifie un adhérent"""
    print("\n--- MODIFIER UN ADHÉRENT ---")
    try:
        id_adherent = input("ID de l'adhérent à modifier: ").strip()
        print("(Laissez vide pour ne pas modifier)")
        nom = input("Nouveau nom (optionnel): ").strip() or None
        prenom = input("Nouveau prénom (optionnel): ").strip() or None
        telephone = input("Nouveau téléphone (optionnel): ").strip() or None
        email = input("Nouvel email (optionnel): ").strip() or None
        
        bib.modifier_adherent(id_adherent, nom, prenom, telephone, email)
    except Exception as e:
        print(f"Erreur: {e}")


def supprimer_adherent(bib):
    """Supprime un adhérent"""
    print("\n--- SUPPRIMER UN ADHÉRENT ---")
    try:
        id_adherent = input("ID de l'adhérent à supprimer: ").strip()
        confirmation = input("Êtes-vous sûr? (oui/non): ").strip().lower()
        if confirmation == "oui":
            bib.supprimer_adherent(id_adherent)
        else:
            print("Suppression annulée")
    except Exception as e:
        print(f"Erreur: {e}")


def emprunter_livre(bib):
    """Permet à un adhérent d'emprunter un livre"""
    print("\n--- EMPRUNTER UN LIVRE ---")
    try:
        id_livre = input("ID du livre: ").strip()
        id_adherent = input("ID de l'adhérent: ").strip()
        bib.emprunter_livre(id_livre, id_adherent)
    except (LivreIndisponibleError, LivreNonTrouveError, AdherentNonTrouveError) as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Erreur inattendue: {e}")


def retourner_livre(bib):
    """Permet à un adhérent de retourner un livre"""
    print("\n--- RETOURNER UN LIVRE ---")
    try:
        id_livre = input("ID du livre: ").strip()
        id_adherent = input("ID de l'adhérent: ").strip()
        bib.retourner_livre(id_livre, id_adherent)
    except (EmpruntNonTrouveError, LivreNonTrouveError, AdherentNonTrouveError) as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Erreur inattendue: {e}")


def main():
    """Fonction principale"""
    print("\n" + "="*50)
    print("BIENVENUE DANS L'APPLICATION DE GESTION DE BIBLIOTHÈQUE")
    print("="*50)
    
    # Initialiser la bibliothèque
    try:
        bib = Bibliotheque(dossier_data="data")
        print("\n✓ Bibliothèque initialisée\n")
    except Exception as e:
        print(f"\n✗ Erreur lors de l'initialisation: {e}")
        return
    
    # Boucle principale
    while True:
        afficher_menu_principal()
        choix = input("Votre choix: ").strip()
        
        try:
            if choix == "1":
                ajouter_livre(bib)
            elif choix == "2":
                modifier_livre(bib)
            elif choix == "3":
                supprimer_livre(bib)
            elif choix == "4":
                rechercher_livre(bib)
            elif choix == "5":
                bib.afficher_tous_les_livres()
            elif choix == "6":
                ajouter_adherent(bib)
            elif choix == "7":
                bib.afficher_tous_les_adherents()
            elif choix == "8":
                modifier_adherent(bib)
            elif choix == "9":
                supprimer_adherent(bib)
            elif choix == "10":
                emprunter_livre(bib)
            elif choix == "11":
                retourner_livre(bib)
            elif choix == "12":
                bib.afficher_tous_les_emprunts()
            elif choix == "13":
                bib.sauvegarder_donnees()
            elif choix == "14":
                print("\nSauvegarde automatique des données...")
                bib.sauvegarder_donnees()
                print("Au revoir!")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")


if __name__ == "__main__":
    main()
