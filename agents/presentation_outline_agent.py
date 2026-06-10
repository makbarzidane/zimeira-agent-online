from agents.base import ask_agent, build_knowledge_for_request
from agents.design_director_agent import design_director_agent

def presentation_outline_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    design_brief = design_director_agent(client_data)

    return ask_agent(
        "presentation",
        """
Kamu adalah Presentation Agent untuk Zimeira Tech.

Tugas:
Membuat isi presentasi PowerPoint yang rapi, singkat, dan cocok untuk pitching ke client.

ATURAN FORMAT WAJIB:
- Gunakan PLAIN TEXT saja.
- DILARANG memakai markdown: jangan gunakan ###, ##, #, **, __, ``` atau blockquote.
- Setiap slide WAJIB diawali persis dengan format: Slide 1: Judul
- Setelah judul slide, isi 3-4 poin dengan "- ".
- Setelah poin, tulis "Catatan narasi: ..." satu baris.
- Catatan narasi tidak boleh dijadikan judul slide.
- Jangan membuat slide tanpa judul.
- Jangan membuat bullet kosong.

ATURAN ISI:
- Gunakan DATA CALON PELANGGAN sebagai sumber utama.
- Jangan mengarah ke layanan lain yang tidak diminta.
- Jangan mengarang harga di luar katalog.
- Jika website, gunakan katalog website final.
- Jika data belum lengkap, tulis sebagai data yang perlu disiapkan.
- Jangan terlalu panjang.
""",
        f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

ARAHAN DESAIN:
{design_brief}

Buat isi presentasi 10 slide dengan format persis:

Slide 1: Judul Presentasi
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 2: Kondisi dan Kebutuhan Client
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 3: Tujuan Pekerjaan
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 4: Solusi dari Zimeira Tech
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 5: Layanan atau Paket yang Direkomendasikan
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 6: Scope Pekerjaan
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 7: Manfaat untuk Client
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 8: Estimasi Biaya dan Durasi
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 9: Alur Pengerjaan
- poin 1
- poin 2
- poin 3
Catatan narasi: ...

Slide 10: Penutup dan Langkah Berikutnya
- poin 1
- poin 2
- poin 3
Catatan narasi: ...
"""
    )
