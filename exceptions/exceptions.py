"""
Exceptions personnalisées pour l'application de gestion de bibliothèque
"""


class LivreIndisponibleError(Exception):
    """Exception levée quand on tente d'emprunter un livre déjà emprunté"""
    pass


class LivreNonTrouveError(Exception):
    """Exception levée quand un livre n'existe pas"""
    pass


class AdherentNonTrouveError(Exception):
    """Exception levée quand un adhérent n'existe pas"""
    pass


class EmpruntNonTrouveError(Exception):
    """Exception levée quand un emprunt n'existe pas"""
    pass


class AdhérentDoublonError(Exception):
    """Exception levée quand on essaie d'ajouter un adhérent avec un ID existant"""
    pass


class LivreDoublonError(Exception):
    """Exception levée quand on essaie d'ajouter un livre avec un ID existant"""
    pass
