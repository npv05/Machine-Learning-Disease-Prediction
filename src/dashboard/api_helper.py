import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def check_api():
    try:
        r = requests.get(f"{API_URL}/health", timeout=3)
        return r.status_code == 200
    except:
        return False

def get_prediction(endpoint, payload):
    try:
        response = requests.post(
            f"{API_URL}/predict/{endpoint}",
            json=payload, timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            return data['prediction'], float(data['confidence'].replace('%',''))
        else:
            st.error(f"API Error: {response.status_code}")
            return None, None
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to API. Make sure FastAPI is running.")
        return None, None
    except Exception as e:
        st.error(f"Something went wrong: {e}")
        return None, None

def show_result(label, conf, positive_keyword, positive_msg, negative_msg, emoji_good, emoji_bad):
    if positive_keyword in label:
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,#dcfce7,#bbf7d0);
                    border-radius:20px; padding:28px; text-align:center;
                    border:2px solid #86efac; margin-top:16px;'>
            <div style='font-size:56px;'>{emoji_good}</div>
            <div style='font-size:24px; font-weight:900; color:#166534; margin:10px 0;'>{label}</div>
            <div style='font-size:16px; color:#15803d;'>{positive_msg}</div>
            <div style='margin-top:16px; background:white; border-radius:12px;
                        padding:12px; display:inline-block; min-width:160px;'>
                <div style='font-size:13px; color:#64748b; font-weight:700;'>CONFIDENCE</div>
                <div style='font-size:32px; font-weight:900; color:#0f766e;'>{conf}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,#fef2f2,#fecaca);
                    border-radius:20px; padding:28px; text-align:center;
                    border:2px solid #fca5a5; margin-top:16px;'>
            <div style='font-size:56px;'>{emoji_bad}</div>
            <div style='font-size:24px; font-weight:900; color:#991b1b; margin:10px 0;'>{label}</div>
            <div style='font-size:16px; color:#b91c1c;'>{negative_msg}</div>
            <div style='margin-top:16px; background:white; border-radius:12px;
                        padding:12px; display:inline-block; min-width:160px;'>
                <div style='font-size:13px; color:#64748b; font-weight:700;'>CONFIDENCE</div>
                <div style='font-size:32px; font-weight:900; color:#dc2626;'>{conf}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)