#Module 11
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from prediction import predict

app = FastAPI(
    title="Predictive Bioinformatics API",
    description="AI-Based Disease Prediction with Mutation Enhancement",
    version="1.0.0"
)

# ── REQUEST MODELS ─────────────────────────────────────────────
class DiabetesInput(BaseModel):
    Pregnancies             : int   = Field(..., ge=0,   le=20,   description="Number of pregnancies. Enter 0 if male.")
    Glucose                 : float = Field(..., ge=0,   le=300,  description="Blood glucose level. Normal: 70-99.")
    BloodPressure           : float = Field(..., ge=0,   le=200,  description="Diastolic blood pressure. Normal: 60-80.")
    SkinThickness           : float = Field(..., ge=0,   le=100,  description="Skin fold thickness. Normal: 10-40.")
    Insulin                 : float = Field(..., ge=0,   le=900,  description="Insulin level. Normal: 16-166.")
    BMI                     : float = Field(..., ge=0,   le=70,   description="Body Mass Index. Normal: 18.5-24.9.")
    DiabetesPedigreeFunction: float = Field(..., ge=0,   le=3,    description="Family history score. Typical: 0.08-2.42.")
    Age                     : int   = Field(..., ge=1,   le=120,  description="Patient age in years.")

class HeartInput(BaseModel):
    age     : int   = Field(..., ge=1,   le=120, description="Patient age in years.")
    trestbps: float = Field(..., ge=0,   le=250, description="Resting blood pressure. Normal: below 120.")
    chol    : float = Field(..., ge=0,   le=600, description="Cholesterol. Normal: below 200.")
    thalach : float = Field(..., ge=0,   le=250, description="Maximum heart rate. Normal: 100-170.")
    oldpeak : float = Field(..., ge=0.0, le=10,  description="ST depression. Normal: 0.")

class CancerInput(BaseModel):
    mean_radius        : float = Field(..., ge=0, le=50,   description="Average tumor radius. Benign: 6-15.")
    mean_texture       : float = Field(..., ge=0, le=50,   description="Texture of tumor. Typical: 9-40.")
    mean_perimeter     : float = Field(..., ge=0, le=250,  description="Tumor boundary size. Benign: 40-100.")
    mean_area          : float = Field(..., ge=0, le=2500, description="Tumor area. Benign: 100-800.")
    mean_smoothness    : float = Field(..., ge=0, le=1,    description="Smoothness of boundary. Typical: 0.05-0.16.")
    mean_compactness   : float = Field(..., ge=0, le=1,    description="Compactness. Typical: 0.02-0.35.")
    mean_concavity     : float = Field(..., ge=0, le=1,    description="Concavity. Typical: 0-0.43.")
    mean_concave_points: float = Field(..., ge=0, le=1,    description="Concave points. Typical: 0-0.20.")
    worst_radius       : float = Field(..., ge=0, le=50,   description="Largest radius. Typical: 7-36.")
    worst_area         : float = Field(..., ge=0, le=4000, description="Largest area. Typical: 185-4254.")

class GeneInput(BaseModel):
    mean_expression : float = Field(..., ge=0, le=5000, description="Average gene activity. Typical: 200-800.")
    std_expression  : float = Field(..., ge=0, le=5000, description="Gene activity variation. Typical: 100-400.")
    max_expression  : float = Field(..., ge=0, le=5000, description="Most active gene. Typical: 500-3000.")
    min_expression  : float = Field(..., ge=0, le=5000, description="Least active gene. Typical: 0-300.")
    expression_range: float = Field(..., ge=0, le=5000, description="Max minus Min expression.")
    mutation_flag   : int   = Field(..., ge=0, le=1,    description="0=normal, 1=unusual gene activity.")

class PredictionResponse(BaseModel):
    disease   : str
    prediction: str
    confidence: str
    status    : str


# ── ENDPOINTS ──────────────────────────────────────────────────
@app.get("/")
def home():
    return {
        "message"  : "Predictive Bioinformatics API is running",
        "version"  : "1.0.0",
        "endpoints": ["/predict/diabetes", "/predict/heart",
                      "/predict/cancer", "/predict/gene", "/health"]
    }

@app.get("/health")
def health_check():
    return {
        "status" : "healthy",
        "models" : ["cancer", "heart", "diabetes", "gene"],
        "message": "All 4 disease models are loaded and ready"
    }

@app.post("/predict/diabetes", response_model=PredictionResponse)
def predict_diabetes(data: DiabetesInput):
    try:
        input_data = {
            'Pregnancies'             : data.Pregnancies,
            'Glucose'                 : data.Glucose,
            'BloodPressure'           : data.BloodPressure,
            'SkinThickness'           : data.SkinThickness,
            'Insulin'                 : data.Insulin,
            'BMI'                     : data.BMI,
            'DiabetesPedigreeFunction': data.DiabetesPedigreeFunction,
            'Age'                     : data.Age,
            'glucose_insulin'         : data.Glucose * data.Insulin,
            'bmi_age'                 : data.BMI * data.Age,
            'glucose_bp_ratio'        : data.Glucose / (data.BloodPressure + 1),
            'skin_bmi'                : data.SkinThickness * data.BMI,
            'anomaly_flag'            : 0
        }
        label, conf = predict('diabetes', input_data)
        status = "normal" if "Not" in label else "alert"
        return PredictionResponse(disease="Diabetes", prediction=label,
                                  confidence=f"{conf}%", status=status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/heart", response_model=PredictionResponse)
def predict_heart(data: HeartInput):
    try:
        input_data = {
            'age'           : data.age,
            'trestbps'      : data.trestbps,
            'chol'          : data.chol,
            'thalach'       : data.thalach,
            'oldpeak'       : data.oldpeak,
            'thalach_age'   : data.thalach * data.age,
            'chol_bp_ratio' : data.chol / (data.trestbps + 1),
            'anomaly_flag'  : 0
        }
        label, conf = predict('heart', input_data)
        status = "normal" if "No" in label else "alert"
        return PredictionResponse(disease="Heart Disease", prediction=label,
                                  confidence=f"{conf}%", status=status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/cancer", response_model=PredictionResponse)
def predict_cancer(data: CancerInput):
    try:
        input_data = {
            'mean radius'           : data.mean_radius,
            'mean texture'          : data.mean_texture,
            'mean perimeter'        : data.mean_perimeter,
            'mean area'             : data.mean_area,
            'mean smoothness'       : data.mean_smoothness,
            'mean compactness'      : data.mean_compactness,
            'mean concavity'        : data.mean_concavity,
            'mean concave points'   : data.mean_concave_points,
            'radius_area'           : data.mean_radius * data.mean_area,
            'compactness_concavity' : data.mean_compactness * data.mean_concavity,
            'worst_radius_area'     : data.worst_radius * data.worst_area,
            'anomaly_flag'          : 0
        }
        label, conf = predict('cancer', input_data)
        status = "normal" if "Benign" in label else "alert"
        return PredictionResponse(disease="Breast Cancer", prediction=label,
                                  confidence=f"{conf}%", status=status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/gene", response_model=PredictionResponse)
def predict_gene(data: GeneInput):
    try:
        input_data = {
            'mean_expression'  : data.mean_expression,
            'std_expression'   : data.std_expression,
            'max_expression'   : data.max_expression,
            'min_expression'   : data.min_expression,
            'expression_range' : data.expression_range,
            'mutation_flag'    : data.mutation_flag,
            'anomaly_flag'     : 0
        }
        label, conf = predict('gene', input_data)
        return PredictionResponse(disease="Gene (ALL/AML)", prediction=label,
                                  confidence=f"{conf}%", status="info")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_full:app", host="127.0.0.1", port=8000, reload=True)