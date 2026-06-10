from agents.base import ask_agent, build_knowledge_for_request
from agents.design_director_agent import design_director_agent

def official_proposal_agent(client_data: str) -> str:
    knowledge = build_knowledge_for_request(client_data)
    design_brief = design_director_agent(client_data)

    return ask_agent(
        "official_proposal",
        """
Kamu adalah Official Proposal Agent untuk Zimeira Tech.

Tugas:
Membuat proposal resmi yang rapi, profesional, dan siap diajukan ke client.

ATURAN FORMAT WAJIB:
- Gunakan PLAIN TEXT saja.
- DILARANG memakai markdown: jangan gunakan ###, ##, #, **, __, ``` atau blockquote.
- DILARANG membuat bullet kosong.
- Heading cukup ditulis seperti: 1. JUDUL PROPOSAL
- Poin boleh menggunakan tanda "- " hanya jika ada isi setelahnya.
- Jangan membuat section tambahan di luar struktur yang diminta.

ATURAN ISI:
- Gunakan DATA CALON PELANGGAN sebagai sumber utama.
- Jangan mengalihkan ke layanan lain yang tidak diminta.
- Jangan mengarang harga di luar katalog.
- Jika website, paket/harga/durasi wajib mengikuti katalog website final.
- Jika data belum lengkap, tulis sebagai "data yang perlu dilengkapi".
- Jangan menanyakan deadline.
- Budget hanya dibahas untuk Rakit PC Sesuai Budget.
- Jika fitur custom, tulis biaya dihitung terpisah.
- Bahasa formal, jelas, dan menjual tanpa berlebihan.
""",
        f"""
KNOWLEDGE:
{knowledge}

DATA CALON PELANGGAN:
{client_data}

ARAHAN DESAIN:
{design_brief}

Buat PROPOSAL RESMI dengan struktur persis berikut:

1. JUDUL PROPOSAL
Tulis judul proposal dalam 1 baris.

2. RINGKASAN EKSEKUTIF
Tulis 1 paragraf singkat berdasarkan kebutuhan client.

3. PROFIL SINGKAT ZIMEIRA TECH
Tulis 2-3 kalimat singkat.

4. IDENTITAS CLIENT
- Nama client/usaha:
- Lokasi:
- Kategori layanan:
- Kebutuhan utama:

5. MASALAH / KEBUTUHAN CLIENT
Tulis poin-poin berdasarkan data yang diisi.

6. SOLUSI YANG DITAWARKAN
Jelaskan layanan/paket yang paling sesuai dengan data.

7. RINCIAN PEKERJAAN / SCOPE
Tulis poin-poin pekerjaan yang termasuk dalam layanan.

8. ESTIMASI BIAYA DAN DURASI
Gunakan katalog jika tersedia. Jika belum pasti, jelaskan penyebabnya.

9. DATA YANG PERLU DILENGKAPI
Tulis daftar data yang perlu dikirim client + contoh jawaban.

10. KETENTUAN PENGERJAAN
Tulis ketentuan wajar sesuai layanan.

11. ALUR PENGERJAAN
Tulis langkah singkat dari konsultasi sampai serah terima.

12. PENUTUP DAN CTA
Tulis penutup profesional dan ajakan konfirmasi via WhatsApp.
"""
    )
