# 🚀 Groq API Setup Guide

## Why Groq?

✅ **14,400 requests per day** (vs Gemini's 20)  
✅ **Completely FREE** forever  
✅ **Very fast** inference  
✅ **High quality** Llama 3.3 70B model  

## Get Your Free Groq API Key

### Step 1: Sign Up
1. Go to https://console.groq.com
2. Click "Sign Up" or "Get Started"
3. Sign up with Google, GitHub, or email

### Step 2: Create API Key
1. Once logged in, go to https://console.groq.com/keys
2. Click "Create API Key"
3. Give it a name (e.g., "Resume Analyser")
4. Copy the API key (starts with `gsk_...`)

### Step 3: Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="gsk_your_api_key_here"
```

**Linux/Mac:**
```bash
export GROQ_API_KEY="gsk_your_api_key_here"
```

**Or create `.streamlit/secrets.toml`:**
```toml
GROQ_API_KEY = "gsk_your_api_key_here"
GEMINI_API_KEY = "your_gemini_key_here"
```

## Run the App

```bash
# Set both API keys
$env:GROQ_API_KEY="gsk_your_groq_key"
$env:GEMINI_API_KEY="your_gemini_key"

# Run app
streamlit run app.py
```

## How It Works

The app now uses a **hybrid approach**:

1. **Groq (Primary)** - For all text analysis:
   - Resume cleanup
   - Skill extraction
   - Resume scoring
   - Improvements
   - JD matching
   - Career roadmap
   
2. **Gemini (OCR only)** - For scanned documents:
   - Image OCR
   - Scanned PDF text extraction
   - Vision API tasks

## Quota Comparison

| Task | Groq Calls | Gemini Calls | Total |
|------|------------|--------------|-------|
| Basic Analysis | 5 | 0-1* | 5-6 |
| With JD | 6 | 0-1* | 6-7 |
| With Roadmap | 6 | 0-1* | 6-7 |
| Full Analysis | 7 | 0-1* | 7-8 |

*Only uses Gemini if resume is scanned/image

## Daily Capacity

With Groq's 14,400 requests/day:
- **Basic analysis**: ~2,400 resumes/day
- **Full analysis**: ~1,800 resumes/day

## Troubleshooting

**Error: "No AI client available"**
- Make sure you set at least one API key (GROQ_API_KEY or GEMINI_API_KEY)

**Error: "Gemini API key required for OCR/Vision"**
- You uploaded a scanned PDF/image but only have Groq key
- Add GEMINI_API_KEY for OCR support

**Groq API errors**
- App will automatically fallback to Gemini if Groq fails
- Check your Groq API key is valid

## Free Tier Limits

**Groq:**
- 14,400 requests/day
- 30 requests/minute
- No expiration

**Gemini:**
- 20 requests/day (only used for OCR now)
- 2 requests/minute

## Need More?

If you need even more capacity:
- Groq Pro: $0.27 per million tokens
- Gemini Paid: $0.35 per million tokens

But the free tier should handle thousands of resumes per day!
