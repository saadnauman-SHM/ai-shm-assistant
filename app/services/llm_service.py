def mock_response(prompt: str):
    print("🔥 DEBUG: mock_response is running")

    prompt_lower = prompt.lower()

    if "bridge" in prompt_lower or "bridges" in prompt_lower:
        answer = "In bridges, SHM helps detect cracks, vibrations, and structural damage early to prevent failures."

    elif "sensor" in prompt_lower or "sensors" in prompt_lower:
        answer = "SHM systems use sensors such as accelerometers, strain gauges, and temperature sensors to monitor structural behavior."

    elif "damage" in prompt_lower or "crack" in prompt_lower:
        answer = "SHM identifies structural damage like cracks, corrosion, and fatigue before failure occurs."

    elif "shm" in prompt_lower or "structural health monitoring" in prompt_lower:
        answer = "Structural Health Monitoring (SHM) is a system used to monitor the condition of structures like bridges, buildings, and pipelines using sensors and data analysis."

    else:
        answer = "SHM is used to monitor and maintain the safety of engineering structures."

    return {
        "generated_text": f"(Smart Mock AI) {answer}"
    }

def query(prompt: str):
    return mock_response(prompt)