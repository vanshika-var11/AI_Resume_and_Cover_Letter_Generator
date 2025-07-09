import streamlit as st  
import traceback
from dotenv import load_dotenv
import os
import re
from utils import generate_resume, generate_cover_letter, convert_to_pdf, convert_to_docx

# ---------- Validation Functions ----------
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return re.fullmatch(r"[6-9]\d{9}", phone)

def is_valid_linkedin(link):
    return link.startswith("https://www.linkedin.com/in/")

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

    # Template Selector
    template = st.radio("Choose Resume Template", ["📋 Structured Pro", "🧘 Focused Minimal"], horizontal=True)

    # 👁️ Preview option placed just after template selection
    preview = st.checkbox("👁️ Preview Selected Resume Template")

    bg_color = "#1e1e1e" if theme == "🌙 Dark" else "#f9f9f9"
    text_color = "#ffffff" if theme == "🌙 Dark" else "#000000"

    # Main Title
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

    # 📘 PREVIEW RESUME BEFORE INPUT
    if preview:
        st.markdown("### 🔍 Resume Template Preview")
        sample_resume = generate_resume(
            name="John Doe",
            email="john@example.com",
            phone="9876543210",
            job_title="Data Analyst",
            company="TechCorp",
            experience="• Analyzed data using Python\n• Created Power BI dashboards",
            skills="Python, SQL, Excel, Power BI",
            education="B.Tech in Computer Science from XYZ University",
            linkedin_url="https://www.linkedin.com/in/johndoe",
            template=template
        )
        st.markdown(f"""
            <div style='background-color:{bg_color};padding:15px;border-radius:8px;color:{text_color};border:2px dashed #2196F3;'>
            <pre style='white-space: pre-wrap; color:{text_color};'>{sample_resume}</pre>
            </div>
        """, unsafe_allow_html=True)

    # 🔽 Form Input
    st.markdown("Fill in your details below:")
    with st.form("resume_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name *", placeholder="e.g., Vanshika Varshney")
            email = st.text_input("Email *", placeholder="e.g., yourname@example.com")
            phone = st.text_input("Phone Number *", placeholder="e.g., 9876543210")
        with col2:
            job_title = st.text_input("Job Title You're Applying For *", placeholder="e.g., Data Analyst")
            company = st.text_input("Company Name *", placeholder="e.g., Accenture")

        experience = st.text_area("Work Experience / Projects *", placeholder="e.g., Analyzed sales data using Python & Power BI...")
        skills = st.text_area("Skills (comma-separated) *", placeholder="e.g., Python, SQL, Excel, Power BI")
        education = st.text_area("Education Background *", placeholder="e.g., B.Tech in Computer Science from XYZ University")
        linkedin_url = st.text_input("LinkedIn Profile (Optional)", placeholder="e.g., https://www.linkedin.com/in/yourname")

        submit = st.form_submit_button("🚀 Generate Resume & Cover Letter")

    # 🎯 Form Submission
    if submit:
        required_fields = [full_name, email, phone, job_title, company, experience, skills, education]
        field_labels = ["Full Name", "Email", "Phone Number", "Job Title", "Company Name", "Work Experience", "Skills", "Education"]
        missing = [label for value, label in zip(required_fields, field_labels) if not value]

        if missing:
            st.error(f"⚠️ Please fill in all the required fields: {', '.join(missing)}")
        elif not is_valid_email(email):
            st.error("📧 Please enter a valid email address.")
        elif not is_valid_phone(phone):
            st.error("📞 Please enter a valid 10-digit Indian phone number (without +91).")
        elif linkedin_url and not is_valid_linkedin(linkedin_url):
            st.error("🔗 LinkedIn URL must start with https://www.linkedin.com/in/")
        else:
            with st.spinner("Generating documents..."):
                resume = generate_resume(full_name, email, phone, job_title, company, experience, skills, education, linkedin_url, template)
                cover_letter = generate_cover_letter(full_name, email, phone, job_title, company, experience, skills, education)

            # 🧾 Resume
            st.markdown("### ✅ Your Resume")
            with st.expander("📘 View Resume"):
                st.markdown(f"""
                    <div style='background-color:{bg_color};padding:15px;border-radius:8px;color:{text_color};border:1px dashed #4CAF50;'>
                    <pre style='white-space: pre-wrap; color:{text_color};'>{resume}</pre>
                    </div>
                """, unsafe_allow_html=True)

            # 📨 Cover Letter
            st.markdown("### ✅ Your Cover Letter")
            with st.expander("📘 View Cover Letter"):
                st.markdown(f"""
                    <div style='background-color:{bg_color};padding:15px;border-radius:8px;color:{text_color};border:1px dashed #4CAF50;'>
                    <pre style='white-space: pre-wrap; color:{text_color};'>{cover_letter}</pre>
                    </div>
                """, unsafe_allow_html=True)

            # 📥 Download Buttons
            col1, col2 = st.columns(2)
            with col1:
                st.download_button("📥 Download Resume PDF", data=convert_to_pdf(resume), file_name="resume.pdf", mime="application/pdf")
                st.download_button("📄 Download Resume DOCX", data=convert_to_docx(resume), file_name="resume.docx")
            with col2:
                st.download_button("📥 Download Cover Letter PDF", data=convert_to_pdf(cover_letter), file_name="cover_letter.pdf", mime="application/pdf")
                st.download_button("📄 Download Cover Letter DOCX", data=convert_to_docx(cover_letter), file_name="cover_letter.docx")

    # 🖌️ Custom Styling
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
    st.error("❌ Error in app startup or form rendering:")
    st.code(traceback.format_exc())
