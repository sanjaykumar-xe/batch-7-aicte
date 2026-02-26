#!/bin/bash
# Quick setup script for Resume Analyser

echo "🚀 Resume Analyser Setup"
echo "========================"
echo ""

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create secrets directory
echo ""
echo "📁 Creating .streamlit directory..."
mkdir -p .streamlit

# Check for API keys
echo ""
echo "🔑 API Key Setup"
echo "================"
echo ""

if [ -z "$GROQ_API_KEY" ]; then
    echo "⚠️  GROQ_API_KEY not set"
    echo "   Get your free key at: https://console.groq.com"
else
    echo "✓ GROQ_API_KEY is set"
fi

if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  GEMINI_API_KEY not set"
    echo "   Get your free key at: https://aistudio.google.com"
else
    echo "✓ GEMINI_API_KEY is set"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the app:"
echo "  export GROQ_API_KEY='your_groq_key'"
echo "  export GEMINI_API_KEY='your_gemini_key'"
echo "  streamlit run app.py"
