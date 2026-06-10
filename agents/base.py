from pathlib import Path
from nvidia_client import get_client
from config import MODELS, TEMPERATURES, MAX_TOKENS
from agents.service_detector import is_website_request
from agents.local_fallback import ensure_text, local_output

client = get_client()

def load_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")

def load_general_knowledge() -> str:
    return load_file("knowledge/general_services.txt")

def load_website_catalog() -> str:
    return load_file("knowledge/website_catalog.txt")

def build_knowledge_for_request(client_data: str) -> str:
    general = load_general_knowledge()
    website = load_website_catalog()
    if is_website_request(client_data):
        return f"KATALOG UMUM ZIMEIRA:\\n{general}\\n\\nKATALOG WEBSITE FINAL - WAJIB DIPAKAI UNTUK WEBSITE:\\n{website}"
    return f"KATALOG UMUM ZIMEIRA:\\n{general}\\n\\nKATALOG WEBSITE FINAL - HANYA DIPAKAI JIKA KEBUTUHAN WEBSITE:\\n{website}"

def save_output(filename: str, content: str) -> str:
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    path = output_dir / filename
    path.write_text(ensure_text(content), encoding="utf-8")
    return str(path)

def _extract_response_text(response) -> str:
    try:
        if not response or not getattr(response, "choices", None):
            return ""
        msg = response.choices[0].message
        content = getattr(msg, "content", "")
        return ensure_text(content, default="")
    except Exception:
        return ""

def ask_agent(agent_name: str, system_prompt: str, user_prompt: str) -> str:
    model = MODELS.get(agent_name, MODELS.get("all_service"))
    temperature = TEMPERATURES.get(agent_name, 0.25)
    max_tokens = MAX_TOKENS.get(agent_name, 1000)

    system_prompt = ensure_text(system_prompt, "")
    user_prompt = ensure_text(user_prompt, "")

    try:
        print(f"Using model for {agent_name}: {model}")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        text = _extract_response_text(response)
        if not text:
            return local_output(agent_name, user_prompt)
        return text
    except Exception as e:
        error_text = f"{type(e).__name__}: {str(e)}"
        print(f"API error on {agent_name}: {error_text}")
        return f"API ERROR pada agent '{agent_name}'.\\nModel: {model}\\nDetail: {error_text}\\n\\n{local_output(agent_name, user_prompt)}"
