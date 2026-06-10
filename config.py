import os

def _get_config(key: str, default: str = "") -> str:
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

PRIMARY_MODEL = _get_config("PRIMARY_MODEL", "nvidia/nemotron-3-nano-30b-a3b")
COPYWRITER_MODEL = _get_config("COPYWRITER_MODEL", PRIMARY_MODEL)
DESIGN_MODEL = _get_config("DESIGN_MODEL", COPYWRITER_MODEL)
TECHNICAL_MODEL = _get_config("TECHNICAL_MODEL", PRIMARY_MODEL)

MODELS = {
    "all_service": PRIMARY_MODEL,
    "brief": PRIMARY_MODEL,
    "checklist": PRIMARY_MODEL,

    "sales": COPYWRITER_MODEL,
    "proposal": COPYWRITER_MODEL,
    "caption": COPYWRITER_MODEL,
    "official_proposal": COPYWRITER_MODEL,
    "presentation": COPYWRITER_MODEL,

    "design_director": DESIGN_MODEL,

    "codex_prompt": TECHNICAL_MODEL,
    "reviewer": TECHNICAL_MODEL,
}

TEMPERATURES = {
    "all_service": 0.25,
    "brief": 0.20,
    "checklist": 0.20,

    "sales": 0.45,
    "proposal": 0.35,
    "caption": 0.70,
    "official_proposal": 0.32,
    "presentation": 0.34,

    "design_director": 0.35,

    "codex_prompt": 0.20,
    "reviewer": 0.20,
}

MAX_TOKENS = {
    "all_service": 2600,
    "brief": 1000,
    "checklist": 1000,

    "sales": 1100,
    "proposal": 1500,
    "caption": 1000,
    "official_proposal": 3200,
    "presentation": 2800,

    "design_director": 1100,

    "codex_prompt": 1500,
    "reviewer": 1100,
}

MODEL_ROLE_DESCRIPTION = {
    "PRIMARY_MODEL": "Logic, klasifikasi layanan, aturan katalog, fallback stabil.",
    "COPYWRITER_MODEL": "Proposal, sales, caption, dan narasi presentasi.",
    "DESIGN_MODEL": "Arahan visual, struktur desain proposal, dan struktur slide.",
    "TECHNICAL_MODEL": "Prompt Codex, planning website, debugging, dan reviewer teknis.",
}
