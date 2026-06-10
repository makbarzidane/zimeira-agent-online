# Zimeira Agent Final Design V3

Versi ini memperbaiki kualitas desain output:

## Yang berubah
1. Proposal HTML sekarang punya:
   - cover page
   - brand Zimeira Tech
   - meta card
   - section-card rapi
   - style print-friendly untuk Save as PDF

2. Presentasi PPTX sekarang punya:
   - title slide lebih profesional
   - kartu poin 2 kolom
   - warna terang + aksen hijau Zimeira
   - closing slide
   - narasi presenter

3. Ditambahkan Design Director Agent:
   - memberi arahan gaya visual
   - membantu proposal/presentasi lebih sesuai data client

4. Ditambahkan opsi DESIGN_MODEL di `.env`:
   - default tetap stabil memakai Nemotron Nano
   - kalau nanti ada model lain yang cocok untuk copy/design direction, isi `DESIGN_MODEL`

## Cara pakai
Gunakan sebagai project baru:

```powershell
cd E:\my-agent\zimeira-agent-final-design-v3
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app_streamlit.py
```

Pilih:
- `Proposal Resmi` untuk proposal HTML/PDF
- `Presentasi PPTX` untuk file PowerPoint
