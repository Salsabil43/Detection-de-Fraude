from fastapi import FastAPI, Request
import pandas as pd
import joblib

app = FastAPI()

# Charger le pipeline entraine
pipeline = joblib.load("pipeline.joblib")

# Seuil de décision (orienté F2-score)
THRESHOLD = 0.5 # on met ici le meilleur score que j'ai 

@app.get("/")
def root():
    return {"message": "Fraud Detection API"}

# Health check
@app.get("/health")
def health():
    return {"status": "API is running"}

# Prediction
@app.post("/predict")
async def predict(request: Request):
    try:
        data = await request.json()
    
    # Conversion en DataFrame (format attendu par sklearn)
        X = pd.DataFrame([data])
    
        """prediction = pipeline.predict(X)[0]
        probability = pipeline.predict_proba(X)[0][1]
        """
    # Probabilité de fraude (classe 1)
        probability = pipeline.predict_proba(X)[0][1]
    # Décision basée sur le seuil choisi
        prediction = int(probability >= THRESHOLD)

        return {
            "fraud_prediction": prediction,
            "fraud_probability": round(float(probability), 4),
            "threshold_used": THRESHOLD
        }

    except Exception as e:
        # Log côté serveur (terminal)
        print(" Erreur API :", str(e))

        # Réponse propre côté client
        raise HTTPException(
            status_code=400,
            detail=f"Prediction error: {str(e)}"
        )

#uvicorn api:app --reload
#ouvre un autre terminal :python client_test.py
#url = "http://127.0.0.1:8000/health"
