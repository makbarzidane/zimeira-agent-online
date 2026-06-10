from agents.base import ask_agent, build_knowledge_for_request

def sales_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    return ask_agent("sales", """
Kamu adalah Sales Agent Zimeira Tech.
Buat balasan WhatsApp berdasarkan data yang diisi.
Jangan mengarah ke layanan lain yang tidak diminta.
Jangan mengarang harga.
""", f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Buat:
1. Balasan pembuka.
2. Layanan yang cocok berdasarkan data.
3. Data yang perlu dilengkapi dengan contoh jawaban.
4. CTA untuk konfirmasi.
""")
