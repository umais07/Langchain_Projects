# 📄 Resume Tracking System

An AI-powered resume analyzer built with **Streamlit** and **Google Gemini**. Upload a resume (PDF) and a job description to get instant feedback on skill gaps, missing keywords, and an overall match score — like an ATS (Applicant Tracking System) reviewer in your browser.

## ✨ Features

- **Tell me about the Resume** – Get a quick summary and evaluation of the uploaded resume.
- **How can I improve these skills?** – Personalized suggestions to strengthen the resume against the job description.
- **What keywords are missing?** – Identify keywords from the job description not present in the resume.
- **Percentage Match** – A scored breakdown (technical skills, experience, keywords, education, soft skills) showing how well the resume fits the role.

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web interface
- [PyPDF2](https://pypi.org/project/PyPDF2/) – PDF text extraction
- [LangChain](https://www.langchain.com/) + [Google Gemini](https://ai.google.dev/) – LLM-powered analysis
- Python `dotenv` – Environment variable management

## 🚀 Getting Started


### Installation

### Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### Run the App

```bash
streamlit run app.py
```

## 📖 Usage

1. Paste the target **job description** into the text box.
2. Upload your **resume as a PDF**.
3. Click one of the four analysis buttons to get tailored feedback.

## 🖼️ Screenshots

### Main Interface
<img width="857" height="621" alt="Main interface" src="https://github.com/user-attachments/assets/403c83be-81f7-46c1-8e96-c56593d8bcc1" />

### PDF Upload Check
<img width="910" height="688" alt="PDF upload file check" src="https://github.com/user-attachments/assets/5df6d29c-6651-40fa-a2f7-df26c3f59cba" />

### Analyzing
<img width="868" height="623" alt="Analyzing" src="https://github.com/user-attachments/assets/9231ca46-fac0-42de-b2c0-040be9084347" />

### "Tell me about the Resume"
<img width="895" height="795" alt="Tell me about the resume response 1" src="https://github.com/user-attachments/assets/d42542b8-6e22-4510-8522-43e39a1a7794" />
<img width="874" height="737" alt="Tell me about the resume response 2" src="https://github.com/user-attachments/assets/ad08037d-7500-4152-9b49-d73c5298ede6" />

### "How can I improve these skills?"
<img width="881" height="789" alt="Skill improvement response 1" src="https://github.com/user-attachments/assets/f4782030-1c36-4856-84e6-7696af4d70e7" />
<img width="793" height="638" alt="Skill improvement response 2" src="https://github.com/user-attachments/assets/bece5453-5fb9-4c50-a596-5433d07ffd42" />

### "What keywords are missing?"
<img width="815" height="628" alt="Missing keywords response 1" src="https://github.com/user-attachments/assets/834e7143-87f5-479c-ad1c-7fc2de3a5965" />
<img width="884" height="814" alt="Missing keywords response 2" src="https://github.com/user-attachments/assets/142f8273-ea11-48d8-859f-300b3e57b931" />

### "Percentage Match"
<img width="900" height="312" alt="Percentage match response" src="https://github.com/user-attachments/assets/46724fe0-529e-48ce-9164-acbc1524c4d7" />

