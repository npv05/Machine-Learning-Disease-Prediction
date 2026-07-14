import streamlit as st
import os

def show():
    st.markdown("<h1>📊 How Well Does Our AI Perform?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; color:#475569;'>These charts show how accurately our AI predicts each disease.</p>", unsafe_allow_html=True)
    st.markdown("---")

    disease_map = {
        "🩺 Breast Cancer" : "breast_cancer",
        "❤️ Heart Disease" : "heart_disease",
        "🩸 Diabetes"      : "diabetes",
        "🧬 Gene (ALL/AML)": "gene_all_aml"
    }

    selected = st.selectbox("Select a disease to see its performance charts:", list(disease_map.keys()))
    key = disease_map[selected]
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style='background:white; border-radius:16px; padding:16px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08); text-align:center; margin-bottom:8px;'>
            <div style='font-size:20px; font-weight:800; color:#1e3a5f;'>🎯 Confusion Matrix</div>
            <div style='font-size:13px; color:#64748b; margin-top:4px;'>
                Shows how many predictions were correct vs wrong
            </div>
        </div>
        """, unsafe_allow_html=True)
        path = f"outputs/confusion_{key}.png"
        if os.path.exists(path):
            st.image(path, use_column_width=True)
        else:
            st.warning("Run evaluation.py first")

    with col2:
        st.markdown("""
        <div style='background:white; border-radius:16px; padding:16px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08); text-align:center; margin-bottom:8px;'>
            <div style='font-size:20px; font-weight:800; color:#1e3a5f;'>📈 ROC Curve</div>
            <div style='font-size:13px; color:#64748b; margin-top:4px;'>
                Higher curve = smarter AI. AUC closer to 1.0 = perfect
            </div>
        </div>
        """, unsafe_allow_html=True)
        path = f"outputs/roc_{key}.png"
        if os.path.exists(path):
            st.image(path, use_column_width=True)
        else:
            st.warning("Run evaluation.py first")

    with col3:
        st.markdown("""
        <div style='background:white; border-radius:16px; padding:16px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08); text-align:center; margin-bottom:8px;'>
            <div style='font-size:20px; font-weight:800; color:#1e3a5f;'>🔍 What Matters Most</div>
            <div style='font-size:13px; color:#64748b; margin-top:4px;'>
                Which health measurements the AI relies on most
            </div>
        </div>
        """, unsafe_allow_html=True)
        path = f"outputs/feature_importance_{key}.png"
        if os.path.exists(path):
            st.image(path, use_column_width=True)
        else:
            st.warning("Run evaluation.py first")