import streamlit as st
import pandas as pd
import os

def show():
    st.markdown("<h1>📋 AI Accuracy Summary</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; color:#475569;'>A summary of how well our AI performs for each disease.</p>", unsafe_allow_html=True)
    st.markdown("---")

    path = "outputs/evaluation_summary.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)

        st.markdown("""
        <div style='background:white; border-radius:20px; padding:24px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:24px;'>
            <h3 style='margin-top:0;'>📊 Performance Table</h3>
        """, unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("<h3>📈 Accuracy Chart</h3>", unsafe_allow_html=True)
        df['Accuracy_num'] = df['Accuracy'].str.replace('%','').astype(float)
        st.bar_chart(df.set_index('Disease')['Accuracy_num'])

        st.markdown("---")
        st.markdown("""
        <div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7); border-radius:16px;
                    padding:20px; border-left:5px solid #0f766e;'>
            <strong style='font-size:16px;'>📖 What do these numbers mean?</strong>
            <ul style='font-size:15px; color:#475569; margin-top:10px; line-height:2;'>
                <li><strong>Accuracy</strong> — Out of every 100 patients, how many did the AI get right</li>
                <li><strong>AUC</strong> — Score from 0 to 1. Closer to 1 = smarter AI. Above 0.8 is very good</li>
                <li>Our breast cancer AI got <strong>95.61%</strong> — correctly identified 95 out of every 100 patients!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Run evaluation.py first to generate the summary.")