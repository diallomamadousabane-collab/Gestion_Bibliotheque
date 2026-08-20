"""
Module contenant la classe Bibliotheque - Gestion complète de l'application
"""

import json
import os
from datetime import datetime
from pathlib import Path

from models.livre import Livre
from models.adherent import Adherent
from models.emprunt import Emprunt
from exceptions.exceptions import (
    LivreIndisponibleError,
    LivreNonTrouveError,
    AdherentNonTrouveError,
    EmpruntNonTrouveError,
    AdhérentDoublonError,
    LivreDoublonError
)


class Bibliotheque:
    """Classe principale pour gérer la bibliothèque"""
    
    def __init__(self, dossier_data="data"):
        """
        Initialise la bibliothèque
        
        Args:
            dossier_data: Dossier contenant les fichiers JSON
        """
        self.dossier_data = dossier_data
        self.livres = []
        self.adherents = []
        self.emprunts = []
        
        # Créer le dossier data s'il n'existe pas
        Path(self.dossier_data).mkdir(exist_ok=True)
        
        # Charger les données existantes
        self.charger_donnees()
    
    # ======================== GESTION DES LIVRES ========================
    
    def ajouter_livre(self, id_livre, titre, auteur, annee, genre):
        """Ajoute un nouveau livre à la bibliothèque"""
        try:
            # Vérifier si le livre existe déjà
            if self._livre_existe(id_livre):
                raise LivreDoublonError(f"Un livre avec l'ID {id_livre} existe déjà")
            
            livre = Livre(id_livre, titre, auteur, annee, genre)
            self.livres.append(livre)
            print(f"✓ Livre '{titre}' ajouté avec succès")
            return livre
        except LivreDoublonError as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def modifier_livre(self, id_livre, titre=None, auteur=None, annee=None, genre=None):
        """Modifie les informations d'un livre"""
        try:
            livre = self.rechercher_livre_par_id(id_livre)
            
            if titre:
                livre.titre = titre
            if auteur:
                livre.auteur = auteur
            if annee:
                livre.annee = annee
            if genre:
                livre.genre = genre
            
            print(f"✓ Livre {id_livre} modifié avec succès")
            return livre
        except LivreNonTrouveError as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def supprimer_livre(self, id_livre):
        """Supprime un livre de la bibliothèque"""
        try:
            livre = self.rechercher_livre_par_id(id_livre)
            self.livres.remove(livre)
            print(f"✓ Livre {id_livre} supprimé avec succès")
            return True
        except LivreNonTrouveError as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def rechercher_livre_par_id(self, id_livre):
        """Recherche un livre par son ID"""
        for livre in self.livres:
            if livre.id == id_livre:
                return livre
        raise LivreNonTrouveError(f"Livre avec l'ID {id_livre} non trouvé")
    
    def rechercher_livres_par_titre(self, titre):
        """Recherche des livres par titre (recherche partielle)"""
        resultats = [livre for livre in self.livres if titre.lower() in livre.titre.lower()]
        return resultats
    
    def rechercher_livres_par_auteur(self, auteur):
        """Recherche des livres par auteur"""
        resultats = [livre for livre in self.livres if auteur.lower() in livre.auteur.lower()]
        return resultats
    
    def afficher_tous_les_livres(self):
        """Affiche tous les livres"""
        if not self.livres:
            print("Aucun livre dans la bibliothèque")
            return
        
        print("\n" + "="*100)
        print("LISTE DES LIVRES")
        print("="*100)
        for livre in self.livres:
            print(livre)
        print("="*100 + "\n")
    
    def _livre_existe(self, id_livre):
        """Vérifie si un livre existe"""
        try:
            self.rechercher_livre_par_id(id_livre)
            return True
        except LivreNonTrouveError:
            return False
    
    # ======================== GESTION DES ADHÉRENTS ========================
    
    def ajouter_adherent(self, id_adherent, nom, prenom, telephone, email):
        """Ajoute un nouvel adhérent"""
        try:
            if self._adherent_existe(id_adherent):
                raise AdhérentDoublonError(f"Un adhérent avec l'ID {id_adherent} existe déjà")
            
            adherent = Adherent(id_adherent, nom, prenom, telephone, email)
            self.adherents.append(adherent)
            print(f"✓ Adhérent {prenom} {nom} ajouté avec succès")
            return adherent
        except AdhérentDoublonError as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def modifier_adherent(self, id_adherent, nom=None, prenom=None, telephone=None, email=None):
        """Modifie les informations d'un adhérent"""
        try:
            adherent = self.rechercher_adherent_par_id(id_adherent)
            
            if nom:
                adherent.nom = nom
            if prenom:
                adherent.prenom = prenom
            if telephone:
                adherent.modifier_telephone(telephone)
            if email:
                adherent.modifier_email(email)
            
            print(f"✓ Adhérent {id_adherent} modifié avec succès")
            return adherent
        except AdherentNonTrouveError as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def supprimer_adherent(self, id_adherent):
        """Supprime un adhérent"""
        try:
            adherent = self.rechercher_adherent_par_id(id_adherent)
            self.adherents.remove(adherent)
            print(f"✓ Adhérent {id_adherent} supprimé avec succès")
            return True
        except AdherentNonTrouveError as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def rechercher_adherent_par_id(self, id_adherent):
        """Recherche un adhérent par son ID"""
        for adherent in self.adherents:
            if adherent.id == id_adherent:
                return adherent
        raise AdherentNonTrouveError(f"Adhérent avec l'ID {id_adherent} non trouvé")
    
    def rechercher_adherents_par_nom(self, nom):
        """Recherche des adhérents par nom"""
        resultats = [adh for adh in self.adherents if nom.lower() in adh.nom.lower()]
        return resultats
    
    def afficher_tous_les_adherents(self):
        """Affiche tous les adhérents"""
        if not self.adherents:
            print("Aucun adhérent dans la bibliothèque")
            return
        
        print("\n" + "="*100)
        print("LISTE DES ADHÉRENTS")
        print("="*100)
        for adherent in self.adherents:
            print(adherent)
        print("="*100 + "\n")
    
    def _adherent_existe(self, id_adherent):
        """Vérifie si un adhérent existe"""
        try:
            self.rechercher_adherent_par_id(id_adherent)
            return True
        except AdherentNonTrouveError:
            return False
    
    # ======================== GESTION DES EMPRUNTS ========================
    
    def emprunter_livre(self, id_livre, id_adherent):
        """Permet à un adhérent d'emprunter un livre"""
        try:
            # Vérifier que le livre existe
            livre = self.rechercher_livre_par_id(id_livre)
            
            # Vérifier que l'adhérent existe
            adherent = self.rechercher_adherent_par_id(id_adherent)
            
            # Vérifier que le livre est disponible
            if not livre.est_disponible():
                raise LivreIndisponibleError(f"Le livre '{livre.titre}' n'est pas disponible")
            
            # Créer un nouvel emprunt
            id_emprunt = self._generer_id_emprunt()
            date_emprunt = datetime.now().strftime("%Y-%m-%d")
            emprunt = Emprunt(id_emprunt, id_livre, id_adherent, date_emprunt)
            
            # Marquer le livre comme indisponible
            livre.marquer_indisponible()
            
            # Ajouter l'emprunt
            self.emprunts.append(emprunt)
            
            print(f"✓ {adherent.get_nom_complet()} a emprunté '{livre.titre}'")
            return emprunt
        
        except (LivreNonTrouveError, AdherentNonTrouveError, LivreIndisponibleError) as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def retourner_livre(self, id_livre, id_adherent):
        """Permet à un adhérent de retourner un livre"""
        try:
            livre = self.rechercher_livre_par_id(id_livre)
            adherent = self.rechercher_adherent_par_id(id_adherent)
            
            # Trouver l'emprunt actif
            emprunt = None
            for emp in self.emprunts:
                if emp.id_livre == id_livre and emp.id_adherent == id_adherent and emp.est_actif():
                    emprunt = emp
                    break
            
            if not emprunt:
                raise EmpruntNonTrouveError(f"Aucun emprunt actif trouvé pour ce livre et cet adhérent")
            
            # Marquer le livre comme disponible
            livre.marquer_disponible()
            
            # Marquer l'emprunt comme retourné
            emprunt.retourner_livre()
            
            print(f"✓ {adherent.get_nom_complet()} a retourné '{livre.titre}'")
            return emprunt
        
        except (LivreNonTrouveError, AdherentNonTrouveError, EmpruntNonTrouveError) as e:
            print(f"✗ Erreur: {e}")
            raise
    
    def afficher_tous_les_emprunts(self):
        """Affiche tous les emprunts"""
        if not self.emprunts:
            print("Aucun emprunt enregistré")
            return
        
        print("\n" + "="*100)
        print("LISTE DES EMPRUNTS")
        print("="*100)
        for emprunt in self.emprunts:
            print(emprunt)
        print("="*100 + "\n")
    
    def _generer_id_emprunt(self):
        """Génère un nouvel ID unique pour un emprunt"""
        if not self.emprunts:
            return "E001"
        
        # Extraire le numéro du dernier emprunt et incrémenter
        derniers_ids = [int(e.id_emprunt[1:]) for e in self.emprunts]
        prochain_id = max(derniers_ids) + 1
        return f"E{prochain_id:03d}"
    
    # ======================== GESTION DES FICHIERS JSON ========================
    
    def charger_donnees(self):
        """Charge les données depuis les fichiers JSON"""
        self._charger_livres()
        self._charger_adherents()
        self._charger_emprunts()
    
    def _charger_livres(self):
        """Charge les livres depuis le fichier JSON"""
        fichier = os.path.join(self.dossier_data, "livres.json")
        try:
            if os.path.exists(fichier):
                with open(fichier, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    self.livres = [Livre.from_dict(livre_dict) for livre_dict in donnees]
                    print(f"✓ {len(self.livres)} livre(s) chargé(s)")
        except json.JSONDecodeError:
            print(f"✗ Erreur: Fichier JSON invalide ({fichier})")
        except Exception as e:
            print(f"✗ Erreur lors du chargement des livres: {e}")
    
    def _charger_adherents(self):
        """Charge les adhérents depuis le fichier JSON"""
        fichier = os.path.join(self.dossier_data, "adherents.json")
        try:
            if os.path.exists(fichier):
                with open(fichier, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    self.adherents = [Adherent.from_dict(adh_dict) for adh_dict in donnees]
                    print(f"✓ {len(self.adherents)} adhérent(s) chargé(s)")
        except json.JSONDecodeError:
            print(f"✗ Erreur: Fichier JSON invalide ({fichier})")
        except Exception as e:
            print(f"✗ Erreur lors du chargement des adhérents: {e}")
    
    def _charger_emprunts(self):
        """Charge les emprunts depuis le fichier JSON"""
        fichier = os.path.join(self.dossier_data, "emprunts.json")
        try:
            if os.path.exists(fichier):
                with open(fichier, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    self.emprunts = [Emprunt.from_dict(emp_dict) for emp_dict in donnees]
                    print(f"✓ {len(self.emprunts)} emprunt(s) chargé(s)")
        except json.JSONDecodeError:
            print(f"✗ Erreur: Fichier JSON invalide ({fichier})")
        except Exception as e:
            print(f"✗ Erreur lors du chargement des emprunts: {e}")
    
    def sauvegarder_donnees(self):
        """Sauvegarde toutes les données dans les fichiers JSON"""
        self._sauvegarder_livres()
        self._sauvegarder_adherents()
        self._sauvegarder_emprunts()
        print("✓ Données sauvegardées avec succès")
    
    def _sauvegarder_livres(self):
        """Sauvegarde les livres dans le fichier JSON"""
        fichier = os.path.join(self.dossier_data, "livres.json")
        try:
            donnees = [livre.to_dict() for livre in self.livres]
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde des livres: {e}")
    
    def _sauvegarder_adherents(self):
        """Sauvegarde les adhérents dans le fichier JSON"""
        fichier = os.path.join(self.dossier_data, "adherents.json")
        try:
            donnees = [adherent.to_dict() for adherent in self.adherents]
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde des adhérents: {e}")
    
    def _sauvegarder_emprunts(self):
        """Sauvegarde les emprunts dans le fichier JSON"""
        fichier = os.path.join(self.dossier_data, "emprunts.json")
        try:
            donnees = [emprunt.to_dict() for emprunt in self.emprunts]
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde des emprunts: {e}")
