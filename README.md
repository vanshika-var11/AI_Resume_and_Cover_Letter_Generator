
🧠 AI Resume & Cover Letter Generator

Generate beautiful, professional resumes and cover letters in seconds using **LLM (LLaMA3-70B)** — all within a clean, responsive **Streamlit web app**.


🚀 Features

- ✍️ **AI-generated Resume** – Based on your job role, experience, skills, and education.
- 💌 **Cover Letter Generator** – Tailored, enthusiastic cover letters for any company.
- 🎨 **Multiple Templates** – Choose from 3 beautifully formatted resume templates.
- 📄 **Download as PDF** – One-click download for resumes in PDF format.
- 🔗 **LinkedIn Support** – Include LinkedIn profile in the contact section.
- ☁️ **Deployed on Streamlit Cloud** – Ready to access from anywhere.


🖼️ Demo

🔗 Live Demo: http://airesumeandcoverlettergenerator-abarsxq2tvcxbzybafufwa.streamlit.app/



📂 Project Structure


ai\_resume\_generator/
│
├── app.py                 # Streamlit frontend
├── utils.py               # Logic for resume, cover letter, PDF generation
├── requirements.txt       # All required packages
├── .gitignore             # Hides env, cache, and venv from git
└── README.md              # This file ✨


 
⚙️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python + [GROQ LLaMA3 API](https://console.groq.com/)
- **PDF**: fpdf for cross-platform PDF generation
- **Secrets Handling**: Streamlit Cloud Secrets
- **Version Control**: Git & GitHub


🔑 Setup Instructions (Local)

 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai_resume_generator.git
cd ai_resume_generator
````

2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install Requirements

```bash
pip install -r requirements.txt
```

 4. Add your `.env` file

```
GROQ_API_KEY=your_groq_api_key_here
```

5. Run the App

```bash
streamlit run app.py
```



 🌐 Deployment on Streamlit Cloud

1. Push code to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and create a new app from your repo.
3. Set **Secrets** in the **Secrets tab** like this:

```toml
GROQ_API_KEY="your_groq_api_key_here"
```
4. Deploy and Done! 🚀




 🤖 Prompt Templates

Choose from:

* 📋 Structured Pro
* 🎨 Creative Spark
* 🧘 Focused Minimal

All templates follow Markdown formatting and are styled using LLM.



 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.



 📜 License

This project is licensed under the MIT License.



