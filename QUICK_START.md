# ⚡ Quick Start Guide

## 🚀 Get Running in 3 Minutes

### Step 1: Clone & Install (1 min)
```bash
git clone https://github.com/yourusername/resume-analyser.git
cd resume-analyser
pip install -r requirements.txt
```

### Step 2: Get API Keys (1 min)

**Groq (Primary):**
1. Go to https://console.groq.com
2. Sign up → Create API Key
3. Copy key (starts with `gsk_`)

**Gemini (OCR):**
1. Go to https://aistudio.google.com
2. Create API Key
3. Copy key (starts with `AIza`)

### Step 3: Run (30 seconds)

**Linux/Mac:**
```bash
export GROQ_API_KEY="gsk_your_key"
export GEMINI_API_KEY="your_key"
streamlit run app.py
```

**Windows:**
```powershell
$env:GROQ_API_KEY="gsk_your_key"
$env:GEMINI_API_KEY="your_key"
streamlit run app.py
```

### Done! 🎉

Open http://localhost:8501 and start analyzing resumes!

---

## 📝 Usage

1. **Upload** resume (PDF, image, or DOCX)
2. **Optional**: Add job description
3. **Optional**: Enter target role
4. Click **"Analyze Resume"**
5. View results and download roadmap PDF

---

## 🆘 Troubleshooting

**"No AI client available"**
→ Set at least one API key

**"Gemini API key required for OCR"**
→ You uploaded a scanned document, add GEMINI_API_KEY

**Quota exceeded**
→ Wait for quota reset (daily) or use different API key

---

## 📚 More Info

- Full documentation: [README.md](README.md)
- Deployment guide: [DEPLOYMENT.md](DEPLOYMENT.md)
- Groq setup: [GROQ_SETUP.md](GROQ_SETUP.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
