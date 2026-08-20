"""
Module contenant la classe Emprunt
"""

from datetime import datetime


class Emprunt:
    """Classe représentant un emprunt dans la bibliothèque"""
    
    def __init__(self, id_emprunt, id_livre, id_adherent, date_emprunt, date_retour=None):
        """
        Initialise un emprunt
        
        Args:
            id_emprunt: Identifiant unique de l'emprunt
            id_livre: Identifiant du livre emprunté
            id_adherent: Identifiant de l'adhérent qui emprunte
            date_emprunt: Date d'emprunt (format: YYYY-MM-DD)
            date_retour: Date de retour (None si non retourné)
        """
        self.id_emprunt = id_emprunt
        self.id_livre = id_livre
        self.id_adherent = id_adherent
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour
    
    def retourner_livre(self, date_retour=None):
        """Marque le livre comme retourné"""
        if date_retour is None:
            date_retour = datetime.now().strftime("%Y-%m-%d")
        self.date_retour = date_retour
    
    def est_actif(self):
        """Retourne True si l'emprunt est toujours actif (livre non retourné)"""
        return self.date_retour is None
    
    def to_dict(self):
        """Convertit l'emprunt en dictionnaire (pour JSON)"""
        return {
            'id_emprunt': self.id_emprunt,
            'id_livre': self.id_livre,
            'id_adherent': self.id_adherent,
            'date_emprunt': self.date_emprunt,
            'date_retour': self.date_retour
        }
    
    @staticmethod
    def from_dict(data):
        """Crée un emprunt à partir d'un dictionnaire"""
        return Emprunt(
            id_emprunt=data['id_emprunt'],
            id_livre=data['id_livre'],
            id_adherent=data['id_adherent'],
            date_emprunt=data['date_emprunt'],
            date_retour=data.get('date_retour', None)
        )
    
    def __str__(self):
        """Représentation textuelle de l'emprunt"""
        statut = "Actif" if self.est_actif() else f"Retourné le {self.date_retour}"
        return f"ID Emprunt: {self.id_emprunt} | Livre: {self.id_livre} | Adhérent: {self.id_adherent} | Emprunté le: {self.date_emprunt} | {statut}"
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return f"Emprunt({self.id_emprunt}, {self.id_livre}, {self.id_adherent})"
