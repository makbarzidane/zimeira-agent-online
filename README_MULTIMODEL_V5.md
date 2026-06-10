# Zimeira Agent Multi-Model V5

Versi ini merealisasikan multi-model setup:

- PRIMARY_MODEL untuk logic dan katalog
- COPYWRITER_MODEL untuk copywriting proposal, sales, caption, dan narasi presentasi
- DESIGN_MODEL untuk arahan visual proposal/presentasi
- TECHNICAL_MODEL untuk prompt Codex dan reviewer teknis

## Cara install sebagai project baru

```powershell
cd E:\my-agent
```

Ekstrak folder ini menjadi:

```text
E:\my-agent\zimeira-agent-multimodel-v5
```

Lalu jalankan:

```powershell
cd E:\my-agent\zimeira-agent-multimodel-v5
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
copy .env.example .env
notepad .env
```

Isi `NVIDIA_API_KEY`, lalu test:

```powershell
python test_models.py
```

Jika aman, jalankan dashboard:

```powershell
python -m streamlit run app_streamlit.py
```

## Rekomendasi awal `.env`

```env
NVIDIA_API_KEY=isi_api_key_nvidia_kamu
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1

PRIMARY_MODEL=nvidia/nemotron-3-nano-30b-a3b
COPYWRITER_MODEL=minimaxai/minimax-m2.7
DESIGN_MODEL=minimaxai/minimax-m2.7
TECHNICAL_MODEL=nvidia/nemotron-3-nano-30b-a3b
```

## Catatan

Kalau MiniMax timeout, jangan panik. Ubah dulu:

```env
COPYWRITER_MODEL=nvidia/nemotron-3-nano-30b-a3b
DESIGN_MODEL=nvidia/nemotron-3-nano-30b-a3b
```

Setelah stabil, baru coba model copywriting lagi.
