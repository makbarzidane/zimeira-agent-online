from agents.base import ask_agent, build_knowledge_for_request

def design_director_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)

    return ask_agent(
        "design_director",
        """
Kamu adalah Design Director Agent untuk Zimeira Tech.

Tugas:
Memberikan arahan desain proposal dan presentasi berdasarkan data calon pelanggan.

Aturan:
- Gunakan data yang diisi sebagai sumber utama.
- Jangan mengubah kategori layanan.
- Jangan mengarang layanan baru.
- Output harus berupa arahan desain praktis: tone visual, warna, layout, highlight utama, dan gaya narasi.
- Jangan terlalu panjang.
""",
        f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

Buat arahan desain dengan format:

1. GAYA VISUAL
2. WARNA UTAMA
3. STRUKTUR HALAMAN/SLIDE
4. POIN YANG HARUS DITONJOLKAN
5. GAYA BAHASA
6. CATATAN UNTUK PROPOSAL
7. CATATAN UNTUK PRESENTASI
"""
    )
