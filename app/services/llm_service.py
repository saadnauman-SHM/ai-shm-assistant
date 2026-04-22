def query(prompt: str):
    if not prompt.strip():
        raise ValueError("Question cannot be empty")

    return {
        "generated_text": f"(Mock AI) Structural Health Monitoring (SHM) is used to monitor structures like bridges and buildings. You asked: {prompt}"
    }