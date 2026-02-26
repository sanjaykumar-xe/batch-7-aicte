# ⚡ Resume Analyser — AI-Powered Resume Analysis

> Professional resume analysis tool powered by Groq AI and Gemini Vision

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-AI-orange?style=for-the-badge)](https://groq.com)
[![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 📂 **Smart Upload** | PDF (text + scanned), PNG/JPG, DOCX support |
| 🔍 **Hybrid OCR** | pdfplumber → pytesseract → Gemini Vision fallback |
| 🧠 **AI Analysis** | Resume cleanup, skill extraction, scoring (0-100) |
| 📊 **ATS Check** | Applicant Tracking System compatibility analysis |
| ⚡ **Skill Extraction** | Technical skills, soft skills, tools, experience |
| ✍️ **Improvements** | Section tips, bullet rewrites, action verbs |
| 🎯 **JD Matching** | Match %, missing skills, ATS keyword gaps |
| 🗺️ **Career Roadmap** | Beginner → Advanced with resources + PDF download |

---

## 🎨 Screenshots

### Hero Section
Modern, animated interface with smooth transitions and professional design.

### Analysis Results
Comprehensive resume scoring with strengths, weaknesses, and actionable improvements.

---

## 🏗️ Architecture

### Hybrid AI System
- **Groq AI** (Primary): Text analysis with 14,400 requests/day
- **Gemini Vision** (Fallback): OCR for scanned documents

### Tech Stack
- **Frontend**: Streamlit with custom CSS animations
- **AI Models**: Llama 3.3 70B (Groq) + Gemini Flash (Google)
- **OCR**: pdfplumber, pytesseract, Gemini Vision
- **PDF Generation**: ReportLab

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- Groq API key (free, 14,400 requests/day)
- Gemini API key (free, for OCR only)

### Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/resume-analyser.git
cd resume-analyser

# Install dependencies
pip install -r requirements.txt

# Set API keys
export GROQ_API_KEY="gsk_your_groq_key"
export GEMINI_API_KEY="your_gemini_key"

# Run app
streamlit run app.py
```

### Windows (PowerShell)
```powershell
$env:GROQ_API_KEY="gsk_your_groq_key"
$env:GEMINI_API_KEY="your_gemini_key"
python -m streamlit run app.py
```

---

## 🔑 Getting API Keys

### Groq API (Primary - High Quota)
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up (free, takes 30 seconds)
3. Go to [API Keys](https://console.groq.com/keys)
4. Create new key
5. Copy key (starts with `gsk_`)

**Quota**: 14,400 requests/day (~2,000 resume analyses)

### Gemini API (OCR Only)
1. Visit [Google AI Studio](https://aistudio.google.com)
2. Create API key
3. Copy key (starts with `AIza`)

**Quota**: 20 requests/day (only used for scanned documents)

---

## 📁 Project Structure

```
resume-analyser/
├── ai/
│   ├── gemini_client.py      # Gemini Vision API client
│   ├── groq_client.py         # Groq text generation client
│   ├── hybrid_client.py       # Smart routing between APIs
│   └── prompts.py             # AI prompt templates
├── ocr/
│   ├── pdf_text_extractor.py # PDF text extraction
│   └── image_ocr.py           # Image OCR with fallbacks
├── utils/
│   ├── file_handler.py        # File type detection
│   └── pdf_generator.py       # Career roadmap PDF export
├── .streamlit/
│   └── secrets.toml.example   # Secrets template
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
├── DEPLOYMENT.md              # Deployment guide
├── GROQ_SETUP.md              # Groq setup instructions
└── README.md                  # This file
```

---

## 🎯 Usage

### Basic Analysis
1. Upload resume (PDF, image, or DOCX)
2. Click "Analyze Resume"
3. View results: score, skills, improvements

### Job Description Matching
1. Upload resume
2. Paste job description
3. Get match percentage and missing skills

### Career Roadmap
1. Upload resume
2. Enter target role (e.g., "Senior Data Scientist")
3. Get personalized learning path with resources
4. Download as PDF

---

## 📊 API Usage & Quotas

### Per Resume Analysis

| Feature | Groq Calls | Gemini Calls | Total |
|---------|------------|--------------|-------|
| Basic (no JD, no roadmap) | 5 | 0-1* | 5-6 |
| With Job Description | 6 | 0-1* | 6-7 |
| With Career Roadmap | 6 | 0-1* | 6-7 |
| Full Analysis (JD + Roadmap) | 7 | 0-1* | 7-8 |

*Gemini only used if resume is scanned/image

### Daily Capacity (Free Tier)

- **Basic analysis**: ~2,400 resumes/day
- **Full analysis**: ~1,800 resumes/day

---

## 🚀 Deployment

### Streamlit Cloud

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Add secrets in Settings → Secrets:
   ```toml
   GROQ_API_KEY = "gsk_your_key"
   GEMINI_API_KEY = "your_key"
   ```
5. Deploy!

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 🔒 Security

- ✅ API keys loaded from environment variables only
- ✅ No API key input in UI
- ✅ `.env` and `secrets.toml` in `.gitignore`
- ✅ Ready for secure deployment
- ✅ No sensitive data stored

---

## 🛠️ Development

### Running Tests
```bash
# Test Groq client
python -c "from ai.groq_client import GroqClient; print(GroqClient('your_key').generate('Hello'))"

# Test Gemini client
python -c "from ai.gemini_client import GeminiClient; print(GeminiClient('your_key').generate('Hello'))"
```

### Code Quality
- Clean, modular architecture
- Type hints where applicable
- Comprehensive error handling
- No unused imports or dead code

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

## 🌟 Acknowledgments

- **Groq** for providing high-quota free AI API
- **Google** for Gemini Vision API
- **Streamlit** for the amazing web framework
- **Open source community** for various libraries used

---

**Built with Responsibility** 💚

*AI-powered resume analysis for everyone, completely free.*
