from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
BASE_DIR = Path(__file__).parent
frontend_path = BASE_DIR / "frontend"
models_path = BASE_DIR / "models"

# Mount static files
if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")

# Load models
try:
    lr_model = joblib.load(models_path / "logistic_regression_model.joblib")
    dt_model = joblib.load(models_path / "decision_tree_model.joblib")
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    raise

# Feature order
feature_names = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
    'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
]

# Request schema
class PredictionRequest(BaseModel):
    age: int = Field(..., ge=1, le=120)
    sex: int = Field(..., ge=0, le=1)
    cp: int = Field(..., ge=0, le=3)
    trestbps: int = Field(..., ge=80, le=250)
    chol: int = Field(..., ge=100, le=600)
    fbs: int = Field(..., ge=0, le=1)
    restecg: int = Field(..., ge=0, le=2)
    thalach: int = Field(..., ge=60, le=220)
    exang: int = Field(..., ge=0, le=1)
    oldpeak: float = Field(..., ge=0.0, le=10.0)
    slope: int = Field(..., ge=0, le=2)
    ca: int = Field(..., ge=0, le=4)
    thal: int = Field(..., ge=0, le=3)

@app.get("/")
def root():
    index_path = frontend_path / "index.html"
    if index_path.exists():
        return FileResponse(index_path, media_type="text/html")

    return {"message": "Heart Disease Prediction API is running"}

@app.get("/")
def root():
    index_path = frontend_path / "index.html"
    if index_path.exists():
        return FileResponse(index_path, media_type="text/html")
    return {"message": "Heart Disease Prediction API is running"}


@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        df = pd.DataFrame([request.dict()])
        df = df[feature_names]

        def run_model(model):
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0][1]
            return {
                "prediction": int(pred),
                "probability": round(float(prob), 4),
                "prediction_label": "Heart Disease: Yes" if pred == 1 else "Heart Disease: No"
            }

        return {
            "logistic_regression": run_model(lr_model),
            "decision_tree": run_model(dt_model)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
