# Gestion de Bibliothèque Python

## 1. Nom du projet
**Application de Gestion de Bibliothèque**

## 2. Description
Une application console permettant de gérer complètement une petite bibliothèque. L'application permet de gérer les livres, les adhérents et les emprunts avec une sauvegarde automatique des données en JSON.

## 3. Objectifs
- Concevoir une application structurée et facile à utiliser
- Utiliser la programmation orientée objet (POO)
- Manipuler des fichiers JSON pour la persistance des données
- Gérer les erreurs et exceptions de manière appropriée
- Démontrer la maîtrise de Git et GitHub
- Mettre en pratique les bonnes pratiques de développement

## 4. Fonctionnalités

### Gestion des Livres
- ✓ Ajouter un nouveau livre avec ID, titre, auteur, année, genre
- ✓ Modifier les informations d'un livre
- ✓ Supprimer un livre
- ✓ Afficher tous les livres
- ✓ Rechercher un livre par ID, titre ou auteur
- ✓ Vérifier la disponibilité d'un livre

### Gestion des Adhérents
- ✓ Ajouter un nouvel adhérent
- ✓ Modifier les informations d'un adhérent
- ✓ Supprimer un adhérent
- ✓ Afficher tous les adhérents
- ✓ Rechercher un adhérent par nom

### Gestion des Emprunts
- ✓ Emprunter un livre (vérification de disponibilité automatique)
- ✓ Retourner un livre
- ✓ Afficher tous les emprunts
- ✓ Gestion des emprunts actifs et des retours

### Gestion des Données
- ✓ Sauvegarde automatique au démarrage
- ✓ Sauvegarde manuelle des données
- ✓ Persistance en fichiers JSON
- ✓ Chargement automatique des données existantes

## 5. Technologies utilisées
- **Langage**: Python 3.6+
- **Format de données**: JSON
- **Structure**: Programmation Orientée Objet (POO)
- **Gestion de version**: Git
- **Plateforme**: GitHub
- **Aucune dépendance externe requise** (utilise uniquement la stdlib Python)

## 6. Structure du projet

```
bibliotheque-python/
├── main.py                 # Point d'entrée de l'application
├── models/                 # Package des modèles de données
│   ├── __init__.py
│   ├── livre.py           # Classe Livre
│   ├── adherent.py        # Classe Adherent
│   └── emprunt.py         # Classe Emprunt
├── services/              # Package des services
│   ├── __init__.py
│   └── bibliotheque.py    # Classe Bibliotheque (logique principale)
├── exceptions/            # Package des exceptions personnalisées
│   ├── __init__.py
│   └── exceptions.py      # Exceptions personnalisées
├── data/                  # Dossier des données JSON
│   ├── livres.json
│   ├── adherents.json
│   └── emprunts.json
├── .gitignore             # Fichiers à ignorer par Git
├── requirements.txt       # Dépendances du projet
└── README.md              # Ce fichier
```

## 7. Installation

### Prérequis
- Python 3.6 ou supérieur
- Git (pour le contrôle de version)

### Étapes d'installation

1. Clonez le dépôt:
```bash
git clone https://github.com/votre-username/gestion-bibliotheque-python.git
cd gestion-bibliotheque-python
```

2. (Optionnel) Créez un environnement virtuel:
```bash
# Sur Windows
python -m venv venv
venv\Scripts\activate

# Sur Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Installez les dépendances (optionnel, aucune requise pour l'application):
```bash
pip install -r requirements.txt
```

## 8. Exécution

Pour lancer l'application:

```bash
python main.py
```

L'application affichera un menu principal avec les options disponibles.

## 9. Utilisation

### Menu Principal
```
GESTION DE BIBLIOTHÈQUE
==================================================
1.  Ajouter un livre
2.  Modifier un livre
3.  Supprimer un livre
4.  Rechercher un livre
5.  Afficher les livres
6.  Ajouter un adhérent
7.  Afficher les adhérents
8.  Modifier un adhérent
9.  Supprimer un adhérent
10. Emprunter un livre
11. Retourner un livre
12. Afficher les emprunts
13. Sauvegarder les données
14. Quitter
```

### Exemple d'utilisation

#### Ajouter un livre
```
Choix: 1
ID du livre: L001
Titre: Le Petit Prince
Auteur: Antoine de Saint-Exupéry
Année de publication: 1943
Genre: Conte
```

#### Ajouter un adhérent
```
Choix: 6
ID de l'adhérent: A001
Nom: DIOP
Prénom: Moussa
Téléphone: 77 000 00 00
Email: moussa@example.com
```

#### Emprunter un livre
```
Choix: 10
ID du livre: L001
ID de l'adhérent: A001
✓ Moussa DIOP a emprunté 'Le Petit Prince'
```

#### Retourner un livre
```
Choix: 11
ID du livre: L001
ID de l'adhérent: A001
✓ Moussa DIOP a retourné 'Le Petit Prince'
```

## 10. Gestion de Git

### Initialisation du projet
```bash
git init
git add .
git commit -m "Initialisation du projet"
```

### Branches utilisées
- `main`: Branche principale (stable)
- `develop`: Branche de développement
- `feature/livres`: Gestion des livres
- `feature/adherents`: Gestion des adhérents
- `feature/emprunts`: Gestion des emprunts

### Workflow typique
```bash
# Créer une branche de fonctionnalité
git checkout -b feature/livres

# Faire des modifications et commits
git add .
git commit -m "Ajout de la classe Livre"

# Pousser la branche
git push origin feature/livres

# Créer une Pull Request sur GitHub
# Puis fusionner dans develop
```

## 11. Difficultés rencontrées

### Gestion des emprunts
**Problème**: Gérer correctement l'état des livres (disponible/emprunté) en relation avec les emprunts.

**Solution**: Créer une classe Emprunt dédiée qui maintient les associations entre livres et adhérents, et mettre à jour l'état du livre lors de chaque emprunt/retour.

### Persistance des données
**Problème**: Charger et sauvegarder les données JSON correctement avec les encodages accents.

**Solution**: Utiliser `encoding='utf-8'` lors de l'ouverture des fichiers et `ensure_ascii=False` dans json.dump().

### Gestion des IDs
**Problème**: Générer automatiquement des IDs uniques pour les emprunts.

**Solution**: Implémenter une méthode `_generer_id_emprunt()` qui extrait le numéro du dernier emprunt et l'incrémente.

### Recherche d'emprunts actifs
**Problème**: Trouver l'emprunt actif (non retourné) d'un livre pour permettre le retour.

**Solution**: Parcourir la liste des emprunts en filtrant par ID livre, ID adhérent et date_retour=None.

