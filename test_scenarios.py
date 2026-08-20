"""
Script de test des 10 scénarios demandés
Teste toutes les fonctionnalités principales de l'application
"""

import os
import shutil
from services.bibliotheque import Bibliotheque
from exceptions.exceptions import (
    LivreIndisponibleError,
    LivreNonTrouveError,
    AdherentNonTrouveError,
    EmpruntNonTrouveError
)


def nettoyer_data():
    """Nettoie les fichiers de données pour recommencer de zéro"""
    if os.path.exists("data"):
        shutil.rmtree("data")
    print("✓ Données nettoyées\n")


def afficher_test(numero, titre):
    """Affiche le titre d'un test"""
    print("\n" + "="*60)
    print(f"TEST {numero}: {titre}")
    print("="*60)


def test_1_ajouter_livre():
    """TEST 1: Ajouter un livre"""
    afficher_test(1, "Ajouter un livre")
    
    bib = Bibliotheque(dossier_data="data")
    
    try:
        # Ajouter un premier livre
        livre1 = bib.ajouter_livre(
            "L001",
            "Le Petit Prince",
            "Antoine de Saint-Exupéry",
            "1943",
            "Conte"
        )
        
        # Ajouter d'autres livres
        livre2 = bib.ajouter_livre(
            "L002",
            "1984",
            "George Orwell",
            "1949",
            "Science-fiction"
        )
        
        livre3 = bib.ajouter_livre(
            "L003",
            "Le Seigneur des Anneaux",
            "J.R.R. Tolkien",
            "1954",
            "Fantasy"
        )
        
        assert len(bib.livres) == 3, "Erreur: 3 livres devaient être ajoutés"
        assert livre1.titre == "Le Petit Prince", "Erreur: titre incorrect"
        
        print("✓ TEST 1 RÉUSSI: 3 livres ajoutés avec succès\n")
        return bib
    except Exception as e:
        print(f"✗ TEST 1 ÉCHOUÉ: {e}\n")
        raise


def test_2_afficher_livres(bib):
    """TEST 2: Afficher les livres"""
    afficher_test(2, "Afficher les livres")
    
    try:
        print(f"Nombre de livres: {len(bib.livres)}")
        bib.afficher_tous_les_livres()
        
        assert len(bib.livres) == 3, "Erreur: devrait avoir 3 livres"
        
        print("✓ TEST 2 RÉUSSI: Tous les livres affichés correctement\n")
    except Exception as e:
        print(f"✗ TEST 2 ÉCHOUÉ: {e}\n")
        raise


def test_3_rechercher_livre_existant(bib):
    """TEST 3: Rechercher un livre existant"""
    afficher_test(3, "Rechercher un livre existant")
    
    try:
        # Recherche par ID
        livre = bib.rechercher_livre_par_id("L001")
        assert livre.titre == "Le Petit Prince", "Erreur: livre incorrect"
        print(f"✓ Livre trouvé par ID: {livre}")
        
        # Recherche par titre
        resultats = bib.rechercher_livres_par_titre("Petit Prince")
        assert len(resultats) == 1, "Erreur: un seul livre devrait être trouvé"
        print(f"✓ Livre trouvé par titre: {resultats[0]}")
        
        # Recherche par auteur
        resultats = bib.rechercher_livres_par_auteur("Orwell")
        assert len(resultats) == 1, "Erreur: un seul livre d'Orwell"
        print(f"✓ Livre trouvé par auteur: {resultats[0]}")
        
        print("✓ TEST 3 RÉUSSI: Recherches fonctionnent correctement\n")
    except Exception as e:
        print(f"✗ TEST 3 ÉCHOUÉ: {e}\n")
        raise


def test_4_rechercher_livre_inexistant(bib):
    """TEST 4: Rechercher un livre inexistant"""
    afficher_test(4, "Rechercher un livre inexistant")
    
    try:
        # Recherche par ID inexistant
        try:
            bib.rechercher_livre_par_id("L999")
            print("✗ Erreur: devrait lever une exception LivreNonTrouveError")
            raise AssertionError("Exception non levée")
        except LivreNonTrouveError as e:
            print(f"✓ Exception levée correctement: {e}")
        
        # Recherche par titre inexistant
        resultats = bib.rechercher_livres_par_titre("Titre inexistant")
        assert len(resultats) == 0, "Erreur: aucun livre ne devrait être trouvé"
        print(f"✓ Aucun résultat pour titre inexistant")
        
        print("✓ TEST 4 RÉUSSI: Gestion des livres inexistants correcte\n")
    except Exception as e:
        print(f"✗ TEST 4 ÉCHOUÉ: {e}\n")
        raise


def test_5_ajouter_adherent(bib):
    """TEST 5: Ajouter un adhérent"""
    afficher_test(5, "Ajouter un adhérent")
    
    try:
        # Ajouter des adhérents
        adh1 = bib.ajouter_adherent(
            "A001",
            "DIOP",
            "Moussa",
            "77 000 00 00",
            "moussa@example.com"
        )
        
        adh2 = bib.ajouter_adherent(
            "A002",
            "SARR",
            "Fatou",
            "77 111 11 11",
            "fatou@example.com"
        )
        
        adh3 = bib.ajouter_adherent(
            "A003",
            "NDIAYE",
            "Amadou",
            "77 222 22 22",
            "amadou@example.com"
        )
        
        assert len(bib.adherents) == 3, "Erreur: 3 adhérents devaient être ajoutés"
        assert adh1.get_nom_complet() == "Moussa DIOP", "Erreur: nom complet incorrect"
        
        print("✓ TEST 5 RÉUSSI: 3 adhérents ajoutés avec succès\n")
        return bib
    except Exception as e:
        print(f"✗ TEST 5 ÉCHOUÉ: {e}\n")
        raise


def test_6_emprunter_livre_disponible(bib):
    """TEST 6: Emprunter un livre disponible"""
    afficher_test(6, "Emprunter un livre disponible")
    
    try:
        # Vérifier que le livre est disponible
        livre = bib.rechercher_livre_par_id("L001")
        assert livre.est_disponible(), "Erreur: le livre devrait être disponible"
        print(f"✓ Livre L001 est disponible: {livre.disponible}")
        
        # Emprunter le livre
        emprunt = bib.emprunter_livre("L001", "A001")
        
        # Vérifier que le livre n'est plus disponible
        assert not livre.est_disponible(), "Erreur: le livre ne devrait pas être disponible"
        print(f"✓ Livre L001 maintenant indisponible: {livre.disponible}")
        
        # Vérifier que l'emprunt est créé
        assert len(bib.emprunts) == 1, "Erreur: un emprunt devrait être créé"
        assert emprunt.est_actif(), "Erreur: l'emprunt devrait être actif"
        
        print("✓ TEST 6 RÉUSSI: Emprunt réussi\n")
    except Exception as e:
        print(f"✗ TEST 6 ÉCHOUÉ: {e}\n")
        raise


def test_7_emprunter_livre_deja_emprunte(bib):
    """TEST 7: Essayer d'emprunter le même livre une deuxième fois"""
    afficher_test(7, "Essayer d'emprunter le même livre une deuxième fois")
    
    try:
        # Essayer d'emprunter le même livre L001 (déjà emprunté par A001)
        try:
            bib.emprunter_livre("L001", "A002")
            print("✗ Erreur: devrait lever une exception LivreIndisponibleError")
            raise AssertionError("Exception non levée")
        except LivreIndisponibleError as e:
            print(f"✓ Exception levée correctement: {e}")
        
        # Vérifier qu'aucun nouvel emprunt n'a été créé
        assert len(bib.emprunts) == 1, "Erreur: toujours un seul emprunt"
        
        # Pouvoir emprunter un autre livre
        emprunt2 = bib.emprunter_livre("L002", "A002")
        assert len(bib.emprunts) == 2, "Erreur: deux emprunts maintenant"
        
        print("✓ TEST 7 RÉUSSI: Protection contre les emprunts doubles fonctionnel\n")
    except Exception as e:
        print(f"✗ TEST 7 ÉCHOUÉ: {e}\n")
        raise


def test_8_retourner_livre(bib):
    """TEST 8: Retourner le livre"""
    afficher_test(8, "Retourner le livre")
    
    try:
        # Vérifier que le livre L001 n'est pas disponible
        livre = bib.rechercher_livre_par_id("L001")
        assert not livre.est_disponible(), "Erreur: le livre devrait être indisponible"
        
        # Retourner le livre
        emprunt = bib.retourner_livre("L001", "A001")
        
        # Vérifier que le livre est à nouveau disponible
        assert livre.est_disponible(), "Erreur: le livre devrait être disponible"
        print(f"✓ Livre L001 est à nouveau disponible: {livre.disponible}")
        
        # Vérifier que l'emprunt n'est plus actif
        assert not emprunt.est_actif(), "Erreur: l'emprunt ne devrait pas être actif"
        assert emprunt.date_retour is not None, "Erreur: date de retour manquante"
        print(f"✓ Emprunt marqué comme retourné: {emprunt.date_retour}")
        
        print("✓ TEST 8 RÉUSSI: Retour de livre fonctionnel\n")
    except Exception as e:
        print(f"✗ TEST 8 ÉCHOUÉ: {e}\n")
        raise


def test_9_retourner_livre_non_emprunte(bib):
    """TEST 9: Essayer de retourner un livre non emprunté"""
    afficher_test(9, "Essayer de retourner un livre non emprunté")
    
    try:
        # Essayer de retourner L001 alors qu'il a déjà été retourné
        try:
            bib.retourner_livre("L001", "A001")
            print("✗ Erreur: devrait lever une exception EmpruntNonTrouveError")
            raise AssertionError("Exception non levée")
        except EmpruntNonTrouveError as e:
            print(f"✓ Exception levée correctement: {e}")
        
        # Essayer de retourner L003 qui n'a jamais été emprunté
        try:
            bib.retourner_livre("L003", "A001")
            print("✗ Erreur: devrait lever une exception EmpruntNonTrouveError")
            raise AssertionError("Exception non levée")
        except EmpruntNonTrouveError as e:
            print(f"✓ Exception levée correctement: {e}")
        
        print("✓ TEST 9 RÉUSSI: Protection contre les retours invalides fonctionnel\n")
    except Exception as e:
        print(f"✗ TEST 9 ÉCHOUÉ: {e}\n")
        raise


def test_10_persistence_donnees():
    """TEST 10: Fermer puis redémarrer l'application et vérifier la persistence"""
    afficher_test(10, "Fermer et redémarrer l'application - Vérifier persistence")
    
    try:
        # Créer une nouvelle bibliothèque (charge les données)
        bib2 = Bibliotheque(dossier_data="data")
        
        # Vérifier que les données ont été chargées
        print(f"\nDonnées chargées:")
        print(f"  - Livres: {len(bib2.livres)}")
        print(f"  - Adhérents: {len(bib2.adherents)}")
        print(f"  - Emprunts: {len(bib2.emprunts)}")
        
        assert len(bib2.livres) == 3, f"Erreur: devrait avoir 3 livres, en a {len(bib2.livres)}"
        assert len(bib2.adherents) == 3, f"Erreur: devrait avoir 3 adhérents, en a {len(bib2.adherents)}"
        assert len(bib2.emprunts) == 2, f"Erreur: devrait avoir 2 emprunts, en a {len(bib2.emprunts)}"
        
        # Vérifier quelques données
        livre = bib2.rechercher_livre_par_id("L001")
        assert livre.titre == "Le Petit Prince", "Erreur: titre du livre incorrect"
        assert livre.est_disponible(), "Erreur: L001 devrait être disponible après retour"
        print(f"✓ Livre L001 charge correctement: {livre}")
        
        adherent = bib2.rechercher_adherent_par_id("A001")
        assert adherent.prenom == "Moussa", "Erreur: prénom de l'adhérent incorrect"
        print(f"✓ Adhérent A001 chargé correctement: {adherent}")
        
        # Vérifier l'état des emprunts
        emprunts_actifs = [e for e in bib2.emprunts if e.est_actif()]
        emprunts_retournes = [e for e in bib2.emprunts if not e.est_actif()]
        
        print(f"\n✓ Emprunts actifs: {len(emprunts_actifs)}")
        print(f"✓ Emprunts retournés: {len(emprunts_retournes)}")
        
        assert len(emprunts_actifs) == 1, "Erreur: 1 emprunt actif attendu"
        assert len(emprunts_retournes) == 1, "Erreur: 1 emprunt retourné attendu"
        
        print("\n✓ TEST 10 RÉUSSI: Persistence des données fonctionnelle\n")
        
    except Exception as e:
        print(f"✗ TEST 10 ÉCHOUÉ: {e}\n")
        raise


def main():
    """Exécute tous les tests"""
    print("\n" + "="*60)
    print("EXÉCUTION DES 10 TESTS DE SCÉNARIOS")
    print("="*60)
    
    try:
        # Nettoyer les données anciennes
        nettoyer_data()
        
        # Exécuter les tests
        bib = test_1_ajouter_livre()
        test_2_afficher_livres(bib)
        test_3_rechercher_livre_existant(bib)
        test_4_rechercher_livre_inexistant(bib)
        bib = test_5_ajouter_adherent(bib)
        test_6_emprunter_livre_disponible(bib)
        test_7_emprunter_livre_deja_emprunte(bib)
        test_8_retourner_livre(bib)
        test_9_retourner_livre_non_emprunte(bib)
        
        # Sauvegarder avant le test 10
        bib.sauvegarder_donnees()
        
        # Test 10: Vérifier la persistence
        test_10_persistence_donnees()
        
        # Afficher le résumé
        print("="*60)
        print("RÉSUMÉ FINAL")
        print("="*60)
        print("✓ TOUS LES TESTS RÉUSSIS (10/10)")
        print("="*60 + "\n")
        
        return True
        
    except Exception as e:
        print("\n" + "="*60)
        print("ERREUR: Un test a échoué")
        print("="*60 + "\n")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
