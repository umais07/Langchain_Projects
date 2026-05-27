# 🌟 Celebrity Insights with LangChain & Groq

An AI-powered app that takes a **celebrity name** as input and returns:
- 📖 A brief overview of who they are
- 🎂 Their date of birth
- 🌍 Major global events that occurred around the time of their birth

Built with **LangChain**, **Groq (LLaMA 4)**, and **Streamlit**.

---

## 🖥️ Demo

![App Screenshot](https://github.com/user-attachments/assets/6d5fc941-bbac-425f-86da-cab287a6f966)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/umais07/Langchain_Projects.git
cd Langchain_Projects
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
groq_key=your_groq_api_key_here
```

> Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Run the app

```bash
streamlit run main.py
```

---

## ⚙️ How It Works

The app uses a **3-step LangChain pipeline**:

```
User Input (Celebrity Name)
        ↓
  Step 1 — General Info       → Who is this person?
        ↓
  Step 2 — Date of Birth      → When were they born?
        ↓
  Step 3 — Global Events      → What happened around that time?
        ↓
    Streamlit UI Output
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [LangChain](https://langchain.com) | LLM chaining & prompt templates |
| [Groq](https://groq.com) | Fast LLM inference (LLaMA 4) |
| [Streamlit](https://streamlit.io) | Web UI |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📁 Project Structure

```
Langchain_Projects/
├── main.py           # Main Streamlit app
├── .env              # API keys (not committed)
├── requirements.txt  # Dependencies
└── README.md
```

---

## 📦 Requirements

```txt
langchain
langchain-core
langchain-community
langchain-groq
streamlit
python-dotenv
```

---

## 🔒 Security Note

Never commit your `.env` file. Make sure `.gitignore` includes:

```gitignore
.env
```
