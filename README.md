# ASK-PDF
# 📄 AskMyPDF — Gemini-powered PDF Q\&A App

AskMyPDF is a smart and lightweight application that lets you upload any PDF file and ask questions related to its content. Powered by Google's Gemini API, it provides detailed answers and summaries directly from the uploaded document — with built-in **page tracking** support.

---

## 🚀 Features

* 📥 Upload any PDF
* 🤖 Ask natural language questions about the content
* 📌 Get full answers **and concise summaries**
* 🧠 Summarize the entire PDF
* 🔍 **NEW: Page Tracking** — identifies the page number(s) where the answer likely exists
* ⚙️ Built with **Streamlit** UI (optional CLI version possible)

---

## 🛠 Tech Stack

| Layer        | Tools                   |
| ------------ | ----------------------- |
| Backend      | Python 3.11 / 3.12      |
| LLM          | Google Gemini 1.5 Flash |
| File Parsing | PyPDF2                  |
| UI           | Streamlit               |
| Secrets      | `.env`, `python-dotenv` |

---

## 📦 Installation & Setup

### ✅ Prerequisites:

* Python 3.11 or 3.12
* `pip` installed

### 📁 Step-by-step:

```bash
# Clone the repo
git clone https://github.com/yourusername/AskMyPDF.git
cd AskMyPDF

# Create and activate virtual environment
python -m venv venv_311
venv_311\Scripts\activate  # Windows
source venv_311/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Rename .env.template to .env
# Inside .env, add:
GOOGLE_API_KEY=your_gemini_api_key
```

---

## ▶️ Running the App 
Run below command in terminal

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
.
├── app.py                  # Streamlit frontend
├── pdf_reader.py          # PDF processing (with page mapping)
├── gemini_qa.py           # Gemini API logic + page tracking
├── requirements.txt
├── .env                   # API Key (not tracked)
└── .gitignore             # Ignore env & secret files
```

---

## 📌 Example Use Cases

* Ask: "‘Courage, friends, and do not yield!’who is the person speaking these lines and on which page no. of pdf ?"
* Ask: "Who is the author of this book?"
* Ask: "Which page mentions marketing strategy?"
* Ask: "List all expense categories where actual exceeded budget.”

---


## 📚 Sample PDF

You can test with annual reports, product brochures, research papers, or books.

---

## 🧪 Future Improvements

* Use embeddings for smarter chunk selection
* Add audio/text-to-speech responses
* Export answers to Word or PDF
* Mobile UI

---

## 📜 License

MIT — feel free to use, fork, and extend.
