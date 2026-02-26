"""
Hybrid AI client - Uses Groq for text analysis and Gemini for OCR/Vision
"""
from ai.groq_client import GroqClient
from ai.gemini_client import GeminiClient


class HybridAIClient:
    """
    Smart AI client that uses:
    - Groq: For text analysis (high quota: 14,400/day)
    - Gemini: For OCR/Vision only (low quota: 20/day)
    """
    
    def __init__(self, groq_api_key: str = None, gemini_api_key: str = None):
        self.groq_client = GroqClient(groq_api_key) if groq_api_key else None
        self.gemini_client = GeminiClient(gemini_api_key) if gemini_api_key else None
    
    def generate(self, prompt: str) -> str:
        """
        Generate text from a prompt.
        Uses Groq for text, Gemini for vision.
        """
        # Check if this is a vision request
        if "__VISION_BASE64__" in prompt:
            if not self.gemini_client:
                return "[Error: Gemini API key required for OCR/Vision]"
            return self.gemini_client.generate(prompt)
        
        # Use Groq for text analysis (high quota)
        if self.groq_client:
            result = self.groq_client.generate(prompt)
            # If Groq fails, fallback to Gemini
            if result.startswith("[Groq error:") and self.gemini_client:
                return self.gemini_client.generate(prompt)
            return result
        
        # Fallback to Gemini if Groq not available
        if self.gemini_client:
            return self.gemini_client.generate(prompt)
        
        return "[Error: No AI client available]"
