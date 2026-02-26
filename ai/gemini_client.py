"""
Gemini API client — handles text and vision (base64) inputs.
"""
from google import genai
from google.genai import types
from PIL import Image
import base64
import io


class GeminiClient:
    MODEL = "gemini-flash-latest"  # Better quota limits than 2.5-flash

    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model = self.MODEL

    def generate(self, prompt: str) -> str:
        """
        Generate text from a prompt.
        If the prompt contains __VISION_BASE64__, uses the Vision API.
        """
        if "__VISION_BASE64__" in prompt:
            return self._generate_vision(prompt)

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.3,
                    max_output_tokens=4096,
                )
            )
            return response.text
        except Exception as e:
            return f"[Gemini error: {e}]"

    def _generate_vision(self, prompt: str) -> str:
        """Handle image/PDF inputs via Gemini Vision."""
        try:
            # Extract the base64 portion
            marker = "__VISION_BASE64__"
            idx = prompt.index(marker) + len(marker)
            payload = prompt[idx:].strip()
            mime_type, b64_data = payload.split("::", 1)
            image_bytes = base64.b64decode(b64_data)

            if mime_type == "application/pdf":
                # Use inline data for PDF
                parts = [
                    types.Part.from_bytes(data=image_bytes, mime_type="application/pdf"),
                    "Extract all text from this document. Return the raw text only, preserving structure."
                ]
            else:
                # Use image
                img = Image.open(io.BytesIO(image_bytes))
                parts = [
                    types.Part.from_image(image=img),
                    "Extract all text from this resume image. Return the raw text only, preserving structure."
                ]
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=parts
            )
            return response.text
        except Exception as e:
            return f"[Vision error: {e}]"
