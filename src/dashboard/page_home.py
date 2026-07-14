import streamlit as st

def show():
    st.markdown("<h1>👋 Welcome to HealthPredict AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px; color:#475569;'>Your personal AI health assistant — simple, fast, and smart.</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
    <div style='background:white; border-radius:24px; padding:32px;
                box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:24px;'>
        <h2 style='margin-top:0;'>🤔 What does this system do?</h2>
        <p style='font-size:17px; color:#475569; line-height:1.8;'>
        This is an <strong>AI doctor assistant</strong>. You enter simple health measurements
        and our smart system tells you whether you might have a health condition.
        Think of it like a <strong>health calculator</strong> — fill in the numbers
        from your medical report and get an instant result!
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🩺 Breast Cancer", "95.61%", "Accuracy")
    with col2: st.metric("❤️ Heart Disease", "78.69%", "Accuracy")
    with col3: st.metric("🩸 Diabetes",      "75.32%", "Accuracy")
    with col4: st.metric("🧬 Gene Test",     "86.67%", "Accuracy")

    st.markdown("---")
    st.markdown("<h2>🔍 What can we check?</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='background:white; border-radius:20px; padding:24px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:16px;
                    border-left:6px solid #ec4899;'>
            <div style='font-size:36px;'>🩺</div>
            <div style='font-size:20px; font-weight:800; color:#1e3a5f; margin:8px 0;'>Breast Cancer</div>
            <div style='font-size:15px; color:#64748b; line-height:1.7;'>
                Checks if a breast tumor is <strong>harmless (benign)</strong> or
                <strong>dangerous (malignant)</strong>.
            </div>
        </div>
        <div style='background:white; border-radius:20px; padding:24px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08);
                    border-left:6px solid #f59e0b;'>
            <div style='font-size:36px;'>🩸</div>
            <div style='font-size:20px; font-weight:800; color:#1e3a5f; margin:8px 0;'>Diabetes</div>
            <div style='font-size:15px; color:#64748b; line-height:1.7;'>
                Checks if a person has <strong>diabetes</strong> using blood sugar,
                BMI and age from a standard blood test.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:white; border-radius:20px; padding:24px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:16px;
                    border-left:6px solid #ef4444;'>
            <div style='font-size:36px;'>❤️</div>
            <div style='font-size:20px; font-weight:800; color:#1e3a5f; margin:8px 0;'>Heart Disease</div>
            <div style='font-size:15px; color:#64748b; line-height:1.7;'>
                Checks if a person has <strong>heart problems</strong> using
                heart rate, blood pressure and cholesterol.
            </div>
        </div>
        <div style='background:white; border-radius:20px; padding:24px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08);
                    border-left:6px solid #8b5cf6;'>
            <div style='font-size:36px;'>🧬</div>
            <div style='font-size:20px; font-weight:800; color:#1e3a5f; margin:8px 0;'>Blood Cancer Gene Test</div>
            <div style='font-size:15px; color:#64748b; line-height:1.7;'>
                Identifies the <strong>type of blood cancer</strong> (ALL or AML)
                from gene activity measurements.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='background:linear-gradient(135deg,#1e3a5f,#0f766e); border-radius:20px;
                padding:28px; text-align:center; color:white;'>
        <div style='font-size:28px; font-weight:800; margin-bottom:16px;'>🚀 How to use</div>
        <div style='display:flex; justify-content:center; gap:40px; flex-wrap:wrap;'>
            <div style='text-align:center;'>
                <div style='font-size:36px;'>1️⃣</div>
                <div style='font-size:15px; margin-top:8px;'>Click<br><strong>Check My Health</strong></div>
            </div>
            <div style='text-align:center;'>
                <div style='font-size:36px;'>2️⃣</div>
                <div style='font-size:15px; margin-top:8px;'>Choose a<br><strong>disease</strong></div>
            </div>
            <div style='text-align:center;'>
                <div style='font-size:36px;'>3️⃣</div>
                <div style='font-size:15px; margin-top:8px;'>Fill in your<br><strong>health numbers</strong></div>
            </div>
            <div style='text-align:center;'>
                <div style='font-size:36px;'>4️⃣</div>
                <div style='font-size:15px; margin-top:8px;'>Click<br><strong>Check Now!</strong></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)