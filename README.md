# Détection de Fraude Bancaire

Projet de détection de fraude bancaire — pipeline Python complet pour l’entraînement,
l’évaluation et le déploiement d’un modèle de classification via une API.


## Aperçu

Ce projet met en place un **workflow reproductible de Machine Learning** appliqué à la
détection de fraudes bancaires.  
Il couvre l’ensemble du cycle de vie d’un modèle : préparation des données,
entraînement, évaluation et déploiement sous forme d’API REST.

L’objectif principal est de **réduire les fraudes non détectées**, un enjeu critique
dans le secteur bancaire.

## Objectifs du projet

- Construire un pipeline Machine Learning robuste
- Appliquer un prétraitement adapté aux données bancaires
- Éviter toute fuite de données (*data leakage*)
- Optimiser le modèle pour la détection de fraude
- Déployer le modèle via une API FastAPI
- Tester et évaluer le modèle en conditions réelles


## Contenu du dépôt

- `data/Dataset_Fraude.csv` : jeu de données source  
- `split_data.py` : script de séparation train / test  
- `fraud_cc.ipynb` : analyse exploratoire des données (EDA)  
- `preprocess_banque_fraud_data.ipynb` : prétraitement et préparation des données  
- `train_pipeline.ipynb` : entraînement et validation du modèle  
- `pipeline.joblib` : pipeline entraîné (préprocessing + modèle)  
- `api.py` : API FastAPI pour servir le modèle  
- `client_test.py` : test simple de l’API  
- `client_test_eval.py` : évaluation complète via l’API  
- `requirements.txt` : dépendances Python  

Des fichiers intermédiaires (CSV prétraités) peuvent également être présents.


## Prérequis

- Python 3.8 ou plus
- pip


### Créer un environnement virtuel 
``` bash
python -m venv .venv
```

### Installation des dépendances  
pip install -r requirements.txt

### Préparation des données

Placez le fichier Dataset_Fraude.csv dans le dossier data/, puis exécutez :

``` bash 
python split_data.py
``` 

Les fichiers suivants seront générés :

- X_train.csv

- X_test.csv

- y_train.csv

- y_test.csv

La séparation est réalisée avant le preprocessing afin d’éviter toute fuite de données (data leakage).

### Entraînement du modèle

L’entraînement est réalisé dans le notebook :

``` bash 
jupyter notebook train_pipeline.ipynb
```

À la fin de l’entraînement, le pipeline complet est sauvegardé dans :

``` bash 
pipeline.joblib
``` 
### Déploiement de l’API

Lancer l’API FastAPI localement :
``` bash 
uvicorn api:app --reload
```

Endpoints disponibles :

    /health : état de l’API

    /predict : prédiction de fraude

#### Technologies utilisées

- Python

- Pandas

- Scikit-learn

- FastAPI

- Joblib


### Améliorations possibles

- Optimisation avancée des hyperparamètres

- Seuil de décision dynamique

- Ajout de tests unitaires

- Déploiement avec Docker

- Monitoring en production
