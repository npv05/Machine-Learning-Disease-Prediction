import streamlit as st
from dashboard.api_helper import get_prediction, show_result

def show():
    st.markdown("<h1>🔬 Check My Health</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; color:#475569;'>Choose a health check, fill in your numbers, and get an instant result.</p>", unsafe_allow_html=True)
    st.markdown("---")

    disease = st.selectbox("👇 Which health check do you want to run?", [
        "🩸 Diabetes Check",
        "❤️ Heart Disease Check",
        "🩺 Breast Cancer Check",
        "🧬 Blood Cancer Gene Check"
    ])

    st.markdown("---")

    if "Diabetes" in disease:
        _diabetes()
    elif "Heart" in disease:
        _heart()
    elif "Breast" in disease:
        _cancer()
    elif "Gene" in disease:
        _gene()


def _diabetes():
    st.markdown("<h2>🩸 Diabetes Check</h2>", unsafe_allow_html=True)
    st.info("""
    📋 **Before you start:** Get your latest blood test report.
    Hover over each field's ❓ to understand what to enter.
    If you don't have a value, leave the default number as it is.
    """)

    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input("🤰 Number of Pregnancies", 0, 20, 1,
            help="👶 How many times has the patient been pregnant? Enter 0 if male or never pregnant.")
        glucose = st.number_input("🍬 Blood Sugar Level", 0, 300, 120,
            help="🩸 Found in your blood test report. Normal: 70–99. Pre-diabetic: 100–125. Diabetic: above 126.")
        bp = st.number_input("💉 Blood Pressure (lower number)", 0, 200, 70,
            help="📊 The lower number from your BP reading (e.g. the 80 in 120/80). Normal: 60–80.")
        skin = st.number_input("📏 Skin Fold Thickness (mm)", 0, 100, 20,
            help="🖐️ Measured by pinching the back of the upper arm. If unknown, enter 20. Normal: 10–40.")
    with col2:
        insulin = st.number_input("💊 Insulin Level", 0, 900, 80,
            help="🧪 From a blood test, 2 hours after eating. Enter 0 if not available. Normal: 16–166.")
        bmi = st.number_input("⚖️ Body Weight Score (BMI)", 0.0, 70.0, 25.0,
            help="📐 Weight in kg ÷ (height in metres)². Normal: 18.5–24.9. Overweight: 25–29.9. Obese: 30+.")
        dpf = st.number_input("👨‍👩‍👧 Family Diabetes Score", 0.0, 3.0, 0.5,
            help="👪 Shows how likely diabetes is based on family history. No family history: enter 0.1. Many relatives with diabetes: enter 1.5+.")
        age = st.number_input("🎂 Age (years)", 1, 120, 30,
            help="🗓️ Patient's age in years.")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Check for Diabetes Now!", type="primary"):
        payload = {
            "Pregnancies": pregnancies, "Glucose": glucose,
            "BloodPressure": bp, "SkinThickness": skin,
            "Insulin": insulin, "BMI": bmi,
            "DiabetesPedigreeFunction": dpf, "Age": age
        }
        with st.spinner("🤖 AI is analysing your health data..."):
            label, conf = get_prediction("diabetes", payload)
        if label:
            show_result(label, conf, "Not",
                "Great news! The AI does not detect diabetes. Keep up a healthy lifestyle!",
                "The AI detected signs of possible diabetes. Please visit your doctor soon.",
                "😊", "⚠️")


def _heart():
    st.markdown("<h2>❤️ Heart Disease Check</h2>", unsafe_allow_html=True)
    st.info("""
    📋 **Before you start:** Get your heart checkup or ECG report.
    These numbers come from a routine cardiac checkup.
    """)

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("🎂 Age (years)", 1, 120, 50,
            help="🗓️ Patient's age in years. Heart problems become more common with age.")
        trestbps = st.number_input("💉 Resting Blood Pressure", 0, 250, 120,
            help="📊 Blood pressure when sitting quietly and relaxed. The top number from a BP reading. Normal: below 120. High: above 140.")
        chol = st.number_input("🧈 Cholesterol Level", 0, 600, 200,
            help="🩸 A fatty substance in your blood. Too much is bad for the heart. Normal: below 200. High: above 240.")
    with col2:
        thalach = st.number_input("💓 Highest Heart Rate Recorded", 0, 250, 150,
            help="❤️ The fastest your heart beat during an exercise or stress test. Normal for adults: 100–170 beats per minute.")
        oldpeak = st.number_input("📉 Heart Stress Score (Oldpeak)", 0.0, 10.0, 1.0,
            help="🫀 From an ECG test. Shows how much your heart struggles during exercise. Normal: 0. Concerning: above 2.")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Check for Heart Disease Now!", type="primary"):
        payload = {
            "age": age, "trestbps": trestbps,
            "chol": chol, "thalach": thalach, "oldpeak": oldpeak
        }
        with st.spinner("🤖 AI is analysing your heart data..."):
            label, conf = get_prediction("heart", payload)
        if label:
            show_result(label, conf, "No",
                "Great news! The AI does not detect heart disease. Keep your heart healthy!",
                "The AI detected possible heart disease. Please consult a heart doctor soon.",
                "😊", "⚠️")


def _cancer():
    st.markdown("<h2>🩺 Breast Cancer Check</h2>", unsafe_allow_html=True)
    st.info("""
    📋 **Before you start:** These numbers come from a biopsy report —
    a lab test where a tiny piece of the tumor is examined under a microscope.
    Your doctor or radiologist will give you this report.
    """)

    col1, col2 = st.columns(2)
    with col1:
        radius      = st.number_input("⭕ Tumor Size — Radius (mm)", 0.0, 50.0, 14.0,
            help="📏 How wide the tumor is from center to edge. Smaller is safer. Safe range: 6–15 mm.")
        texture     = st.number_input("🔲 Tumor Surface Roughness", 0.0, 50.0, 19.0,
            help="🔬 How rough the surface of the tumor looks under a microscope. Lower = smoother = safer. Typical: 9–40.")
        perimeter   = st.number_input("📐 Tumor Outline Size (mm)", 0.0, 250.0, 92.0,
            help="📏 Total length around the edge of the tumor. Smaller is safer. Safe range: 40–100 mm.")
        area        = st.number_input("📦 Tumor Total Size (mm²)", 0.0, 2500.0, 654.0,
            help="📐 How much space the tumor takes up. Smaller is safer. Safe range: 100–800 mm².")
        smoothness  = st.number_input("〰️ Tumor Edge Smoothness", 0.0, 1.0, 0.096,
            help="🌊 How smooth the tumor edges are. Closer to 0 = smoother = safer. Typical: 0.05–0.16.")
    with col2:
        compactness = st.number_input("🔵 Tumor Compactness", 0.0, 1.0, 0.104,
            help="🏀 How tightly packed the tumor is. Higher = more irregular shape. Typical: 0.02–0.35.")
        concavity   = st.number_input("🌀 Tumor Dents/Hollows", 0.0, 1.0, 0.088,
            help="🌊 How many dents the tumor has. More dents = more concerning. Typical: 0–0.43.")
        concave_pts = st.number_input("📍 Number of Dent Points", 0.0, 1.0, 0.048,
            help="📌 How many dent points are on the tumor boundary. More = more concerning. Typical: 0–0.20.")
        worst_rad   = st.number_input("⭕ Largest Tumor Radius (mm)", 0.0, 50.0, 16.0,
            help="📏 The biggest size recorded for this tumor. Higher = larger. Typical: 7–36 mm.")
        worst_area  = st.number_input("📦 Largest Tumor Area (mm²)", 0.0, 4000.0, 880.0,
            help="📐 The biggest area recorded. Typical: 185–4254 mm².")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Check Tumor Type Now!", type="primary"):
        payload = {
            "mean_radius": radius, "mean_texture": texture,
            "mean_perimeter": perimeter, "mean_area": area,
            "mean_smoothness": smoothness, "mean_compactness": compactness,
            "mean_concavity": concavity, "mean_concave_points": concave_pts,
            "worst_radius": worst_rad, "worst_area": worst_area
        }
        with st.spinner("🤖 AI is analysing the tumor data..."):
            label, conf = get_prediction("cancer", payload)
        if label:
            show_result(label, conf, "Benign",
                "The tumor appears BENIGN — NOT cancerous. Regular checkups still recommended.",
                "The tumor may be MALIGNANT — possibly cancerous. Please consult a doctor immediately.",
                "😊", "⚠️")


def _gene():
    st.markdown("<h2>🧬 Blood Cancer Gene Check</h2>", unsafe_allow_html=True)
    st.info("""
    📋 **Before you start:** These values come from a gene expression lab test.
    Think of genes like tiny switches in your body — this test checks how many are ON or OFF.
    This helps identify which type of blood cancer a patient has.
    Your doctor or lab will provide these numbers.
    """)

    col1, col2 = st.columns(2)
    with col1:
        mean_exp = st.number_input("📊 Average Gene Activity", 0.0, 5000.0, 500.0,
            help="🔬 The AVERAGE of how active all the body's gene switches are. Higher = more switches ON. Normal: 200–800.")
        std_exp  = st.number_input("📉 Gene Activity Variation", 0.0, 5000.0, 200.0,
            help="📊 How DIFFERENT the gene activities are from each other. High variation can signal disease. Normal: 100–400.")
        max_exp  = st.number_input("📈 Most Active Gene Level", 0.0, 5000.0, 1000.0,
            help="⬆️ The activity level of the most turned-ON gene switch. Typical: 500–3000.")
    with col2:
        min_exp   = st.number_input("📉 Least Active Gene Level", 0.0, 5000.0, 100.0,
            help="⬇️ The activity level of the most turned-OFF gene switch. Typical: 0–300.")
        exp_range = st.number_input("↔️ Gene Activity Range", 0.0, 5000.0, 900.0,
            help="📏 Most Active Gene Level MINUS Least Active Gene Level. Example: 1000 - 100 = 900.")
        mut_flag  = st.selectbox("🧬 Is Gene Activity Unusual?",
            options=[0, 1],
            format_func=lambda x: "0 — No, gene activity looks normal" if x == 0
                                  else "1 — Yes, gene activity looks unusual",
            help="🚨 If the Gene Activity Variation above is much higher than 400, select YES (1). Otherwise select NO (0).")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Check Blood Cancer Type Now!", type="primary"):
        payload = {
            "mean_expression": mean_exp, "std_expression": std_exp,
            "max_expression": max_exp, "min_expression": min_exp,
            "expression_range": exp_range, "mutation_flag": mut_flag
        }
        with st.spinner("🤖 AI is analysing the gene data..."):
            label, conf = get_prediction("gene", payload)
        if label:
            if label == "ALL":
                st.markdown(f"""
                <div style='background:linear-gradient(135deg,#eff6ff,#dbeafe);
                            border-radius:20px; padding:28px; text-align:center;
                            border:2px solid #93c5fd; margin-top:16px;'>
                    <div style='font-size:56px;'>🔵</div>
                    <div style='font-size:28px; font-weight:900; color:#1e3a5f; margin:10px 0;'>ALL Detected</div>
                    <div style='font-size:16px; color:#1d4ed8; margin-bottom:16px;'>
                        Acute Lymphoblastic Leukemia — Most common in children. Highly treatable.
                        Please consult your doctor for treatment planning.
                    </div>
                    <div style='background:white; border-radius:12px; padding:12px; display:inline-block;'>
                        <div style='font-size:13px; color:#64748b; font-weight:700;'>CONFIDENCE</div>
                        <div style='font-size:32px; font-weight:900; color:#1d4ed8;'>{conf}%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='background:linear-gradient(135deg,#fff7ed,#fed7aa);
                            border-radius:20px; padding:28px; text-align:center;
                            border:2px solid #fb923c; margin-top:16px;'>
                    <div style='font-size:56px;'>🟠</div>
                    <div style='font-size:28px; font-weight:900; color:#7c2d12; margin:10px 0;'>AML Detected</div>
                    <div style='font-size:16px; color:#c2410c; margin-bottom:16px;'>
                        Acute Myeloid Leukemia — More common in adults.
                        Please consult your doctor immediately for urgent treatment.
                    </div>
                    <div style='background:white; border-radius:12px; padding:12px; display:inline-block;'>
                        <div style='font-size:13px; color:#64748b; font-weight:700;'>CONFIDENCE</div>
                        <div style='font-size:32px; font-weight:900; color:#ea580c;'>{conf}%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)