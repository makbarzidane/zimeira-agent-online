from agents.service_detector import detect_general_service, is_website_request

def ensure_text(value, default="Belum ada output."):
    if value is None:
        return default
    if isinstance(value, str):
        return value.strip() or default
    return str(value).strip() or default

def local_output(agent_name: str, client_data: str) -> str:
    service = detect_general_service(client_data)
    web = is_website_request(client_data)
    if web:
        recommendation = """Rekomendasi website:
- Landing Page Basic: Rp900.000 | 2-4 hari.
- Website Portofolio Pribadi: Rp1.200.000 | 3-5 hari.
- Website Usaha Starter: Rp2.500.000 | 5-8 hari.
- UMKM Profesional: Rp3.800.000 | 7-12 hari.
- Website Katalog Produk: Rp5.500.000 | 12-18 hari.
- Cafe/resto/homestay/travel/kuliner/lembaga kecil diarahkan ke UMKM Profesional.
- Banyak produk/menu/varian diarahkan ke Website Katalog Produk."""
    else:
        recommendation = """Rekomendasi umum:
Fokus pada kategori layanan yang dipilih. Jika komputer/laptop, cek kondisi perangkat. Jika desain, minta ukuran, teks, logo, warna, referensi. Jika print/download, pastikan file legal dan detail cetak jelas. Budget hanya untuk Rakit PC."""
    return f"""[LOCAL FALLBACK - API tidak mengembalikan output valid]

Agent: {agent_name}
Kategori terdeteksi: {service}

Data calon pelanggan:
{client_data}

{recommendation}

Data yang perlu dilengkapi:
- Nama pelanggan/usaha
- Lokasi
- Detail kebutuhan
- File/foto/referensi jika ada
- Nomor WhatsApp aktif

Balasan singkat:
Bisa kak, Zimeira Tech dapat bantu untuk kebutuhan tersebut. Saya akan sesuaikan dengan kategori layanan dan katalog yang tersedia. Silakan lengkapi data yang masih kurang agar estimasi dan scope bisa dibuat lebih tepat.
""".strip()
