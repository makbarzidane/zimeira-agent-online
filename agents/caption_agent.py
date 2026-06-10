from agents.base import ask_agent, build_knowledge_for_request

def caption_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    return ask_agent("caption", """
Kamu adalah Caption Agent Zimeira Tech.
Buat caption promosi berdasarkan kategori layanan yang diisi.
Jangan mengarah ke layanan lain.
""", f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Buat:
1. Caption Facebook group bisnis lokal.
2. Caption Instagram maksimal 5 hashtag.
3. Caption WhatsApp Story.
""")
