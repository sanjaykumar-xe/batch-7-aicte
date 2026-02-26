# Resume Analyser - Project Structure

## 📁 Directory Structure

```
resume-analyser/
├── .streamlit/
│   └── secrets.toml.example      # Streamlit secrets template
├── ai/
│   ├── __init__.py
│   ├── gemini_client.py          # Gemini API client (text + vision)
│   └── prompts.py                # AI prompt templates
├── ocr/
│   ├── __init__.py
│   ├── pdf_text_extractor.py    # PDF text extraction
│   └── image_ocr.py              # Image OCR (pytesseract + Gemini Vision)
├── utils/
│   ├── __init__.py
│   ├── file_handler.py           # File type detection + DOCX extraction
│   └── pdf_generator.py          # Career roadmap PDF generation
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── app.py                        # Main Streamlit application
├── DEPLOYMENT.md                 # Deployment instructions
├── PROJECT_STRUCTURE.md          # This file
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies
```

## 🔧 Core Components

### Main Application (`app.py`)
- Streamlit UI with custom CSS
- Hero section with animations
- File upload handling
- Resume analysis workflow
- Results visualization

### AI Module (`ai/`)
- **gemini_client.py**: Handles all Gemini API calls
  - Text generation
  - Vision API for scanned documents
  - Error handling
- **prompts.py**: Structured prompts for:
  - Resume cleanup
  - Skill extraction
  - Resume scoring
  - JD matching
  - Improvement suggestions
  - Career roadmap generation

### OCR Module (`ocr/`)
- **pdf_text_extractor.py**: Extracts text from PDFs using pdfplumber
- **image_ocr.py**: OCR for images/scanned PDFs
  - Primary: pytesseract
  - Fallback: Gemini Vision API

### Utils Module (`utils/`)
- **file_handler.py**: File type detection and DOCX text extraction
- **pdf_generator.py**: Generates styled career roadmap PDFs

## 🎨 Features

1. **Resume Upload**: PDF, PNG, JPG, DOCX support
2. **AI Analysis**:
   - Text extraction and cleanup
   - Skill extraction (technical, soft skills, tools)
   - Resume scoring (0-100)
   - ATS compatibility check
   - Improvement suggestions
3. **Job Description Matching** (optional)
4. **Career Roadmap** (optional)
5. **PDF Export** for roadmap

## 🔐 Security

- API key loaded from environment variables only
- No API key input in UI
- `.env` and `secrets.toml` in `.gitignore`
- Ready for secure deployment

## 📊 API Usage

**Per Resume Analysis:**
- Basic: 5 API calls
- With JD: 6 API calls
- With Roadmap: 6 API calls
- Full (JD + Roadmap): 7 API calls

**Free Tier Limits:**
- gemini-flash-latest: ~20-50 requests/day
- Allows 2-4 full resume analyses per day

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export GEMINI_API_KEY="your_api_key_here"

# Run app
streamlit run app.py
```

## 📝 Code Quality

- Clean, modular architecture
- Single responsibility principle
- Type hints where applicable
- Error handling throughout
- No unused imports or test files
- Optimized for performance
