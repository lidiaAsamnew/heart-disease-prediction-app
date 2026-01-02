# Heart Disease Prediction 

A full-stack web application for heart disease classification using Logistic Regression and Decision Tree models. The application features a FastAPI backend and a modern, responsive frontend.

## 🎯 Project Overview

This project implements a heart disease prediction system that:

- Uses two trained ML models: Logistic Regression and Decision Tree
- Provides a FastAPI backend for serving predictions
- Includes an interactive web UI for easy patient data input and result visualization
- Compares predictions from both models with confidence probabilities
- Demonstrates a complete end-to-end ML deployment pipeline

## 🏗️ Project Structure
```
heart-disease-prediction-app/
├── backend/
│   ├── app.py                         # FastAPI backend application
│   ├── requirements.txt               # Python dependencies
│   └── models/                        # Trained ML models
│       ├── logistic_regression_model.joblib
│       ├── decision_tree_model.joblib
│       ├── scaler.joblib
│       └── feature_names.joblib
├── frontend/
│   ├── index.html                     # Main HTML page
│   ├── style.css                      # Styling
│   └── script.js                      # JavaScript logic
└── README.md
```

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/heart-disease-prediction-app.git
cd heart-disease-prediction-app
```

### Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

## 🎓 Usage

### Step 1: Ensure Trained Models Are Available

Make sure the following files exist in `backend/models/`:

- `logistic_regression_model.joblib`
- `decision_tree_model.joblib`
- `scaler.joblib`
- `feature_names.joblib`

These models are trained and exported from the ML pipeline project.

### Step 2: Start the FastAPI Server

Launch the backend server:

```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The server will start at:

```
http://localhost:8000
```

### Step 3: Access the Web UI

Open your browser and navigate to:

```
http://localhost:8000
```

You can now:

- Enter patient clinical data
- Click **Predict** to get predictions from both models
- View and compare confidence probabilities

## 📊 Features

### Input Parameters

The system accepts the following patient features:

- **Age**: Age in years (1–120)
- **Sex**: 0 = Female, 1 = Male
- **Chest Pain Type (cp)**: 0–3
- **Resting Blood Pressure (trestbps)**: 80–250
- **Cholesterol (chol)**: 100–600 mg/dl
- **Fasting Blood Sugar (fbs)**: 0 or 1
- **Resting ECG (restecg)**: 0–2
- **Maximum Heart Rate (thalach)**: 60–220
- **Exercise Angina (exang)**: 0 or 1
- **Oldpeak**: ST depression (0.0–10.0)
- **Slope**: Slope of peak exercise ST segment (0–2)
- **CA**: Number of major vessels (0–4)
- **Thal**: Thalassemia (0–3)

## 📡 API Endpoints

- **GET `/`** – Serves the web UI
- **GET `/health`** – Health check endpoint
- **POST `/predict`** – Returns predictions from both ML models

## 📘 API Documentation

Interactive API documentation is available at:

- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`

## 🧪 Example API Request
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trestbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 2.3,
    "slope": 0,
    "ca": 0,
    "thal": 1
  }'
```

## 🎨 Web UI Features

- **Responsive Design** – Works on desktop, tablet, and mobile
- **Real-time Validation** – Input validation for all fields
- **Visual Comparison** – Side-by-side model results
- **Probability Visualization** – Confidence score display
- **Risk Assessment** – Combined interpretation of both models

## 🔬 Model Information

### Logistic Regression

- Linear model for binary classification
- High interpretability
- Works well with scaled numerical features

### Decision Tree

- Non-linear classification model
- Captures complex feature relationships
- Easy to understand decision paths

## 🚀 Deployment

This application is deployed using:

- **Backend** → Render (FastAPI API service)
- **Frontend** → Vercel (Static web application)

The backend serves the prediction API, while the frontend communicates with it using HTTP requests.

## 🌍 Live Demo

**Frontend (Vercel)**
https://heart-disease-prediction-81qt4sr40-lidiaasamnews-projects.vercel.app/

**Backend (Render)**
https://heart-disease-prediction-app-lfsn.onrender.com/

## 🛠️ Technologies Used

### Backend

- FastAPI
- Uvicorn
- Pydantic
- Scikit-learn
- Joblib
- Pandas

### Frontend

- HTML5
- CSS3
- JavaScript (ES6+)
- Fetch API

## 📝 Notes

- Models must be trained and exported before running the backend
- Ensure model files exist in the correct directory
- CORS should be restricted in production environments
- Authentication can be added for real-world usage

## 📄 License

This project is intended for educational and academic purposes only.

## 👤 Author

Developed as part of a Machine Learning assignment, demonstrating full-stack ML system development.

## 🌟 Acknowledgments

- Scikit-learn for machine learning tools
- FastAPI for backend framework
- Open heart disease datasets
