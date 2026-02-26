"""
PDF text extraction — handles both text-based and (fallback) scanned PDFs.
"""
import io


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract text from a PDF file.
    Returns extracted text string; may be empty for scanned/image-only PDFs.
    """
    try:
        import pdfplumber

        text_parts = []
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

        return "\n\n".join(text_parts)

    except ImportError:
        # Fallback to pypdf if pdfplumber not available
        try:
            from pypdf import PdfReader

            reader = PdfReader(io.BytesIO(pdf_bytes))
            text_parts = []
            for page in reader.pages:
                text_parts.append(page.extract_text() or "")
            return "\n\n".join(text_parts)

        except Exception as e:
            return f"[PDF extraction error: {e}]"

    except Exception as e:
        return f"[PDF extraction error: {e}]"
