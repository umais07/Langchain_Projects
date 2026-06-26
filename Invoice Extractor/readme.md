

# 🧾 Multi-Language Invoice Extractor

An AI-powered invoice understanding app built with **LangChain** and **Streamlit**. Upload invoices in any language and extract structured data — or ask targeted questions and get precise answers.

---

## ✨ How It Works

The app uses a two-stage query design:

1. **System Prompt First** — On every query, the model extracts the full invoice breakdown (vendor, items, totals, shipping, tax, etc.) as structured context.
2. **Targeted Answer Second** — It then answers your specific question on top of that context.

> **Result:** Ask for everything → get the full breakdown. Ask just about shipping → get only shipping. No noise, no hallucinations.

---

## 🖼️ Demo

**Query 1 — Full Invoice Extraction**

<img width="829" height="824" alt="image" src="https://github.com/user-attachments/assets/63b8eda4-93d6-4e0c-83ba-112dc8425951" />
<br><br>
<img width="916" height="825" alt="image" src="https://github.com/user-attachments/assets/33c5218d-a408-4147-8076-6fe2d2c6bd86" />

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🦜 **LangChain** | Prompt chaining & LLM orchestration |
| 🎈 **Streamlit** | Interactive UI |
| 🤖 **Groq** | Vision + language understanding |

---
