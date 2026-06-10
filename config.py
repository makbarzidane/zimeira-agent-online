import os

# Model utama yang stabil untuk logic, kategori layanan, dan aturan katalog.
PRIMARY_MODEL = os.getenv("PRIMARY_MODEL", "nvidia/nemotron-3-nano-30b-a3b")

# Model khusus copywriting untuk proposal, sales, caption, dan narasi presentasi.
COPYWRITER_MODEL = os.getenv("COPYWRITER_MODEL", PRIMARY_MODEL)

# Model khusus arahan desain untuk tone visual, struktur proposal, dan struktur slide.
DESIGN_MODEL = os.getenv("DESIGN_MODEL", COPYWRITER_MODEL)

# Model khusus teknis untuk prompt Codex, planning website, debugging, dan reviewer teknis.
TECHNICAL_MODEL = os.getenv("TECHNICAL_MODEL", PRIMARY_MODEL)

MODELS = {
    # Core / logic
    "all_service": PRIMARY_MODEL,
    "brief": PRIMARY_MODEL,
    "checklist": PRIMARY_MODEL,

    # Copywriting
    "sales": COPYWRITER_MODEL,
    "proposal": COPYWRITER_MODEL,
    "caption": COPYWRITER_MODEL,
    "official_proposal": COPYWRITER_MODEL,
    "presentation": COPYWRITER_MODEL,

    # Design
    "design_director": DESIGN_MODEL,

    # Technical
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
