import pandas as pd
from sklearn.model_selection import train_test_split
import os

# =========================
# 1) Charger les données brutes
# =========================
df = pd.read_csv("data/Dataset_Fraude.csv")


# Séparer X / y
y = df["is_fraud"]
X = df.drop("is_fraud", axis=1)

# =========================
# 2) Split AVANT preprocessing
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 3) Sauvegarde
# =========================
os.makedirs("data/split", exist_ok=True)

X_train.to_csv("data/split/X_train.csv", index=False)
X_test.to_csv("data/split/X_test.csv", index=False)
y_train.to_frame(name="is_fraud").to_csv("data/split/y_train.csv", index=False)
y_test.to_frame(name="is_fraud").to_csv("data/split/y_test.csv", index=False)


print("✅ Split terminé et sauvegardé")
