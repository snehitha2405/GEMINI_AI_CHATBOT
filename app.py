import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

/* ==========================================
   MAIN BACKGROUND
========================================== */

.stApp {
    background: linear-gradient(
        135deg,
        #667eea,
        #764ba2
    );
}


/* ==========================================
   MAIN CONTENT
========================================== */

.main {
    padding: 2rem;
}


/* ==========================================
   TITLE
========================================== */

h1 {
    text-align: center;

    color: white !important;

    font-size: 42px;

    font-weight: 700;

    margin-bottom: 10px;
}


/* ==========================================
   NORMAL TEXT
========================================== */

p {
    color: white;
}


/* ==========================================
   TEXT AREA LABEL
========================================== */

.stTextArea label {
    color: white !important;

    font-weight: 600;

    font-size: 18px;
}


/* ==========================================
   TEXT AREA
========================================== */

.stTextArea textarea {

    background-color: #ffffff !important;

    color: #222222 !important;

    border-radius: 15px !important;

    border: 2px solid #667eea !important;

    padding: 15px !important;

    font-size: 16px !important;

    min-height: 140px;
}


/* ==========================================
   TEXT AREA PLACEHOLDER
========================================== */

.stTextArea textarea::placeholder {

    color: #777777 !important;

    opacity: 1 !important;
}


/* ==========================================
   TEXT AREA FOCUS
========================================== */

.stTextArea textarea:focus {

    border: 2px solid #00d4ff !important;

    box-shadow:
        0 0 10px rgba(0, 212, 255, 0.35) !important;
}


/* ==========================================
   BUTTON
========================================== */

.stButton button {

    width: 100%;

    border-radius: 15px;

    padding: 12px;

    font-size: 18px;

    font-weight: bold;

    background: linear-gradient(
        90deg,
        #00d4ff,
        #00b4d8
    ) !important;

    color: #2d1457 !important;

    border: none !important;

    transition: 0.3s;
}


/* ==========================================
   BUTTON HOVER
========================================== */

.stButton button:hover {

    background: linear-gradient(
        90deg,
        #ff4b8b,
        #ff6b9d
    ) !important;

    color: white !important;

    transform: translateY(-2px);

    box-shadow:
        0 5px 15px rgba(0, 0, 0, 0.25);
}


/* ==========================================
   SUCCESS MESSAGE
========================================== */

.stAlert {

    border-radius: 15px !important;
}


/* ==========================================
   SPINNER TEXT
========================================== */

.stSpinner > div {

    color: white !important;
}


/* ==========================================
   DARK MODE SUPPORT
========================================== */

@media (prefers-color-scheme: dark) {

    .stTextArea label {
        color: white !important;
    }

    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #222222 !important;
    }

    .stTextArea textarea::placeholder {
        color: #777777 !important;
    }

    p {
        color: white !important;
    }

}

</style>
""", unsafe_allow_html=True)

# ==========================================
# TITLE
# ==========================================

st.title("🤖 Gemini AI Chatbot")

st.write("✨ Ask Gemini anything!")

# ==========================================
# INPUT
# ==========================================

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words"
)

# ==========================================
# BUTTON
# ==========================================

if st.button("🚀 Generate Response"):

    if prompt:

        with st.spinner("🤖 Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("✅ Response generated!")

        st.write(response.text)

    else:

        st.warning("⚠️ Please enter a prompt.")
