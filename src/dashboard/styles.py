import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Quicksand:wght@500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif !important;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 40%, #f0fdf4 100%);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a5f 0%, #0f766e 100%) !important;
        border-right: none !important;
    }
    [data-testid="stSidebar"] * { color: white !important; }
    [data-testid="stSidebar"] .stRadio label {
        background: rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 10px 16px;
        margin: 4px 0;
        display: block;
        transition: all 0.2s;
        cursor: pointer;
        font-size: 16px !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,0.25);
        transform: translateX(4px);
    }
    h1 {
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 700 !important;
        font-size: 2.8rem !important;
        background: linear-gradient(135deg, #1e3a5f, #0f766e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0 !important;
    }
    h2, h3 {
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 700 !important;
        color: #1e3a5f !important;
    }
    [data-testid="stMetric"] {
        background: white;
        border-radius: 20px;
        padding: 20px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: transform 0.2s;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    [data-testid="stMetricLabel"] {
        font-size: 14px !important;
        font-weight: 700 !important;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 900 !important;
        color: #0f766e !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #1e3a5f, #0f766e) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 14px 40px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        font-family: 'Nunito', sans-serif !important;
        width: 100% !important;
        transition: all 0.3s !important;
        box-shadow: 0 4px 15px rgba(15,118,110,0.3) !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(15,118,110,0.4) !important;
    }
    .stNumberInput > div > div > input {
        border-radius: 12px !important;
        border: 2px solid #e2e8f0 !important;
        font-size: 16px !important;
        font-family: 'Nunito', sans-serif !important;
    }
    .stNumberInput label, .stSelectbox label {
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #1e3a5f !important;
    }
    hr {
        border: none !important;
        height: 3px !important;
        background: linear-gradient(90deg, #1e3a5f, #0f766e, transparent) !important;
        border-radius: 2px !important;
        margin: 24px 0 !important;
    }
    /* ── TOOLTIP ICON FIX — visible in both light and dark themes ── */
    button[data-testid="stTooltipHoverTarget"] {
        color: #0f766e !important;
        background: #e0f2fe !important;
        border-radius: 50% !important;
        width: 22px !important;
        height: 22px !important;
        font-size: 13px !important;
        font-weight: 900 !important;
        border: 2px solid #0f766e !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin-left: 6px !important;
        transition: all 0.2s !important;
    }
    button[data-testid="stTooltipHoverTarget"]:hover {
        background: #0f766e !important;
        color: white !important;
        transform: scale(1.1) !important;
    }
    button[data-testid="stTooltipHoverTarget"] svg {
        fill: #0f766e !important;
    }
    button[data-testid="stTooltipHoverTarget"]:hover svg {
        fill: white !important;
    }
    </style>
    """, unsafe_allow_html=True)