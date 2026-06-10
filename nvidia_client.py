import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def _get_secret_value(key: str, default: str = "") -> str:
    """
    Urutan pengambilan config:
    1. Environment variable lokal/server
    2. Streamlit secrets saat deploy online
    3. Default
    """
    value = os.getenv(key)
    if value:
        return value

    try:
        import streamlit as st
        if key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass

    return default

def get_client():
    api_key = _get_secret_value("NVIDIA_API_KEY")
    base_url = _get_secret_value("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")

    if not api_key or api_key.strip() in {"isi_api_key_nvidia_kamu", "isi_api_key_nvidia_kamu_di_sini"}:
        raise RuntimeError(
            "NVIDIA_API_KEY belum diisi. "
            "Jika lokal, isi file .env. "
            "Jika Streamlit Cloud, isi App settings > Secrets."
        )

    return OpenAI(
        base_url=base_url,
        api_key=api_key,
        timeout=180.0,
        max_retries=0,
    )
