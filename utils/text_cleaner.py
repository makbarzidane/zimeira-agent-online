import re

def ensure_text(value, default="Belum ada output."):
    if value is None:
        return default
    if isinstance(value, str):
        return value.strip() or default
    return str(value).strip() or default

def clean_ai_text(text: str) -> str:
    """
    Membersihkan artefak markdown dari output model:
    - ###, ##, #
    - **bold**
    - bullet kosong seperti "-" atau "•"
    - code fence
    - spasi berlebihan
    """
    text = ensure_text(text, "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # remove code fences but keep content
    text = re.sub(r"```[a-zA-Z0-9_-]*", "", text)
    text = text.replace("```", "")

    cleaned_lines = []
    for line in text.splitlines():
        s = line.strip()

        # skip empty markdown bullets/dots
        if s in {"-", "•", "*", "–", "—", ".", "·"}:
            continue

        # remove markdown heading prefix
        s = re.sub(r"^\s*#{1,6}\s*", "", s)

        # remove bold/italic markdown markers
        s = s.replace("**", "")
        s = s.replace("__", "")
        # Remove single * only when used as wrapper before words, but keep multiplication-like content
        s = re.sub(r"^\*+", "", s)
        s = re.sub(r"\*+$", "", s)

        # normalize excessive whitespace
        s = re.sub(r"[ \t]+", " ", s).strip()

        cleaned_lines.append(s)

    # collapse more than 2 blank lines
    out = "\n".join(cleaned_lines)
    out = re.sub(r"\n{3,}", "\n\n", out).strip()
    return out

def clean_heading(text: str) -> str:
    text = clean_ai_text(text)
    text = re.sub(r"^\d+[\.\)]\s*", "", text).strip()
    return text

def is_noise_line(line: str) -> bool:
    s = clean_ai_text(line).strip()
    return not s or s in {"-", "•", "*", "–", "—", ".", "·"}
