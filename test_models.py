from agents.base import ask_agent
from config import PRIMARY_MODEL, COPYWRITER_MODEL, DESIGN_MODEL, TECHNICAL_MODEL, MODELS

def main():
    print("=== Zimeira Multi-Model Test ===")
    print(f"PRIMARY_MODEL    : {PRIMARY_MODEL}")
    print(f"COPYWRITER_MODEL : {COPYWRITER_MODEL}")
    print(f"DESIGN_MODEL     : {DESIGN_MODEL}")
    print(f"TECHNICAL_MODEL  : {TECHNICAL_MODEL}")
    print()

    tests = [
        ("brief", "Balas singkat: Brief agent aktif."),
        ("sales", "Buat 1 kalimat sales yang profesional untuk jasa website UMKM."),
        ("design_director", "Beri 1 arahan desain singkat untuk proposal Zimeira Tech."),
        ("codex_prompt", "Balas singkat: Technical agent aktif."),
    ]

    for agent_name, prompt in tests:
        print(f"\n--- Testing {agent_name} -> {MODELS.get(agent_name)} ---")
        result = ask_agent(
            agent_name,
            "Kamu adalah test agent. Jawab singkat dan jelas.",
            prompt
        )
        print(result[:800])

if __name__ == "__main__":
    main()
