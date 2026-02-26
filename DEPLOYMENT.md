# Deployment Guide

## Streamlit Cloud Deployment

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Set main file path: `app.py`
   - Click "Advanced settings" > "Secrets"
   - Add your secret:
     ```toml
     GEMINI_API_KEY = "AIzaSyBendq1WVjyuJtp3wBMOFpHrwWx126wUdI"
     ```
   - Click "Deploy"

## Vercel Deployment (Alternative)

Note: Vercel is primarily for Next.js/React apps. For Python/Streamlit, use Streamlit Cloud instead.

If you want to use Vercel, you'll need to:
1. Convert the app to a web framework like FastAPI
2. Use Vercel's Python runtime
3. Set environment variables in Vercel dashboard

## Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd resume
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variable**
   
   Windows (PowerShell):
   ```powershell
   $env:GEMINI_API_KEY="your_api_key_here"
   ```
   
   Linux/Mac:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
   
   Or create a `.streamlit/secrets.toml` file:
   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Security Notes

- ✅ API key is loaded from environment variables only
- ✅ No API key input field in the UI
- ✅ `.env` and `secrets.toml` are in `.gitignore`
- ✅ Never commit API keys to version control
- ✅ Use Streamlit Cloud secrets for deployment
