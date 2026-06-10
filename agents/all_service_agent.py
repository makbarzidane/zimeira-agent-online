from agents.base import ask_agent, build_knowledge_for_request
from agents.service_detector import is_website_request

def all_service_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    website_rule = (
        "Jika website: wajib pakai katalog website final; cafe/resto/homestay/travel/kuliner/lembaga kecil arahkan ke UMKM Profesional; banyak produk/menu/varian arahkan ke Website Katalog Produk."
        if is_website_request(client_data) else
        "Jika bukan website, fokus hanya ke kategori layanan yang dipilih."
    )
    return ask_agent("all_service", f"""
Kamu adalah Zimeira Service Agent.
Aturan:
- Gunakan data yang diisi sebagai sumber utama.
- Jangan mengalihkan ke layanan lain yang tidak diminta.
- Jika data kurang, tulis data yang perlu dilengkapi, jangan mengarang.
- Jangan menanyakan deadline.
- Budget hanya untuk Rakit PC.
- Jangan mengarang harga di luar katalog.
- {website_rule}
""", f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Buat output:
1. KATEGORI LAYANAN
2. BALASAN WHATSAPP
3. RINGKASAN KEBUTUHAN
4. DATA YANG MASIH PERLU DILENGKAPI + contoh jawaban
5. REKOMENDASI LAYANAN / PAKET
6. ESTIMASI BIAYA DAN DURASI
7. CHECKLIST PENGERJAAN
8. CATATAN TEKNIS / PROMPT CODEX
""")
