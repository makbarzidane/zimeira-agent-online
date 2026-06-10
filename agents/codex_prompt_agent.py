from agents.base import ask_agent, build_knowledge_for_request

def codex_prompt_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    return ask_agent("codex_prompt", """
Kamu adalah Codex Prompt Agent.
Jika data mengarah ke website/app, buat prompt Codex.
Jika bukan website/app, jangan membuat prompt coding; buat catatan teknis layanan.
""", f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Jika website/app:
Buat prompt Codex berisi paket yang dipilih, tujuan, stack, halaman, fitur, UI/UX, SEO, responsive, dan kriteria selesai.

Jika bukan website/app:
Buat catatan teknis pengerjaan sesuai kategori layanan.
""")
