"""
Module contenant la classe Livre
"""


class Livre:
    """Classe représentant un livre dans la bibliothèque"""
    
    def __init__(self, id, titre, auteur, annee, genre, disponible=True):
        """
        Initialise un livre
        
        Args:
            id: Identifiant unique du livre
            titre: Titre du livre
            auteur: Auteur du livre
            annee: Année de publication
            genre: Genre littéraire
            disponible: État de disponibilité (True par défaut)
        """
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre
        self.disponible = disponible
    
    def marquer_indisponible(self):
        """Marque le livre comme indisponible"""
        self.disponible = False
    
    def marquer_disponible(self):
        """Marque le livre comme disponible"""
        self.disponible = True
    
    def est_disponible(self):
        """Retourne True si le livre est disponible"""
        return self.disponible
    
    def to_dict(self):
        """Convertit le livre en dictionnaire (pour JSON)"""
        return {
            'id': self.id,
            'titre': self.titre,
            'auteur': self.auteur,
            'annee': self.annee,
            'genre': self.genre,
            'disponible': self.disponible
        }
    
    @staticmethod
    def from_dict(data):
        """Crée un livre à partir d'un dictionnaire"""
        return Livre(
            id=data['id'],
            titre=data['titre'],
            auteur=data['auteur'],
            annee=data['annee'],
            genre=data['genre'],
            disponible=data.get('disponible', True)
        )
    
    def __str__(self):
        """Représentation textuelle du livre"""
        disponibilite = "Disponible" if self.disponible else "Emprunté"
        return f"ID: {self.id} | Titre: {self.titre} | Auteur: {self.auteur} | Année: {self.annee} | Genre: {self.genre} | {disponibilite}"
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return f"Livre({self.id}, {self.titre}, {self.auteur})"
