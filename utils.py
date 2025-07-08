import os
import requests
import streamlit as st
from xhtml2pdf import pisa
from io import BytesIO
import qrcode

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# GROQ API details
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-70b-8192"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}


def build_prompt(template, name, email, phone, job_title, company, experience, skills, education, linkedin_url):
    contact_info = f"Email: {email}\nPhone: {phone}"
    if linkedin_url:
        contact_info += f"\nLinkedIn: {linkedin_url}"

    skills_list_bullet = '\n- '.join(skill.strip() for skill in skills.split(','))
    skills_inline = ', '.join(skill.strip() for skill in skills.split(','))

    if template == "📋 Structured Pro":
        return f"""
# {name}

**Contact Info**  
{contact_info}

---

## 🎯 Objective  
Aspiring {job_title} role at **{company}**.

---

## 🛠️ Skills  
- {skills_list_bullet}

---

## 🎓 Education  
{education}

---

## 💼 Projects / Work Experience  
{experience}
"""

    elif template == "🎨 Creative Spark":
        return f"""
# 👩‍💼 {name}

📧 {email} | 📞 {phone} {'| 🔗 ' + linkedin_url if linkedin_url else ''}

---

## 🎯 Objective  
Excited to apply as a **{job_title}** at **{company}**, where I can bring my unique skills and creativity.

---

## 🌟 Skills  
- {skills_list_bullet}

---

## 🎓 Education  
{education}

---

## 🧪 Experience / Projects  
{experience}
"""

    elif template == "🧘 Focused Minimal":
        return f"""
# {name}

**Contact:**  
{contact_info}

---

## Objective  
Seeking the position of {job_title} at {company}.

---

## Skills  
{skills_inline}

---

## Education  
{education}

---

## Experience / Projects  
{experience}
"""
    else:
        return "Invalid template selected."


def generate_resume(name, email, phone, job_title, company, experience, skills, education, linkedin_url, template):
    prompt = build_prompt(template, name, email, phone, job_title, company, experience, skills, education, linkedin_url)

    response = requests.post(GROQ_URL, headers=headers, json={
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    })

    return response.json()["choices"][0]["message"]["content"].strip()


def generate_cover_letter(name, email, phone, job_title, company, experience, skills, education):
    prompt = f"""
Write a formal and enthusiastic cover letter in Markdown format using these details:

Full Name: {name}  
Email: {email}  
Phone: {phone}  
Job Title: {job_title}  
Company: {company}  
Experience: {experience}  
Skills: {skills}  
Education: {education}

It should include a greeting, role interest, highlighted skills, and a positive closing.
"""

    response = requests.post(GROQ_URL, headers=headers, json={
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    })

    return response.json()["choices"][0]["message"]["content"].strip()


def convert_to_pdf(content_md, output_file="output.pdf"):
    html_content = f"<html><body><pre>{content_md}</pre></body></html>"
    result = BytesIO()
    pisa_status = pisa.CreatePDF(html_content, dest=result)
    if pisa_status.err:
        return None
    return result.getvalue()


def generate_qr_code(linkedin_url):
    qr = qrcode.make(linkedin_url)
    return qr
