from agents.base import ask_agent, build_knowledge_for_request

def checklist_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    return ask_agent("checklist", """
Kamu adalah Checklist Agent Zimeira Tech.
Buat daftar kerja sesuai kategori layanan dan data yang diisi.
""", f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Buat checklist:
1. Data awal yang harus dikumpulkan.
2. Konfirmasi scope.
3. Langkah pengerjaan.
4. Pemeriksaan hasil.
5. Revisi/approval.
6. Serah terima.
""")
