from agents.base import ask_agent, build_knowledge_for_request

def proposal_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    return ask_agent("proposal", """
Kamu adalah Penawaran Agent Zimeira Tech.
Buat penawaran singkat sesuai data yang diisi dan katalog.
Jangan membuat penawaran layanan lain yang tidak diminta.
""", f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Buat penawaran:
1. Judul.
2. Kebutuhan pelanggan.
3. Layanan/paket yang direkomendasikan.
4. Scope pekerjaan.
5. Estimasi biaya dan durasi jika ada.
6. Add-on/custom jika diperlukan.
7. Data yang perlu dilengkapi.
8. CTA.
""")
