import streamlit as st
import requests  # Backend API se baat karne ke liye
import pandas as pd
from streamlit_mic_recorder import mic_recorder

# --- 1. UI CONFIGURATION ---
st.set_page_config(page_title="Data Vishleshan Studio", layout="wide")

# Custom CSS for Modern Look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { border-radius: 10px; height: 3em; background-color: #007BFF; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (User Profile & Language) ---
with st.sidebar:
    st.title("🔐 Data Studio")
    user_lang = st.selectbox("Apni Bhasha Chunein", ["Hindi", "English", "Urdu"])
    st.markdown("---")
    st.subheader("📁 Cloud Storage")
    uploaded_file = st.file_uploader("File select karein", type=['xlsx', 'pdf', 'docx', 'pptx', 'mp4'])

# --- 3. MAIN DASHBOARD ---
st.title("📊 Universal Data Vishleshan AI")

col_editor, col_ai = st.columns([2, 1])

with col_editor:
    st.subheader("📝 Universal Editor (Read/Write/Modify)")
    if uploaded_file:
        file_ext = uploaded_file.name.split('.')[-1]
        st.success(f"File '{uploaded_file.name}' successfully upload ho gayi hai.")
        
        # Agar Excel hai toh Editor dikhao
        if file_ext in ['xlsx', 'csv']:
            df = pd.read_excel(uploaded_file) if file_ext == 'xlsx' else pd.read_csv(uploaded_file)
            edited_df = st.data_editor(df, num_rows="dynamic") # Yahan modify kar sakte hain
            
            if st.button("📥 Modified File Download Karein"):
                # Backend ko request jayegi download ke liye
                st.write("Processing download...")
        
        # Animation Selection Tray
        st.markdown("---")
        st.subheader("🎭 Animation Studio")
        anim_style = st.selectbox("Animation Style Select Karein", ["None", "Fade", "Fly-In", "Zoom", "Bounce"])
        if st.button("✨ Apply Animation"):
            st.info(f"{anim_style} animation apply ho raha hai... Same format mein download taiyar hai.")

    else:
        st.info("Kripya sidebar se koi file upload karein taaki hum kaam shuru kar sakein.")

with col_ai:
    st.subheader("🎙️ Voice Assistant (Aam Bhasha)")
    st.write("Boliye: 'Iska graph dikhao' ya 'Summary Urdu mein do'")
    
    # Mic integration
    audio_data = mic_recorder(start_prompt="⏺️ Command Bolein", stop_prompt="⏹️ Stop", key='mic')
    
    user_text = st.text_input("Ya yahan type karein:")
    
    if st.button("Run AI Action") or audio_data:
        with st.spinner("AI vishleshan kar raha hai..."):
            # Yahan hum Backend (main.py) ko request bhejenge
            # response = requests.post("http://localhost:8000/process", data=...)
            st.markdown("#### 💡 AI Response:")
            st.write("Bhai, aapka data analyze ho gaya hai. Analysis ke mutabiq sales 20% badhi hai.")