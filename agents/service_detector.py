def is_website_request(text: str) -> bool:
    t = (text or "").lower()
    keywords = [
        "website", "web", "seo", "landing page", "company profile", "portfolio", "portofolio",
        "katalog produk", "cms", "domain", "hosting", "vercel", "netlify", "toko online",
        "ecommerce", "menu digital", "homestay", "villa", "penginapan", "tour", "travel",
        "sekolah", "kursus", "lembaga", "kedinasan", "pendaftaran", "maintenance website",
        "cafe", "resto", "produk online"
    ]
    return any(k in t for k in keywords)

def detect_general_service(text: str) -> str:
    t = (text or "").lower()
    if is_website_request(text):
        return "Website & SEO"
    if any(k in t for k in ["windows", "install ulang", "driver", "software", "aplikasi", "lemot", "backup data"]):
        return "Komputer & Laptop"
    if any(k in t for k in ["cleaning", "repasta", "panas", "overheat", "kipas", "debu"]):
        return "Cleaning / Repasta Laptop-PC"
    if any(k in t for k in ["rakit pc", "pc budget", "build pc"]):
        return "Rakit PC Sesuai Budget"
    if any(k in t for k in ["ram", "ssd", "storage", "ganti part", "keyboard", "baterai", "layar"]):
        return "Penggantian Part Laptop-PC"
    if any(k in t for k in ["print", "cetak", "scan", "jilid", "ketik", "download"]):
        return "Download, Print & Dokumen"
    if any(k in t for k in ["logo", "banner", "poster", "flyer", "feed instagram", "desain"]):
        return "Desain Promosi"
    return "Konsultasi Umum"
