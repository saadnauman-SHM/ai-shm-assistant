from app.core.logger import get_logger

logger = get_logger(__name__)

def mock_response(prompt: str):
    return {
        "generated_text": f"(Mock AI) SHM monitors structures like bridges and buildings. You asked: {prompt}"
    }

def query(prompt: str):
    logger.info(f"Received prompt: {prompt}")

    if not prompt.strip():
        logger.error("Empty prompt received")
        raise ValueError("Question cannot be empty")

    try:
        # 🔴 Placeholder for real AI (blocked in your environment)
        raise Exception("Real AI not available")

    except Exception as e:
        logger.warning(f"Falling back to mock AI: {str(e)}")
        return mock_response(prompt)