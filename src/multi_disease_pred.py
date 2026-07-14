#Module 8
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from prediction import predict

# ── MULTI DISEASE PREDICTION FUNCTION ─────────────────────────
def predict_all(patient_data):
    """
    Takes one patient's data and runs all 4 disease predictions at once
    """
    print("\n" + "="*45)
    print("     MULTI DISEASE PREDICTION REPORT")
    print("="*45)

    results = {}

    # ── DIABETES ──────────────────────────────────────
    glucose   = patient_data.get('Glucose', 0)
    insulin   = patient_data.get('Insulin', 0)
    bmi       = patient_data.get('BMI', 0)
    age       = patient_data.get('Age', 0)
    bp        = patient_data.get('BloodPressure', 0)
    skin      = patient_data.get('SkinThickness', 0)

    diabetes_input = {
        'Pregnancies'             : patient_data.get('Pregnancies', 0),
        'Glucose'                 : glucose,
        'BloodPressure'           : bp,
        'SkinThickness'           : skin,
        'Insulin'                 : insulin,
        'BMI'                     : bmi,
        'DiabetesPedigreeFunction': patient_data.get('DiabetesPedigreeFunction', 0),
        'Age'                     : age,
        'glucose_insulin'         : glucose * insulin,
        'bmi_age'                 : bmi * age,
        'glucose_bp_ratio'        : glucose / (bp + 1),
        'skin_bmi'                : skin * bmi,
        'anomaly_flag'            : 0
    }
    label, conf = predict('diabetes', diabetes_input)
    results['Diabetes'] = {'prediction': label, 'confidence': conf}

    # ── HEART ─────────────────────────────────────────
    thalach  = patient_data.get('thalach', 0)
    chol     = patient_data.get('chol', 0)
    trestbps = patient_data.get('trestbps', 0)

    heart_input = {
        'age'           : age,
        'trestbps'      : trestbps,
        'chol'          : chol,
        'thalach'       : thalach,
        'oldpeak'       : patient_data.get('oldpeak', 0),
        'thalach_age'   : thalach * age,
        'chol_bp_ratio' : chol / (trestbps + 1),
        'anomaly_flag'  : 0
    }
    label, conf = predict('heart', heart_input)
    results['Heart Disease'] = {'prediction': label, 'confidence': conf}

    # ── CANCER ────────────────────────────────────────
    cancer_input = {
        'mean radius'            : patient_data.get('mean radius', 0),
        'mean texture'           : patient_data.get('mean texture', 0),
        'mean perimeter'         : patient_data.get('mean perimeter', 0),
        'mean area'              : patient_data.get('mean area', 0),
        'mean smoothness'        : patient_data.get('mean smoothness', 0),
        'mean compactness'       : patient_data.get('mean compactness', 0),
        'mean concavity'         : patient_data.get('mean concavity', 0),
        'mean concave points'    : patient_data.get('mean concave points', 0),
        'radius_area'            : patient_data.get('mean radius', 0) * patient_data.get('mean area', 0),
        'compactness_concavity'  : patient_data.get('mean compactness', 0) * patient_data.get('mean concavity', 0),
        'worst_radius_area'      : patient_data.get('worst radius', 0) * patient_data.get('worst area', 0),
        'anomaly_flag'           : 0
    }
    label, conf = predict('cancer', cancer_input)
    results['Breast Cancer'] = {'prediction': label, 'confidence': conf}

    # ── GENE ──────────────────────────────────────────
    gene_input = {
        'mean_expression'  : patient_data.get('mean_expression', 0),
        'std_expression'   : patient_data.get('std_expression', 0),
        'max_expression'   : patient_data.get('max_expression', 0),
        'min_expression'   : patient_data.get('min_expression', 0),
        'expression_range' : patient_data.get('expression_range', 0),
        'mutation_flag'    : patient_data.get('mutation_flag', 0),
        'anomaly_flag'     : 0
    }
    label, conf = predict('gene', gene_input)
    results['Gene (ALL/AML)'] = {'prediction': label, 'confidence': conf}

    # ── PRINT COMBINED REPORT ─────────────────────────
    print("\n" + "="*45)
    print("           COMBINED SUMMARY")
    print("="*45)
    for disease, result in results.items():
        print(f"{disease:<20}: {result['prediction']:<30} ({result['confidence']}% confident)")
    print("="*45)

    return results


# ── TEST WITH SAMPLE PATIENT ───────────────────────────────────
if __name__ == '__main__':
    sample_patient = {
        # Diabetes fields
        'Pregnancies'             : 6,
        'Glucose'                 : 148,
        'BloodPressure'           : 72,
        'SkinThickness'           : 35,
        'Insulin'                 : 0,
        'BMI'                     : 33.6,
        'DiabetesPedigreeFunction': 0.627,
        'Age'                     : 50,

        # Heart fields
        'thalach'                 : 150,
        'chol'                    : 250,
        'trestbps'                : 130,
        'oldpeak'                 : 1.5,

        # Cancer fields
        'mean radius'             : 17.99,
        'mean texture'            : 10.38,
        'mean perimeter'          : 122.8,
        'mean area'               : 1001.0,
        'mean smoothness'         : 0.1184,
        'mean compactness'        : 0.2776,
        'mean concavity'          : 0.3001,
        'mean concave points'     : 0.1471,
        'worst radius'            : 25.38,
        'worst area'              : 2019.0,

        # Gene fields
        'mean_expression'         : 500.0,
        'std_expression'          : 200.0,
        'max_expression'          : 1000.0,
        'min_expression'          : 100.0,
        'expression_range'        : 900.0,
        'mutation_flag'           : 1,
    }

    predict_all(sample_patient)

    print("\n====== Module 8 Complete ======")
    print("Multi disease prediction working for all 4 diseases")
    print("Ready to move to Module 9 — Evaluation Module")