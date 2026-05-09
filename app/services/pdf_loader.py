from pypdf import PdfReader
from app.core.logger import get_logger

logger = get_logger(__name__)


def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        logger.info(f"Successfully extracted text from {pdf_path}")

        return text

    except Exception as e:
        logger.error(f"PDF extraction failed for {pdf_path}: {e}")
        return ""