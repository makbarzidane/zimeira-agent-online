from agents.base import ask_agent, build_knowledge_for_request

def reviewer_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    return ask_agent("reviewer", """
Kamu adalah Reviewer Agent Zimeira Tech.
Review data/brief/hasil pekerjaan berdasarkan kategori dan katalog.
""", f"""
KNOWLEDGE:
{knowledge}

DATA YANG DIREVIEW:
{client_data}

Buat review:
1. Kategori layanan.
2. Kesesuaian dengan data dan katalog.
3. Kelebihan.
4. Kekurangan.
5. Data yang perlu dilengkapi.
6. Risiko/kendala.
7. Saran perbaikan.
""")
