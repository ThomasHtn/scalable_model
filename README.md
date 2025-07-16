# 🧠 Income Prediction – FastAPI, Alembic & MLflow
A full-stack machine learning pipeline to predict whether a person's income exceeds $50K/year based on census data.

This project combines modern MLOps tools and best practices to deliver a scalable, versioned, and production-ready ML system.

---

## 📦 Project structure

```
scalable_model/               # Racine du projet ML scalable
│
├── api/                      # API FastAPI exposant le modèle pour la prédiction
│   ├── main.py               # Entrypoint de l’API REST pour prédire les revenus
│   ├── model_loader.py       # Chargement du modèle et du préprocesseur sauvegardés
│   ├── requirements.txt      # Dépendances spécifiques à l’API
│   ├── Dockerfile            # Image Docker pour conteneuriser l’API
│   └── training/             # Module de pipeline d’entraînement
│       ├── train.py          # Script d'entraînement principal
│       ├── preprocess.py     # Prétraitement des données (pipeline scikit-learn)
│       ├── evaluate.py       # Évaluation des performances
│       ├── model.py          # Architecture du modèle (Keras)
│       └── __init__.py       # Initialisation du module
│
├── database/                 # Microservice de gestion de la base de données
│   ├── main.py               # API FastAPI exposant les endpoints CRUD
│   ├── db_init.py            # Script d'initialisation ou de remplissage de la base
│   ├── models/               # Modèles SQLAlchemy
│   │   └── user_model.py     # Modèle représentant un utilisateur
│   ├── schemas/              # Schémas Pydantic pour validation d’entrées
│   │   └── user_schema.py    # Schéma d’un utilisateur (UserIn, UserOut)
│   ├── crud/                 # Fonctions de lecture/écriture dans la base
│   │   └── user_crud.py      # CRUD pour la table `users`
│   ├── modules/              # Aides et scripts liés à la DB
│   │   └── populate_db.py    # Script pour insérer des données dans la DB
│   ├── alembic.ini           # Configuration Alembic
│   ├── alembic/              # Répertoire Alembic (migrations, env.py)
│   │   ├── env.py            # Configuration de l’environnement Alembic
│   │   └── versions/         # Fichiers de migration (auto-générés)
│   ├── requirements.txt      # Dépendances spécifiques au service DB
│   └── Dockerfile            # Image Docker pour conteneuriser le service BDD
│
├── data/                     # Données du projet
│   ├── raw/                  # Données brutes initiales (ex. adult.data)
│   └── processed/            # Données transformées/filtrées
│
├── dump/                     # Fichiers générés liés à la DB ou au dump SQL
│   └── generated-user.db     # Fichier SQLite contenant la table `users`
│
├── mlruns/                   # Dossier généré par MLflow pour le suivi d'expériences
│   └── ...                   # Contient les artefacts, métriques, modèles versionnés
│
├── model_artifacts/          # Fichiers finaux du modèle entraîné
│   ├── model1.keras          # Modèle Keras exporté
│   └── preprocessor2.pkl     # Pipeline de prétraitement sauvegardé (scikit-learn)
│
├── monitoring/               # Stack de monitoring (Grafana, Prometheus, Kuma)
│   ├── grafana/              # Configuration de Grafana
│   │   ├── dashboards/       # Dashboards custom
│   │   └── datasources/      # Sources de données pour Grafana
│   ├── prometheus/           # Fichier de configuration Prometheus
│   ├── kuma/                 # Configuration de Kuma (agent + dashboard)
│   └── Dockerfile            # Image Docker pour le service de monitoring
│
├── tests/                    # Tests unitaires et end-to-end
│   ├── test_api.py           # Tests de l’API de prédiction
│   ├── test_db.py            # Tests CRUD de l’API de la DB
│   ├── test_training.py      # Tests du pipeline d'entraînement
│   └── test_monitoring.py    # Vérifications basiques de l’intégration monitoring
│
├── assets/                   # Assets du projet (captures, visuels)
│   ├── api_swagger.png
│   ├── database_swagger.png
│   ├── grafana.png
│   └── mlflow-result.png
│
├── notebook.ipynb            # Notebook d’exploration (optionnel)
├── docker-compose.yml        # Orchestration multi-conteneurs avec Docker Compose
├── Makefile                  # Commandes CLI utiles (lint, test, format, build, etc.)
├── requirements.txt          # Dépendances globales du projet (hors services isolés)
├── .env                      # Fichier d’environnement (DB_URL, secrets, etc.)
├── .gitignore                # Fichiers/dossiers ignorés par Git
└── README.md                 # Documentation principale du projet
```
--- 

## 🌐 Virtual environment

**Linux**
```batch
python3 -m venv .venv
source .venv/bin/activate
```

**MacOS-Windows**
```batch
python -m venv .venv
.venv\Scripts\activate
```

---

## Alembic

**Créer une nouvelle migration**
Depuis la racine du projet :
```batch
alembic -c database/alembic.ini revision --autogenerate -m "nom de la migration"
```

**Appliquer la migration**
Depuis la racine du projet :
```batch
alembic -c database/alembic.ini upgrade head
```

---

## Database api 
Depuis la racine du projet
```batch
uvicorn database.main:app --reload
```

---

## Fastapi 
Depuis la racine du projet 
```batch
uvicorn api.main:app --host 0.0.0.0 --port 8500 --reload
```

Prédire une valeur avec curl 
```batch
curl -X POST http://localhost:8500/predict_income \
  -H "Content-Type: application/json" \
  -d '{
    "age": 39,
    "workclass": "State-gov",
    "fnlwgt": 77516,
    "education": "Bachelors",
    "education_num": 13,
    "marital_status": "Never-married",
    "occupation": "Adm-clerical",
    "relationship": "Not-in-family",
    "capital_gain": 2174,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": "United-States"
  }'
```
---

## Grafana 
![Grafana](/assets/grafana.png)

---

## Mlflow 
![Mlflow](/assets/mlflow-result.png)

---

## Api 
![api](/assets/api_swagger.png)

---

## Database 
![api](/assets/database_swagger.png)


## Comparaison avec CHAT GPT

Métriques du nouveau modèle
| Composant     | Valeur observée       | Interprétation                                                                 |
| ------------- | --------------------- | ------------------------------------------------------------------------------ |
| **CPU Busy**  | \~4.5 %               | Très faible charge. Usage classique d'un serveur avec trafic modéré.           |
| **RAM Used**  | \~32.9 % (sur 31 GiB) | Utilisation mémoire typique d’un environnement de test/production léger.       |
| **Disk Used** | Peu utilisé           | Système sain, stockage stable.                                                 |
| **Network**   | < 25 kb/s             | Faible trafic réseau (indique peu d’entrées/sorties ou peu de connexions API). |
| **CPU Cores** | 16                    | Machine puissante, mais dans une plage standard pour des workloads modestes.   |

Métriques de CHAT GPT
| Composant          | ChatGPT v4 – ordre de grandeur                     | Comparaison avec votre environnement                                                |
| ------------------ | -------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **CPU équivalent** | ≈ 20 000+ cœurs CPU pour les processus auxiliaires | Vous avez 16 cœurs → 1/1 250e de la capacité CPU d’un seul job OpenAI.              |
| **GPU**            | 10 000+ GPUs A100 40/80 Go sur plusieurs semaines  | Aucun GPU actif dans votre environnement (ou désactivé via `CUDA_VISIBLE_DEVICES`). |
| **RAM totale**     | Plusieurs To (teraoctets)                          | 31 GiB → \~0.003 % de la RAM totale d’un job d’entraînement de LLM.                 |
| **Bande passante** | Réseau InfiniBand 400 Gb/s par nœud                | Vous êtes à < 1 Mb/s → ≈ 1/400 000e de la bande passante d’un nœud OpenAI.          |
| **Coût énergie**   | Plusieurs millions de dollars                      | Probablement moins de quelques euros/jour pour votre serveur.                       |

Implication en matière de données personnelles

| Point de comparaison             | Votre système actuel                                             | ChatGPT (OpenAI, cloud-scale)                                                |
| -------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Traçabilité des utilisateurs** | Possible via IP/session/API logs                                 | Extrêmement fine (logs, prompt tracking, usage analytics)                    |
| **Sensibilité des données**      | Faible/modérée (données de recensement)                          | Potentiellement très élevée (données entrées librement par les utilisateurs) |
| **Risque RGPD**                  | Faible à modéré, mais réel si les logs ne sont pas pseudonymisés | Élevé : stockage mondial, traitement à très large échelle.                   |

**En bref** 

Même si l'infrastructure actuelle est 1000 à 1 000 000 fois plus petite que celle nécessaire à l’entraînement de ChatGPT :

Les principes de conformité restent les mêmes : chaque donnée collectée, même indirectement via monitoring, peut constituer une donnée personnelle.

L’effet cumulatif de logs, métriques système et journaux API peut permettre un profilage.

En 2025, les outils permettent de voir presque tout ce que fait un utilisateur contrairement à 1994. Cela change radicalement la responsabilité du DPO.