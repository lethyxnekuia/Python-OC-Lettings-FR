<p align="center">
  <img src="https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png" />
</p>

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


# Pipeline CI/CD pour Django

Ce dépôt utilise GitHub Actions pour mettre en œuvre un pipeline de Continuous Integration (CI) et de Continuous Deployment (CD) pour une application Django. Le pipeline se déclenche à chaque push et pull request sur la branche `master`.

## Déploiement

L'application est déployée automatiquement via le pipeline CI/CD.

### Prérequis

- Disposer d'un compte sur les services SaaS suivants : GitHub Actions, Docker Hub, Render.
- Configurer dans les paramètres du dépot github les variables d'environnement pour le projet GitHub Actions :
  - `DOCKER_USERNAME`: identifiant du compte Docker Hub
  - `DOCKER_PASSWORD`: mot de passe du compte Docker Hub
  - `RENDER_API_KEY`: clé API de l'application sur Render
  - `RENDER_API_ID`: ID API de l'application sur Render

### Récapitulatif

Chaque push sur le repository GitHub déclenche un workflow de GitHub Actions :

- (workflow *test*) Si la modification concerne la branche `master`, les étapes suivantes sont exécutées :
  - `checkout code`: le code source est récupéré depuis le repository.
  - `set up python`: l'environnement est configuré avec Python 3.11.
  - `install dependencies`: les dépendances listées dans `requirements.txt` sont installées.
  - `run flake8`: le code est analysé pour détecter les problèmes de style et de syntaxe.
  - `set up django db`: la base de données est migrée pour préparer les tests.
  - `run tests`: les tests sont exécutés avec `pytest` et un rapport de couverture est généré.
  - `upload coverage to codecov`: le rapport de couverture est téléchargé sur Codecov.

- (workflow *build_and_push*) Si le job `test` est réussi, les étapes suivantes sont exécutées :
  - `checkout code`: le code source est récupéré depuis le repository.
  - `set up docker buildx`: Docker Buildx est configuré pour construire des images multiplateformes.
  - `login to docker hub`: authentification à Docker Hub avec les identifiants fournis.
  - `build and push docker image`: l'image Docker de l'application est construite et poussée sur Docker Hub avec le tag `latest`.
  - `post build cleanup`: les images Docker inutilisées sont supprimées pour libérer de l'espace.
  - `trigger render deploy`: une requête de déploiement est envoyée à Render via leur API.

### Utilisation de Docker en local

```bash
docker compose build
docker compose up
```

Une fois le conteneur lancé, allez à l'adresse `http://localhost:80` pour accéder à l'application.

Documentation Docker : [https://docs.docker.com/](https://docs.docker.com/)


