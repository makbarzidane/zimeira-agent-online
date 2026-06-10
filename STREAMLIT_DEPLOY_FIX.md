# Streamlit Deploy Fix - NVIDIA_API_KEY belum diisi

Error:
```text
RuntimeError: NVIDIA_API_KEY belum diisi
```

Penyebab:
Di Streamlit Cloud, file `.env` tidak ikut dipakai. API key harus dimasukkan lewat:
`App settings > Secrets`.

## Isi Secrets Streamlit

Masuk ke Streamlit Cloud:
`Manage app > Settings > Secrets`

Isi:

```toml
NVIDIA_API_KEY = "isi_api_key_nvidia_kamu"
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"

PRIMARY_MODEL = "nvidia/nemotron-3-nano-30b-a3b"
COPYWRITER_MODEL = "meta/llama-3.1-8b-instruct"
DESIGN_MODEL = "meta/llama-3.1-8b-instruct"
TECHNICAL_MODEL = "nvidia/nemotron-3-nano-30b-a3b"
```

Lalu klik Save dan Reboot/Rerun app.
