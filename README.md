# Heart Disease Prediction Web Application

A full-stack web application for heart disease prediction using trained machine learning models. The application features a FastAPI backend and a modern, responsive frontend.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)

## 🎯 Overview

This application provides an intuitive web interface for predicting heart disease risk using two machine learning models:
- **Logistic Regression**: Linear classification model
- **Decision Tree**: Tree-based classification model

Users can input patient data through a web form and receive predictions from both models with confidence scores.

## ✨ Features

- 🎨 Modern, responsive UI design
- 🤖 Dual model predictions (Logistic Regression + Decision Tree)
- 📊 Confidence scores for each prediction
- ✅ Input validation
- 🚀 FastAPI backend with automatic API documentation
- 📱 Mobile-friendly interface
- 🔒 CORS-enabled for cross-origin requests

## 📁 Project Structure

```
heart-disease-prediction-app/
├── backend/
│   ├── app.py                    # FastAPI application
│   ├── requirements.txt          # Python dependencies
│   └── models/                   # Trained ML models
│       ├── logistic_regression_model.joblib
│       ├── decision_tree_model.joblib
│       ├── scaler.joblib
│       └── feature_names.joblib
├── frontend/
│   ├── index.html               # Main HTML file
│   ├── style.css                # Styling
│   └── script.js                # Frontend logic
└── README.md
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure model files are in the `backend/models/` directory:
   - `logistic_regression_model.joblib`
   - `decision_tree_model.joblib`
   - `scaler.joblib` (optional, if used)
   - `feature_names.joblib` (optional, if used)

### Frontend Setup

The frontend is served by the FastAPI backend, so no separate setup is required.

## 📖 Usage

### Running Locally

1. Start the FastAPI server:
```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

3. Fill in the patient data form and click "Predict"

### Input Fields

- **Age**: Patient's age in years (1-120)
- **Sex**: 0 = Female, 1 = Male
- **Chest Pain Type**: 0-3 (various types)
- **Resting BP**: Resting blood pressure (80-250)
- **Cholesterol**: Serum cholesterol in mg/dl (100-600)
- **Fasting BS**: Fasting blood sugar > 120 mg/dl (0 or 1)
- **Rest ECG**: Resting ECG results (0-2)
- **Max Heart Rate**: Maximum heart rate achieved (60-220)
- **Exercise Angina**: Exercise induced angina (0 or 1)
- **Oldpeak**: ST depression induced by exercise (0.0-10.0)
- **Slope**: Slope of peak exercise ST segment (0-2)
- **CA**: Number of major vessels colored by flourosopy (0-4)
- **Thal**: Thalassemia (0-3)

## 📡 API Documentation

### Endpoints

#### GET `/`
Returns the main HTML page or API information.

#### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "models_loaded": true
}
```

#### POST `/predict`
Predicts heart disease using both models.

**Request Body:**
```json
{
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
}
```

**Response:**
```json
{
  "logistic_regression": {
    "prediction": 1,
    "probability": 0.8234,
    "prediction_label": "Heart Disease: Yes"
  },
  "decision_tree": {
    "prediction": 1,
    "probability": 0.7891,
    "prediction_label": "Heart Disease: Yes"
  }
}
```

### Interactive API Documentation

FastAPI provides automatic interactive documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🚀 Deployment

### Option 1: Railway (Recommended for Backend)

1. Create a `Procfile` in the backend directory:
```
web: uvicorn app:app --host 0.0.0.0 --port $PORT
```

2. Push to GitHub and connect to Railway
3. Set environment variables if needed
4. Deploy!

### Option 2: Render

1. Create a `render.yaml` file
2. Connect your GitHub repository
3. Configure the service
4. Deploy!

### Option 3: Vercel (For Frontend + Backend)

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Create `vercel.json` in the root:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "backend/app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/predict",
      "dest": "backend/app.py"
    },
    {
      "src": "/health",
      "dest": "backend/app.py"
    },
    {
      "src": "/(.*)",
      "dest": "backend/app.py"
    }
  ]
}
```

3. Deploy:
```bash
vercel
```

### Environment Variables

For production, consider setting:
- `ALLOWED_ORIGINS`: Comma-separated list of allowed CORS origins
- `PORT`: Server port (default: 8000)

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **Joblib**: Model loading
- **Scikit-learn**: Model inference
- **Pandas**: Data manipulation

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with modern features
- **JavaScript (ES6+)**: Client-side logic
- **Fetch API**: HTTP requests

## 📝 Notes

- The models must be trained and exported from the ML pipeline project
- Ensure model files are in the correct directory before running
- For production, restrict CORS origins to your frontend domain
- Consider adding authentication for production use

## 🔗 Related Projects

- [ML Pipeline](../heart-disease-ml-pipeline/): Training and model export

## 📄 License

This project is for educational purposes.

## 👤 Author

Created as part of a machine learning assignment.

---

**Live Demo**: [Deployment URL will be added after deployment]

