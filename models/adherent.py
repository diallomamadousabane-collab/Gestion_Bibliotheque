"""
Module contenant la classe Adherent
"""


class Adherent:
    """Classe représentant un adhérent de la bibliothèque"""
    
    def __init__(self, id, nom, prenom, telephone, email):
        """
        Initialise un adhérent
        
        Args:
            id: Identifiant unique de l'adhérent
            nom: Nom de famille
            prenom: Prénom
            telephone: Numéro de téléphone
            email: Adresse email
        """
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
    
    def get_nom_complet(self):
        """Retourne le nom complet de l'adhérent"""
        return f"{self.prenom} {self.nom}"
    
    def modifier_telephone(self, nouveau_telephone):
        """Modifie le numéro de téléphone"""
        self.telephone = nouveau_telephone
    
    def modifier_email(self, nouvel_email):
        """Modifie l'adresse email"""
        self.email = nouvel_email
    
    def to_dict(self):
        """Convertit l'adhérent en dictionnaire (pour JSON)"""
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'telephone': self.telephone,
            'email': self.email
        }
    
    @staticmethod
    def from_dict(data):
        """Crée un adhérent à partir d'un dictionnaire"""
        return Adherent(
            id=data['id'],
            nom=data['nom'],
            prenom=data['prenom'],
            telephone=data['telephone'],
            email=data['email']
        )
    
    def __str__(self):
        """Représentation textuelle de l'adhérent"""
        return f"ID: {self.id} | Nom: {self.nom} | Prénom: {self.prenom} | Téléphone: {self.telephone} | Email: {self.email}"
    
    def __repr__(self):
        """Représentation pour le débogage"""
        return f"Adherent({self.id}, {self.nom}, {self.prenom})"
