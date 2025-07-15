```
scalable_model/               # Racine du projet ML scalable
│
├── data/                     # Répertoire pour gérer les données du projet
│   ├── raw/                  # Données brutes non modifiées (CSV initiaux, etc.)
│   └── processed/            # Données nettoyées et transformées prêtes pour l'entraînement
│
├── notebooks/                # Notebooks Jupyter pour exploration et prototypage
│
├── api/                      # Répertoire pour l'API FastAPI (prédiction)
│   ├── main.py               # Entrypoint de l’API REST pour servir le modèle
│   ├── model_loader.py       # Charger le modèle entraîné pour la prédiction
│   ├── requirements.txt      # Dépendances spécifiques à l'API FastAPI
│   └── Dockerfile            # Image Docker pour conteneuriser l’API de prédiction
│
│   ├── training/             # Pipeline d'entraînement ML pour l'API FastAPI
│   │   ├── train.py          # Script principal pour entraîner le modèle
│   │   ├── preprocess.py     # Script pour prétraiter/transformer les données
│   │   ├── evaluate.py       # Évaluer les performances du modèle entraîné
│   │   └── model.py          # Définition de l'architecture et sauvegarde du modèle
│
├── database/                 # Microservice pour gérer la base de données et migrations
│   ├── models/               # Dossier pour les modèles de données SQLAlchemy
│   │   ├── __init__.py       # Fichier d'initialisation du module schema
│   │   └── user_model.py     # Exemple de schéma SQL alchemy pour les utilisateurs
│   ├── schemas/              # Dossier pour les schémas Pydantic
│   │   ├── __init__.py       # Fichier d'initialisation du module schema
│   │   └── user_schema.py    # Exemple de schéma Pydantic pour les utilisateurs
│   ├── crud/                 # Fonctions CRUD (Create, Read, Update, Delete)
│   ├── database.py           # Création de la session DB, moteur SQLAlchemy
│   ├── main.py               # Entrypoint FastAPI pour exposer l’API interne de la BDD
│   ├── alembic.ini           # Fichier de configuration Alembic
│   ├── migrations/           # Scripts de migration générés par Alembic
│   ├── alembic/              # Répertoire pour `env.py` et `versions/` Alembic
│   ├── requirements.txt      # Dépendances spécifiques au service DB
│   └── Dockerfile            # Image Docker pour conteneuriser l’API BDD + migrations
│
│   └── modules/              # Dossier pour les modules liés à la gestion de la DB
│   │   ├── __init__.py       # Fichier d'initialisation du module schema
│   │   └── db_helpers.py    # Exemple de schéma Pydantic pour les utilisateurs
|
├── monitoring/               # Configuration pour le monitoring avec Kuma, Prometheus & Grafana
│   ├── kuma/                 # Configs spécifiques à Kuma pour collecter des métriques
│   │   ├── kuma_config.yml   # Configuration principale pour Kuma
│   │   └── kuma_agent.yml    # Agent Kuma à déployer dans chaque service pour collecter les métriques
│   ├── prometheus/           # Config de Prometheus pour scraper les métriques
│   │   └── prometheus.yml    # Fichier de configuration de Prometheus pour scraper Kuma
│   ├── grafana/              # Configs Grafana : dashboards et datasources
│   │   ├── dashboards/       # Définition des dashboards Grafana
│   │   │   ├── dashboards.yml  # Fichier d'import pour dashboards
│   │   │   └── system-dashboard.yml # Exemple de dashboard système
│   │   ├── datasources/      # Config datasources Grafana (Prometheus, DB, etc.)
│   │   │   └── datasource.yml # Définition des connexions datasources
│   └── Dockerfile            # Image Docker pour conteneuriser les services de monitoring
│
├── mlruns/                   # Dossier pour stocker les artefacts modèles versionnés via MLflow
│   ├── model_v1/             # Version 1 du modèle sauvegardée (fichiers MLflow)
│   └── model_v2/             # Version 2 du modèle (itération améliorée)
│
├── tests/                    # Tests unitaires et tests end-to-end
│   ├── test_training.py      # Tests pour vérifier le pipeline d'entraînement
│   ├── test_api.py           # Tests pour l'API de prédiction (routes, réponse)
│   ├── test_db.py            # Tests pour l'API BDD (CRUD, connexion)
│   └── test_monitoring.py    # Tests basiques du monitoring (endpoint Kuma)
│
├── docker-compose.yml        # Orchestration multi-conteneurs (API, DB, monitoring)
├── Makefile                  # Commandes utiles : lint, test, build, format, etc.
├── requirements.txt          # Dépendances globales pour tout le projet
├── .env                      # Variables d'environnement (ex. : URL DB, secrets)
├── .gitignore                # Fichiers/dossiers à ignorer dans le versioning Git
└── README.md                 # Documentation principale : usage, architecture, setup
```