import streamlit as st 
import traceback
from dotenv import load_dotenv
import os
from markdown2 import markdown
import base64
from utils import generate_resume, generate_cover_letter, convert_to_pdf, generate_qr_code

try:
    load_dotenv()

    st.set_page_config(page_title="AI Resume & Cover Letter Generator", layout="centered")

    # Theme Toggle
    theme = st.radio("Choose Theme", ["🌞 Light", "🌙 Dark"], horizontal=True)
    if theme == "🌙 Dark":
        st.markdown("""
            <style>
            body, .stApp {
                background-color: #1e1e1e;
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)

    # Template Switcher
    template = st.radio("Choose Resume Template", ["📋 Structured Pro", "🎨 Creative Spark", "🧘 Focused Minimal"], horizontal=True)

    # Dynamic style variables
    bg_color = "#1e1e1e" if theme == "🌙 Dark" else "#f9f9f9"
    text_color = "#ffffff" if theme == "🌙 Dark" else "#000000"

    # Stylish Title
    st.markdown(f"""
        <style>
        .main-title {{
            text-align: center;
            font-size: 40px;
            color: #4CAF50;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        </style>
        <div class="main-title"> AI Resume & Cover Letter Generator</div>
    """, unsafe_allow_html=True)

    st.markdown("Fill in your details below:")

    with st.form("resume_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
        with col2:
            job_title = st.text_input("Job Title You're Applying For")
            company = st.text_input("Company Name")

        experience = st.text_area("Work Experience / Projects")
        skills = st.text_area("Skills (comma-separated)")
        education = st.text_area("Education Background")
        linkedin_url = st.text_input("LinkedIn Profile (Optional for QR Code)")

        preview = st.checkbox("👁️ Preview Resume Format")
        submit = st.form_submit_button(" Generate Documents")

    if submit:
        with st.spinner("Generating documents..."):
            resume = generate_resume(full_name, email, phone, job_title, company, experience, skills, education, linkedin_url, template)
            cover_letter = generate_cover_letter(full_name, email, phone, job_title, company, experience, skills, education)

        st.markdown(" Generated Resume")
        with st.expander("📘 View Resume"):
            st.markdown(f"""
                <div style='background-color:{bg_color};padding:15px;border-radius:8px;color:{text_color};border:1px dashed #4CAF50;'>
                <pre style='white-space: pre-wrap; color:{text_color};'>{resume}</pre>
                </div>
            """, unsafe_allow_html=True)

        st.markdown(" Generated Cover Letter")
        with st.expander("📘 View Cover Letter"):
            st.markdown(f"""
                <div style='background-color:{bg_color};padding:15px;border-radius:8px;color:{text_color};border:1px dashed #4CAF50;'>
                <pre style='white-space: pre-wrap; color:{text_color};'>{cover_letter}</pre>
                </div>
            """, unsafe_allow_html=True)

        # PDF Export Buttons
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("📥 Download Resume PDF", data=convert_to_pdf(resume), file_name="resume.pdf", mime="application/pdf")
        with col2:
            st.download_button("📥 Download Cover Letter PDF", data=convert_to_pdf(cover_letter), file_name="cover_letter.pdf", mime="application/pdf")

       

        if preview:
            st.markdown(f"""Selected Template Style: `{template}`""")
            if template == "📋 Structured Pro":
                st.info("You selected the **Structured Pro** layout – formal, professional, and clearly sectioned.")
            elif template == "🎨 Creative Spark":
                st.success("You selected the **Creative Spark** layout – modern, visually engaging, and expressive.")
            elif template == "🧘 Focused Minimal":
                st.warning("You selected the **Focused Minimal** layout – clean, lightweight, and distraction-free.")

    # Optional global style
    st.markdown("""
        <style>
        textarea, input {
            border: 1px solid #ccc !important;
            border-radius: 5px !important;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    

except Exception as e:
    st.error("Error in app startup or form rendering:")
    st.code(traceback.format_exc())
