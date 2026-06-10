from agents.base import ask_agent, build_knowledge_for_request

def brief_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    return ask_agent("brief", """
Kamu adalah Brief Agent Zimeira Tech.
Ubah data calon pelanggan menjadi brief pekerjaan.
Fokus hanya pada kategori dan data yang diisi.
""", f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Buat brief:
1. Kategori layanan.
2. Ringkasan kebutuhan.
3. Tujuan pekerjaan.
4. Data yang sudah tersedia.
5. Data yang masih kurang.
6. Pertanyaan lanjutan + contoh jawaban.
""")
