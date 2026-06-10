from datetime import datetime
from agents.base import save_output
from agents.all_service_agent import all_service_agent
from agents.sales_agent import sales_agent
from agents.brief_agent import brief_agent
from agents.proposal_agent import proposal_agent
from agents.caption_agent import caption_agent
from agents.checklist_agent import checklist_agent
from agents.codex_prompt_agent import codex_prompt_agent
from agents.reviewer_agent import reviewer_agent
from agents.official_proposal_agent import official_proposal_agent
from agents.presentation_outline_agent import presentation_outline_agent
from question_flows import SERVICE_CATEGORIES, QUESTION_FLOWS, build_client_data
from utils.exporter import save_text_markdown_html
from utils.pptx_exporter import create_pptx_from_outline

def choose_category():
    print("\\n=== Pilih Kategori Layanan ===")
    for i, category in enumerate(SERVICE_CATEGORIES, start=1):
        print(f"{i}. {category}")
    try:
        return SERVICE_CATEGORIES[int(input("\\nPilih nomor kategori: ").strip()) - 1]
    except Exception:
        print("Pilihan tidak valid. Menggunakan Konsultasi Umum.")
        return "Konsultasi Umum"

def get_client_input():
    base_data = {
        "nama": input("Nama client/bisnis: ").strip(),
        "kontak": input("Kontak/WA jika ada: ").strip(),
        "lokasi": input("Lokasi: ").strip(),
    }
    category = choose_category()
    answers = {}
    for q in QUESTION_FLOWS.get(category, []):
        print(f"\\n{q['label']}")
        print(f"Contoh jawaban: {q['placeholder']}")
        answers[q["key"]] = input("Jawaban: ").strip()
    return build_client_data(base_data, category, answers)

def run_one(label, filename, func, data, stamp, export_html=False, export_pptx=False):
    result = func(data)
    saved = []
    if export_html:
        saved.extend(save_text_markdown_html(stamp, filename, label, result).values())
    else:
        saved.append(save_output(f"{stamp}_{filename}.txt", result))
    if export_pptx:
        saved.append(create_pptx_from_outline(stamp, filename, result, project_title=label))
    print("\\nFiles:")
    for p in saved:
        print("-", p)
    return result

def main():
    menu = [
        ("Generate Paket Layanan Lengkap", "paket_layanan_lengkap", all_service_agent, False, False),
        ("Sales Agent", "sales", sales_agent, False, False),
        ("Brief Agent", "brief", brief_agent, False, False),
        ("Penawaran/Proposal Agent", "penawaran", proposal_agent, False, False),
        ("Proposal Resmi", "proposal_resmi", official_proposal_agent, True, False),
        ("Presentasi PPTX", "presentasi_zimeira", presentation_outline_agent, True, True),
        ("Caption Agent", "caption", caption_agent, False, False),
        ("Checklist Agent", "checklist", checklist_agent, False, False),
        ("Codex Prompt / Catatan Teknis Agent", "codex_or_teknis", codex_prompt_agent, False, False),
        ("Reviewer Agent", "review", reviewer_agent, False, False),
    ]
    print("=== Zimeira Agent Final Bugfix V2 ===")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item[0]}")
    try:
        selected = menu[int(input("\\nPilih menu: ").strip()) - 1]
    except Exception:
        print("Pilihan tidak valid.")
        return
    data = get_client_input()
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result = run_one(selected[0], selected[1], selected[2], data, stamp, selected[3], selected[4])
    print("\\n=== HASIL ===\\n")
    print(result)

if __name__ == "__main__":
    main()
