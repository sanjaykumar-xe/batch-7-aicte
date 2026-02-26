"""
Image-based OCR using pytesseract (with pdf2image for scanned PDFs).
Falls back to base64 + Gemini Vision if tesseract is unavailable.
"""
import io
import base64


def extract_text_from_image(file_bytes: bytes, is_pdf: bool = False) -> str:
    """
    Extract text from image bytes (PNG/JPG) or a scanned PDF.
    Tries pytesseract first, then returns base64 placeholder for Gemini Vision.
    """
    try:
        from PIL import Image
        import pytesseract

        if is_pdf:
            try:
                from pdf2image import convert_from_bytes
                images = convert_from_bytes(file_bytes)
            except ImportError:
                # pdf2image not installed, return raw for Gemini
                return _base64_fallback(file_bytes, is_pdf=True)

            text_parts = []
            for img in images:
                text_parts.append(pytesseract.image_to_string(img))
            return "\n\n".join(text_parts)
        else:
            img = Image.open(io.BytesIO(file_bytes))
            return pytesseract.image_to_string(img)

    except ImportError:
        # pytesseract not available — return base64 string so Gemini Vision handles it
        return _base64_fallback(file_bytes, is_pdf=is_pdf)
    except Exception as e:
        return _base64_fallback(file_bytes, is_pdf=is_pdf)


def _base64_fallback(file_bytes: bytes, is_pdf: bool = False) -> str:
    """
    Return a special marker so the Gemini client knows to use Vision API.
    """
    b64 = base64.b64encode(file_bytes).decode("utf-8")
    mime = "application/pdf" if is_pdf else "image/png"
    return f"__VISION_BASE64__{mime}::{b64}"
