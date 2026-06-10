# Zimeira Agent Multi-Model Setup V5

Versi ini sudah memakai 4 role model:

## 1. PRIMARY_MODEL
Untuk:
- klasifikasi layanan
- membaca katalog
- menjaga aturan harga
- brief
- checklist
- fallback stabil

Default:
```env
PRIMARY_MODEL=nvidia/nemotron-3-nano-30b-a3b
```

## 2. COPYWRITER_MODEL
Untuk:
- Sales Agent
- Caption Agent
- Penawaran/Proposal Agent
- Proposal Resmi
- Narasi Presentasi

Rekomendasi:
```env
COPYWRITER_MODEL=minimaxai/minimax-m2.7
```

## 3. DESIGN_MODEL
Untuk:
- Design Director Agent
- arahan visual proposal
- struktur slide
- tone presentasi

Rekomendasi awal:
```env
DESIGN_MODEL=minimaxai/minimax-m2.7
```

## 4. TECHNICAL_MODEL
Untuk:
- Codex Prompt Agent
- Reviewer Agent
- planning website
- catatan teknis project

Rekomendasi stabil:
```env
TECHNICAL_MODEL=nvidia/nemotron-3-nano-30b-a3b
```

## Setup yang disarankan

Paling aman:
```env
PRIMARY_MODEL=nvidia/nemotron-3-nano-30b-a3b
COPYWRITER_MODEL=minimaxai/minimax-m2.7
DESIGN_MODEL=minimaxai/minimax-m2.7
TECHNICAL_MODEL=nvidia/nemotron-3-nano-30b-a3b
```

Jika MiniMax timeout, ubah sementara:
```env
COPYWRITER_MODEL=nvidia/nemotron-3-nano-30b-a3b
DESIGN_MODEL=nvidia/nemotron-3-nano-30b-a3b
```

## Test model

Setelah isi `.env`, jalankan:

```powershell
python test_models.py
```

Jika salah satu model timeout atau error, ubah model tersebut di `.env`.
