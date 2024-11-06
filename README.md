
# pyStat

`pyStat` est une application Python pour effectuer des statistiques simples et doubles.

## Aperçu

Les version compiler en application windows sont disponible dans dans les [releases]('https://github.com/FaouzKK/PyStat/releases').

## Structure du projet

Le projet est structuré de la manière suivante :

- `src/` : Contient le code source de l'application.

## Fonctionnalités

- Entrée manuelle de données.
- Calcul automatique de statistiques de base (moyenne, écart-type, etc.).
  
## Prérequis

Avant de commencer, assurez-vous que vous avez les éléments suivants installés :

- Python 3.7+ (recommandé Python 3.12+)
- Pip (pour gérer les dépendances)

### Dépendances

Pour installer les dépendances nécessaires, utilisez le fichier `requirements.txt` fourni dans ce dépôt :

```bash
pip install -r requirements.txt
```

Les principales bibliothèques utilisées sont :

- **PySide6** : pour l'interface graphique.

## Installation

### 1. Clonez le dépôt

```bash
git clone https://github.com/votre-utilisateur/pyStat.git
cd pyStat
```

### 2. Créez un environnement virtuel

Il est recommandé de créer un environnement virtuel pour isoler les dépendances de votre projet :

```bash
python -m venv venv
```

### 3. Activez l'environnement virtuel

#### Sur Windows :
```bash
.env\Scripts\activate
```

#### Sur macOS/Linux :
```bash
source venv/bin/activate
```

### 4. Installez les dépendances

```bash
pip install -r requirements.txt
```

### 5. Lancez l'application

Vous pouvez démarrer l'application en exécutant le fichier principal du projet :

```bash
python src/app.py
```

## Utilisation

1. Lancez l'application.
2. Entrez vos données dans le formulaire.
3. Appuyez sur "Continuer" pour afficher les résultats statistiques.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer l'application ou si vous avez trouvé un bug, n'hésitez pas à soumettre une **pull request** ou à ouvrir une **issue**.

### Étapes pour contribuer :

1. Fork ce dépôt.
2. Créez une nouvelle branche (`git checkout -b feature/amélioration`).
3. Effectuez vos modifications.
4. Testez vos changements.
5. Soumettez une pull request.

## License

Ce projet est sous la licence MIT. Voir le fichier [MIT](LICENSE) pour plus d'informations.

## Aide

Si vous rencontrez des problèmes ou avez des questions, vous pouvez ouvrir une issue dans ce dépôt.
