def query(prompt):
    return {
        "generated_text": f"(Mock AI) Structural Health Monitoring is a system used to monitor structures like bridges and buildings. You asked: {prompt}"
    }

output = query("Explain structural health monitoring simply.")

print(output["generated_text"])