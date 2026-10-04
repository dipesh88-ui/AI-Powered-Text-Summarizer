# 🤖 AI Text Summarizer using T5 & FastAPI

An AI-powered **Text Summarization application** built using **Python, FastAPI, Hugging Face Transformers, and the T5 model**.

The application allows users to enter or paste long text and generates a concise summary using a Transformer-based NLP model.

## 🚀 Features

- 📝 Summarize long text using AI
- 🤖 T5 Transformer model for text summarization
- ⚡ FastAPI backend
- 🌐 Simple and responsive web interface
- 🔄 REST API endpoint for summarization
- 💻 Supports CPU, CUDA, and Apple MPS when available
- 🧹 Text preprocessing and cleaning
- 📦 Easy local setup

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic

### Machine Learning / NLP
- PyTorch
- Hugging Face Transformers
- T5 (`t5-small`)
- SentencePiece

### Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

## 📂 Project Structure

```text
AI-Text-Summarizer-T5-FastAPI/
│
├── app.py
├── index.html
├── requirements.txt
├── run.bat
├── text_summarizer.ipynb
├── .gitignore
│
└── saved_summary_model/
    └── # Optional locally trained/saved model
```

> **Note:** The trained model directory is excluded from GitHub because large model files can exceed GitHub's file-size limits.

## ⚙️ How It Works

The application follows the following pipeline:

```text
User Input
    ↓
Text Preprocessing
    ↓
"T5 Summarize" Prompt
    ↓
T5 Transformer Model
    ↓
Text Generation
    ↓
Generated Summary
    ↓
Web Interface
```

The backend cleans the input text by removing unnecessary whitespace and HTML tags before passing it to the T5 tokenizer. The model then generates the summary using beam search. 

## 🧠 Model

This project uses the **T5 (Text-To-Text Transfer Transformer)** architecture through Hugging Face Transformers.

The application first checks whether a locally saved model exists. If not, it falls back to:

```text
t5-small
```

The model generates summaries using:

- Maximum input length: `512`
- Maximum output length: `150`
- Beam search: `4 beams`
- Early stopping: Enabled

## 🔌 API Endpoint

### `POST /summarize/`

Generates a summary from the provided text.

### Request

```json
{
    "dialogue": "Enter your text here..."
}
```

### Response

```json
{
    "summary": "Generated summary..."
}
```

## 🖥️ Web Interface

The frontend provides a simple interface where users can:

1. Enter or paste text.
2. Click the **Summarize** button.
3. Wait for the AI model to process the text.
4. View the generated summary.

The frontend communicates with the FastAPI backend using a POST request to `/summarize/`. 

## 📋 Requirements

The main dependencies include:

```text
fastapi
uvicorn
transformers
torch
sentencepiece
jinja2
pydantic
```

These dependencies are listed in `requirements.txt`.

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Text-Summarizer-T5-FastAPI.git
```

### 2. Open the project

```bash
cd AI-Text-Summarizer-T5-FastAPI
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server using:

```bash
uvicorn app:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## 📓 Jupyter Notebook

The repository also contains:

```text
text_summarizer.ipynb
```

The notebook can be used for experimenting with the text summarization model and related NLP workflow.

## 📁 Model Handling

The application supports loading a locally saved model from:

```text
saved_summary_model/
```

If the local model is unavailable, the application automatically uses:

```text
t5-small
```

The `saved_summary_model/` directory and large model files are ignored by Git according to the project's `.gitignore`.

## 🔮 Future Improvements

- [ ] Support PDF and DOCX summarization
- [ ] Add multiple summarization modes
- [ ] Add multilingual summarization
- [ ] Improve UI/UX
- [ ] Add user authentication
- [ ] Deploy the application online
- [ ] Add summarization history
- [ ] Add model selection
- [ ] Add document upload support

## 📸 Demo

Add screenshots or a GIF of the application here:

```markdown
![Text Summarizer Demo](screenshots/demo.png)
```

## 👨‍💻 Author

**Dipesh Kumar**

B.Tech Computer Science & Engineering

---

⭐ If you find this project useful, consider giving it a **star** on GitHub!

## 📄 License

This project is intended for educational and learning purposes.
