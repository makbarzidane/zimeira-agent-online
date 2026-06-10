from pathlib import Path
import html
import re
from utils.text_cleaner import ensure_text, clean_ai_text, clean_heading, is_noise_line

def safe_filename(text: str) -> str:
    text = ensure_text(text, "output").strip().lower()
    text = re.sub(r"[^a-z0-9A-Z_\- ]+", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:60] or "output"

def _is_section_heading(line: str) -> bool:
    s = clean_ai_text(line).strip()
    if not s:
        return False

    # 1. JUDUL PROPOSAL / 1) JUDUL PROPOSAL
    if re.match(r"^\d+[\.\)]\s+[A-Za-zÀ-ÿ0-9]", s):
        return True

    # uppercase short headings
    if s.isupper() and 5 <= len(s) <= 90:
        return True

    return False

def _parse_sections(content: str):
    content = clean_ai_text(content)
    lines = content.splitlines()

    sections = []
    current_title = None
    current_body = []

    for line in lines:
        if is_noise_line(line):
            continue

        clean = clean_ai_text(line).strip()

        if _is_section_heading(clean):
            if current_title or current_body:
                sections.append((current_title or "Proposal", "\n".join(current_body).strip()))
            current_title = clean_heading(clean)
            current_body = []
        else:
            current_body.append(clean)

    if current_title or current_body:
        sections.append((current_title or "Proposal", "\n".join(current_body).strip()))

    # remove duplicated empty / tiny proposal section if caused by title
    normalized = []
    for title, body in sections:
        title = clean_heading(title)
        body = clean_ai_text(body)
        if not body and title.lower() in {"proposal", "judul proposal"}:
            continue
        normalized.append((title, body))

    return normalized or [("Proposal", content)]

def _format_body(text: str):
    text = clean_ai_text(text)
    parts = []
    in_ul = False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            parts.append("</ul>")
            in_ul = False

    for line in text.splitlines():
        s = clean_ai_text(line).strip()
        if not s or s in {"-", "•", "*"}:
            continue

        # bullet with content
        if re.match(r"^[-•]\s+\S+", s):
            if not in_ul:
                parts.append("<ul>")
                in_ul = True
            item = re.sub(r"^[-•]\s+", "", s).strip()
            parts.append(f"<li>{html.escape(item)}</li>")
            continue

        close_ul()

        # label-value line
        if ":" in s and len(s.split(":", 1)[0]) <= 35:
            label, value = s.split(":", 1)
            parts.append(f"<p><strong>{html.escape(label.strip())}:</strong>{html.escape(value.strip())}</p>")
        else:
            parts.append(f"<p>{html.escape(s)}</p>")

    close_ul()
    return "\n".join(parts)

def save_text_markdown_html(stamp: str, filename: str, title: str, content) -> dict:
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    content = clean_ai_text(content)
    title = clean_ai_text(title or "Zimeira Tech")

    base = f"{stamp}_{safe_filename(filename)}"
    txt_path = output_dir / f"{base}.txt"
    md_path = output_dir / f"{base}.md"
    html_path = output_dir / f"{base}.html"

    txt_path.write_text(content, encoding="utf-8")
    md_path.write_text(content, encoding="utf-8")

    sections = _parse_sections(content)
    first_title = sections[0][1].splitlines()[0] if sections and sections[0][0].upper().startswith("JUDUL") and sections[0][1] else sections[0][0]
    first_title = clean_ai_text(first_title)

    cards = ""
    for idx, (sec_title, sec_body) in enumerate(sections, start=1):
        if not clean_ai_text(sec_body) and sec_title.lower() in {"proposal", "judul proposal"}:
            continue
        cards += f"""
        <section class="section-card">
          <div class="section-number">{idx:02d}</div>
          <div class="section-content">
            <h2>{html.escape(clean_heading(sec_title))}</h2>
            {_format_body(sec_body)}
          </div>
        </section>
        """

    html_content = f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
    :root {{
        --dark: #07111F;
        --card: #FFFFFF;
        --soft: #F4F7FB;
        --green: #00A676;
        --mint: #10B981;
        --blue: #38BDF8;
        --text: #0F172A;
        --muted: #64748B;
        --line: #E2E8F0;
    }}
    * {{ box-sizing: border-box; }}
    body {{
        margin: 0;
        background: var(--soft);
        color: var(--text);
        font-family: Arial, Helvetica, sans-serif;
        line-height: 1.65;
    }}
    .cover {{
        background:
          radial-gradient(circle at 12% 5%, rgba(0,166,118,.30), transparent 28%),
          linear-gradient(135deg, #07111F, #0F172A);
        color: white;
        padding: 54px 64px 48px;
        border-radius: 0 0 34px 34px;
    }}
    .brand-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 70px;
    }}
    .logo {{
        display: inline-flex;
        align-items: center;
        gap: 12px;
        font-weight: 800;
        letter-spacing: -0.02em;
    }}
    .logo-mark {{
        width: 46px;
        height: 46px;
        border-radius: 14px;
        background: linear-gradient(135deg, var(--green), var(--blue));
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
    }}
    .doc-label {{
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,.10);
        border: 1px solid rgba(255,255,255,.18);
        color: #D1FAE5;
        font-size: 13px;
        font-weight: 700;
    }}
    .cover h1 {{
        max-width: 820px;
        margin: 0;
        font-size: 42px;
        line-height: 1.12;
        letter-spacing: -0.04em;
    }}
    .cover p {{
        max-width: 740px;
        color: #CBD5E1;
        margin: 18px 0 0;
        font-size: 16px;
    }}
    .meta-strip {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        max-width: 980px;
        margin: -34px auto 34px;
        padding: 0 18px;
    }}
    .meta-card {{
        background: white;
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 14px 38px rgba(15,23,42,.08);
    }}
    .meta-label {{
        font-size: 12px;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: .08em;
        font-weight: 700;
        margin-bottom: 6px;
    }}
    .meta-value {{
        font-weight: 800;
        color: var(--text);
    }}
    .page {{
        max-width: 980px;
        margin: 0 auto 50px;
        padding: 0 18px;
    }}
    .section-card {{
        display: grid;
        grid-template-columns: 72px 1fr;
        gap: 20px;
        background: white;
        border: 1px solid var(--line);
        border-radius: 22px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 10px 28px rgba(15,23,42,.055);
        break-inside: avoid;
    }}
    .section-number {{
        width: 54px;
        height: 54px;
        border-radius: 18px;
        background: rgba(0,166,118,.10);
        border: 1px solid rgba(0,166,118,.18);
        color: var(--green);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
    }}
    h2 {{
        margin: 0 0 12px;
        font-size: 22px;
        letter-spacing: -0.02em;
        color: var(--dark);
    }}
    p {{
        margin: 0 0 10px;
        color: #334155;
        font-size: 15px;
    }}
    ul {{
        margin: 8px 0 12px;
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 7px;
        color: #334155;
        font-size: 15px;
    }}
    .footer {{
        max-width: 980px;
        margin: 24px auto 40px;
        padding: 0 18px;
        color: var(--muted);
        font-size: 12px;
        display: flex;
        justify-content: space-between;
    }}
    @media print {{
        body {{ background: white; }}
        .cover {{ border-radius: 0; padding: 42px 48px; }}
        .cover h1 {{ font-size: 34px; }}
        .meta-strip {{ margin-top: 22px; }}
        .section-card {{ box-shadow: none; }}
    }}
</style>
</head>
<body>
    <div class="cover">
        <div class="brand-row">
            <div class="logo"><div class="logo-mark">ZT</div><div>Zimeira Tech</div></div>
            <div class="doc-label">Proposal Resmi</div>
        </div>
        <h1>{html.escape(first_title)}</h1>
        <p>Dokumen penawaran layanan yang disusun berdasarkan kebutuhan calon pelanggan dan katalog layanan Zimeira Tech.</p>
    </div>

    <div class="meta-strip">
        <div class="meta-card"><div class="meta-label">Penyedia</div><div class="meta-value">Zimeira Tech</div></div>
        <div class="meta-card"><div class="meta-label">Dokumen</div><div class="meta-value">{html.escape(title)}</div></div>
        <div class="meta-card"><div class="meta-label">Status</div><div class="meta-value">Siap Review</div></div>
    </div>

    <main class="page">
        {cards}
    </main>

    <div class="footer">
        <div>Zimeira Tech - Solusi teknologi, desain, dan website usaha</div>
        <div>Generated by Zimeira Agent</div>
    </div>
</body>
</html>
"""
    html_path.write_text(html_content, encoding="utf-8")
    return {"txt": str(txt_path), "md": str(md_path), "html": str(html_path)}
