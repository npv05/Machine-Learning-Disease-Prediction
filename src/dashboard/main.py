import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dashboard.styles      import load_styles
from dashboard.api_helper  import check_api
from dashboard             import page_home, page_predict, page_evaluation, page_summary

st.set_page_config(
    page_title="HealthPredict AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_styles()

# ── SIDEBAR ────────────────────────────────────────────────────
st.sidebar.markdown("""
<div style='text-align:center; padding:20px 0 10px 0;'>
    <div style='font-size:60px;'>🏥</div>
    <div style='font-family:Quicksand,sans-serif; font-size:22px;
                font-weight:800; color:white; margin-top:8px;'>HealthPredict AI</div>
    <div style='font-size:13px; color:rgba(255,255,255,0.7); margin-top:4px;'>Smart Disease Detection</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate", [
    "🏠  Home",
    "🔬  Check My Health",
    "📊  Model Performance",
    "📋  Accuracy Summary"
])

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='font-size:13px;font-weight:700;color:rgba(255,255,255,0.8);margin-bottom:8px;'>⚙️ System Status</div>", unsafe_allow_html=True)
if check_api():
    st.sidebar.success("✅ System is Ready!")
else:
    st.sidebar.error("❌ System Offline")
    st.sidebar.caption("Start FastAPI:\npython src/api_full.py")

# ── ROUTING ────────────────────────────────────────────────────
if   "Home"        in page: page_home.show()
elif "Health"      in page: page_predict.show()
elif "Performance" in page: page_evaluation.show()
elif "Accuracy"    in page: page_summary.show()