"""
Groq API client for text generation (high quota, fast inference)
"""
from groq import Groq


class GroqClient:
    MODEL = "llama-3.3-70b-versatile"  # Best model for analysis
    
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
        self.model = self.MODEL
    
    def generate(self, prompt: str) -> str:
        """Generate text from a prompt using Groq."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert resume analyst and career coach. Provide detailed, accurate, and helpful analysis."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=4096,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[Groq error: {e}]"
