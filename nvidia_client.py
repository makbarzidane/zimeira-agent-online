import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_client() -> OpenAI:
    api_key = os.getenv("NVIDIA_API_KEY")
    base_url = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")

    if not api_key:
        raise RuntimeError("NVIDIA_API_KEY belum diisi. Copy .env.example menjadi .env lalu isi API key.")

    return OpenAI(
        base_url=base_url,
        api_key=api_key,
        timeout=180.0,
        max_retries=0,
    )
