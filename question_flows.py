SERVICE_CATEGORIES = [
    "Website & SEO",
    "Komputer & Laptop",
    "Cleaning / Repasta Laptop-PC",
    "Rakit PC Sesuai Budget",
    "Penggantian Part Laptop-PC",
    "Desain Promosi",
    "Download, Print & Dokumen",
    "Maintenance Website",
    "Konsultasi Umum",
]

QUESTION_FLOWS = {
    "Website & SEO": [
        {"key": "jenis_bisnis", "label": "Jenis bisnis/usaha", "help": "Contoh: cafe, toko, jasa travel, homestay, klinik, kursus, kontraktor, personal portfolio.", "placeholder": "Contoh: Cafe dan resto kecil di Pagaralam"},
        {"key": "tujuan_website", "label": "Tujuan utama website", "help": "Contoh: agar usaha terlihat profesional, menampilkan menu, memudahkan order WhatsApp, menampilkan galeri.", "placeholder": "Contoh: Menampilkan menu, promo, galeri, lokasi, dan tombol order WhatsApp"},
        {"key": "konten_yang_ditampilkan", "label": "Konten yang ingin ditampilkan", "help": "Contoh: profil usaha, daftar layanan/produk, galeri, testimoni, lokasi, jam buka, kontak.", "placeholder": "Contoh: Profil cafe, menu makanan/minuman, promo, galeri, Google Maps, WhatsApp"},
        {"key": "jumlah_produk_varian", "label": "Jumlah produk/menu/layanan", "help": "Contoh: 5 layanan utama, 20 menu makanan, 30 produk kopi. Ini menentukan UMKM Profesional atau Katalog Produk.", "placeholder": "Contoh: Sekitar 25 menu makanan dan minuman"},
        {"key": "butuh_update_sendiri", "label": "Apakah ingin bisa update konten sendiri?", "help": "Contoh: Tidak perlu, cukup dibantu Zimeira. Atau: Ya, ingin tambah produk/menu sendiri.", "placeholder": "Contoh: Untuk awal tidak perlu CMS, update bisa dibantu Zimeira"},
        {"key": "asset_website", "label": "Asset yang sudah tersedia", "help": "Contoh: logo sudah ada, foto produk ada, teks belum ada, sosial media ada.", "placeholder": "Contoh: Logo ada, foto menu ada, teks profil belum ada"},
        {"key": "referensi_tampilan", "label": "Referensi tampilan", "help": "Contoh: simple elegan, warna coklat kopi, mirip website cafe modern, atau link referensi.", "placeholder": "Contoh: Warna coklat krem, modern, simple, cocok untuk cafe"},
    ],
    "Komputer & Laptop": [
        {"key": "jenis_perangkat", "label": "Jenis perangkat", "help": "Contoh: Laptop Asus X441, PC rakitan, Acer Aspire, Lenovo ThinkPad.", "placeholder": "Contoh: Laptop Asus X441"},
        {"key": "kebutuhan_utama", "label": "Kebutuhan utama", "help": "Contoh: instal ulang Windows, instal aplikasi, laptop lemot, backup data, optimasi performa.", "placeholder": "Contoh: Instal ulang Windows dan driver"},
        {"key": "kondisi_perangkat", "label": "Kondisi/keluhan perangkat", "help": "Contoh: sering lemot, banyak error, tidak bisa masuk Windows, sering blue screen.", "placeholder": "Contoh: Laptop lemot dan sering muncul error saat startup"},
        {"key": "backup_data", "label": "Apakah data perlu dibackup?", "help": "Contoh: Ya, folder kuliah dan foto penting. Atau: Tidak perlu, data boleh dihapus.", "placeholder": "Contoh: Ya, backup folder Documents dan foto"},
        {"key": "aplikasi_dibutuhkan", "label": "Aplikasi yang dibutuhkan", "help": "Contoh: browser, office alternatif, PDF reader, aplikasi kuliah/kerja legal.", "placeholder": "Contoh: Chrome, Office alternatif, PDF reader, aplikasi printer"},
    ],
    "Cleaning / Repasta Laptop-PC": [
        {"key": "jenis_perangkat", "label": "Jenis perangkat", "help": "Contoh: Laptop Asus, PC rakitan, laptop gaming, PC kantor.", "placeholder": "Contoh: Laptop Acer Aspire 5"},
        {"key": "keluhan_suhu", "label": "Keluhan yang dirasakan", "help": "Contoh: laptop panas, kipas berisik, tiba-tiba mati, performa turun.", "placeholder": "Contoh: Laptop cepat panas dan kipas berisik"},
        {"key": "terakhir_dibersihkan", "label": "Terakhir cleaning/repasta kapan?", "help": "Contoh: Belum pernah, 1 tahun lalu, sekitar 6 bulan lalu.", "placeholder": "Contoh: Belum pernah dibersihkan sejak beli"},
        {"key": "penggunaan_harian", "label": "Dipakai untuk apa sehari-hari?", "help": "Contoh: kuliah, kerja, desain, editing, gaming ringan, kasir toko.", "placeholder": "Contoh: Dipakai kuliah, browsing, dan desain Canva"},
    ],
    "Rakit PC Sesuai Budget": [
        {"key": "budget_pc", "label": "Budget khusus rakit PC", "help": "Contoh: Rp4.000.000, Rp6.000.000, Rp8.000.000. Budget hanya untuk kategori ini.", "placeholder": "Contoh: Rp6.000.000"},
        {"key": "kebutuhan_pc", "label": "PC akan dipakai untuk apa?", "help": "Contoh: sekolah, kerja kantor, desain, editing, gaming, streaming, kasir usaha.", "placeholder": "Contoh: Untuk desain ringan, kerja, dan game online ringan"},
        {"key": "perangkat_sudah_ada", "label": "Perangkat yang sudah ada", "help": "Contoh: monitor sudah ada, keyboard belum, mouse ada, speaker belum.", "placeholder": "Contoh: Monitor dan mouse sudah ada, keyboard belum ada"},
        {"key": "preferensi_komponen", "label": "Preferensi komponen jika ada", "help": "Contoh: AMD/Intel bebas, butuh WiFi, SSD 512GB, RAM 16GB.", "placeholder": "Contoh: Bebas AMD/Intel, yang penting RAM 16GB dan SSD 512GB"},
    ],
    "Penggantian Part Laptop-PC": [
        {"key": "jenis_perangkat", "label": "Jenis perangkat", "help": "Contoh: Laptop Asus, PC rakitan, Acer Aspire, Lenovo Ideapad.", "placeholder": "Contoh: Laptop Lenovo Ideapad"},
        {"key": "part_bermasalah", "label": "Part yang ingin diganti", "help": "Contoh: keyboard, baterai, RAM, SSD, HDD, kipas, layar, charger.", "placeholder": "Contoh: Keyboard dan baterai"},
        {"key": "gejala_kerusakan", "label": "Gejala kerusakan", "help": "Contoh: tombol mati, baterai cepat habis, SSD penuh, kipas bunyi.", "placeholder": "Contoh: Beberapa tombol keyboard tidak bisa ditekan"},
        {"key": "part_sudah_ada", "label": "Apakah part sudah ada?", "help": "Contoh: Part sudah ada tinggal pasang. Atau: Belum ada, minta dibantu carikan.", "placeholder": "Contoh: Belum ada, minta dibantu carikan part yang cocok"},
    ],
    "Desain Promosi": [
        {"key": "jenis_desain", "label": "Jenis desain yang dibutuhkan", "help": "Contoh: logo, banner digital, poster promosi, flyer, kartu nama, feed Instagram.", "placeholder": "Contoh: Logo dan poster promosi"},
        {"key": "nama_brand", "label": "Nama brand/usaha/acara", "help": "Contoh: Besemah Coffee, Kopi Sore, Zimeira Tech, Event Lomba Futsal.", "placeholder": "Contoh: Kopi Sore Pagaralam"},
        {"key": "tujuan_desain", "label": "Tujuan desain", "help": "Contoh: promosi grand opening, identitas usaha, poster diskon, banner WhatsApp.", "placeholder": "Contoh: Untuk promosi menu baru di Instagram dan WhatsApp"},
        {"key": "teks_desain", "label": "Teks yang ingin dimasukkan", "help": "Contoh: nama usaha, promo, alamat, kontak, harga, tagline.", "placeholder": "Contoh: Promo Paket Kopi Sore mulai Rp15.000, WA 08xxx"},
        {"key": "warna_referensi", "label": "Warna atau referensi desain", "help": "Contoh: coklat dan krem, minimalis, elegan, modern, kirim link/gambar referensi.", "placeholder": "Contoh: Warna coklat kopi, krem, simple dan premium"},
        {"key": "asset_desain", "label": "Asset yang sudah ada", "help": "Contoh: logo sudah ada, foto produk ada, belum ada foto, ingin dibuat dari nol.", "placeholder": "Contoh: Foto produk ada, logo belum ada"},
    ],
    "Download, Print & Dokumen": [
        {"key": "jenis_layanan_dokumen", "label": "Jenis layanan dokumen", "help": "Contoh: print, scan, jilid, ketik ulang, download file legal.", "placeholder": "Contoh: Print dan jilid tugas"},
        {"key": "detail_file", "label": "Detail file/dokumen", "help": "Contoh: PDF 25 halaman, A4, hitam putih, 1 rangkap, jilid lakban.", "placeholder": "Contoh: PDF 25 halaman, A4, hitam putih, 1 rangkap"},
        {"key": "jenis_cetak", "label": "Jenis cetak/hasil", "help": "Contoh: hitam putih, warna biasa, full gambar, scan PDF, jilid lakban.", "placeholder": "Contoh: Hitam putih A4 + jilid lakban"},
        {"key": "catatan_file_legal", "label": "Catatan file", "help": "Contoh: file tugas kuliah, dokumen pribadi, file legal. Untuk download hanya file legal.", "placeholder": "Contoh: File tugas kuliah dalam format PDF"},
    ],
    "Maintenance Website": [
        {"key": "link_website", "label": "Link website", "help": "Contoh: https://namausaha.com atau https://namausaha.vercel.app", "placeholder": "Contoh: https://kopisore.com"},
        {"key": "jenis_update", "label": "Jenis update/perawatan", "help": "Contoh: update teks, tambah foto, backup, cek error, cek kecepatan, update artikel/produk.", "placeholder": "Contoh: Update foto galeri dan teks menu"},
        {"key": "akses_website", "label": "Akses website yang tersedia", "help": "Contoh: ada akses admin, ada akses hosting, belum ada akses, minta dibantu cek.", "placeholder": "Contoh: Ada akses admin CMS, hosting belum ada"},
        {"key": "jumlah_konten", "label": "Jumlah konten yang ingin diupdate", "help": "Contoh: 5 foto, 2 halaman teks, 10 produk, 1 artikel.", "placeholder": "Contoh: 5 foto galeri dan 3 menu baru"},
    ],
    "Konsultasi Umum": [
        {"key": "kebutuhan_umum", "label": "Kebutuhan utama", "help": "Contoh: ingin tanya jasa yang cocok, bingung pilih paket, ingin konsultasi dulu.", "placeholder": "Contoh: Saya ingin konsultasi layanan yang cocok untuk usaha saya"},
        {"key": "kondisi_saat_ini", "label": "Kondisi saat ini", "help": "Contoh: usaha baru mulai, laptop bermasalah, butuh promosi, belum punya website.", "placeholder": "Contoh: Usaha baru mulai dan belum punya media promosi online"},
        {"key": "hasil_yang_diinginkan", "label": "Hasil yang diinginkan", "help": "Contoh: ingin lebih mudah dapat pelanggan, laptop normal lagi, desain siap posting.", "placeholder": "Contoh: Ingin usaha terlihat lebih profesional dan mudah dihubungi"},
    ],
}

def build_client_data(base_data: dict, category: str, answers: dict) -> str:
    lines = [
        f"Kategori layanan dipilih: {category}",
        f"Nama client/bisnis: {base_data.get('nama', '')}",
        f"Kontak/WA: {base_data.get('kontak', '')}",
        f"Lokasi: {base_data.get('lokasi', '')}",
    ]
    for q in QUESTION_FLOWS.get(category, []):
        lines.append(f"{q['label']}: {answers.get(q['key'], '')}")
    return "\\n".join(lines).strip()
