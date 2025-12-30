import requests
import pandas as pd
from sklearn.metrics import classification_report, fbeta_score

# =========================
# 1) Charger les données de test
# =========================
df_test = pd.read_csv("data/split/X_test.csv")
y_true = pd.read_csv("data/split/y_test.csv")["is_fraud"]

# =========================
# 2) URL de l’API
# =========================
url = "http://127.0.0.1:8000/predict"

# =========================
# 3) Prédictions via API
# =========================
y_pred = []

for _, row in df_test.iterrows():
    payload = row.where(pd.notnull(row),None).to_dict()    
    response = requests.post(url, json=payload).json()
    y_pred.append(response["fraud_prediction"])


# =========================
# 4) Évaluation
# =========================
print(classification_report(y_true, y_pred))
print("F2-score :", fbeta_score(y_true, y_pred, beta=2))
