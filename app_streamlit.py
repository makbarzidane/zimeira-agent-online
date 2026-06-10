import streamlit as st
from datetime import datetime
from pathlib import Path

from config import PRIMARY_MODEL, COPYWRITER_MODEL, DESIGN_MODEL, TECHNICAL_MODEL, MODEL_ROLE_DESCRIPTION

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
from agent_guide import AGENT_GUIDE
from utils.exporter import save_text_markdown_html, ensure_text
from utils.text_cleaner import clean_ai_text
from utils.pptx_exporter import create_pptx_from_outline

st.set_page_config(page_title="Zimeira Admin Panel", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")

CSS = """
<style>
.stApp { background: radial-gradient(circle at 8% 0%, rgba(0,166,118,.20), transparent 26%), radial-gradient(circle at 92% 4%, rgba(56,189,248,.12), transparent 25%), linear-gradient(135deg, #06101D 0%, #08111F 45%, #0B1220 100%); }
.block-container { max-width:100% !important; padding:4.2rem 2.2rem 3rem !important; }
[data-testid="stSidebar"] { background:linear-gradient(180deg,#06101D 0%,#0F172A 100%); border-right:1px solid rgba(255,255,255,.08); }
[data-testid="stSidebar"] * { color:#E5E7EB; }
#MainMenu, footer { visibility:hidden; }
.z-hero { border-radius:28px; padding:32px 36px; background:linear-gradient(135deg,rgba(0,166,118,.20),rgba(56,189,248,.07) 45%,rgba(15,23,42,.94)); border:1px solid rgba(255,255,255,.12); box-shadow:0 22px 70px rgba(0,0,0,.30); margin-bottom:20px; }
.z-kicker { display:inline-flex; padding:8px 13px; border-radius:999px; background:rgba(0,166,118,.14); border:1px solid rgba(110,231,183,.22); color:#6EE7B7; font-weight:850; font-size:13px; }
.z-title { margin-top:18px; font-size:42px; line-height:1.08; letter-spacing:-.045em; font-weight:950; color:#F8FAFC; }
.z-gradient { background:linear-gradient(90deg,#6EE7B7,#38BDF8); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.z-subtitle { margin-top:14px; color:#CBD5E1; font-size:16px; line-height:1.65; max-width:980px; }
.z-card { background:rgba(15,23,42,.78); border:1px solid rgba(255,255,255,.10); border-radius:22px; padding:20px; box-shadow:0 16px 48px rgba(0,0,0,.22); margin-bottom:16px; }
.z-card-title { color:#F8FAFC; font-size:18px; font-weight:900; letter-spacing:-.02em; margin-bottom:6px; }
.z-card-desc { color:#94A3B8; font-size:14px; line-height:1.55; }
.z-badge { display:inline-flex; align-items:center; padding:7px 11px; border-radius:999px; background:rgba(0,166,118,.13); border:1px solid rgba(110,231,183,.20); color:#6EE7B7; font-size:13px; font-weight:850; }
.z-badge-blue { background:rgba(56,189,248,.12); border-color:rgba(125,211,252,.18); color:#7DD3FC; }
.z-question-card { background:rgba(15,23,42,.72); border:1px solid rgba(255,255,255,.10); border-radius:20px; padding:16px; margin-bottom:10px; }
.z-output { background:linear-gradient(145deg,rgba(0,166,118,.10),rgba(15,23,42,.84)); border:1px solid rgba(110,231,183,.16); border-radius:26px; padding:22px; box-shadow:0 22px 65px rgba(0,0,0,.28); margin-top:20px; }
.stTextInput > div > div > input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div { background:rgba(2,6,23,.56) !important; color:#F8FAFC !important; border:1px solid rgba(255,255,255,.13) !important; border-radius:16px !important; }
.stTextInput label, .stTextArea label, .stSelectbox label { color:#E5E7EB !important; font-weight:800 !important; }
.stButton > button { width:100%; border:0 !important; border-radius:18px !important; padding:.9rem 1.2rem !important; background:linear-gradient(135deg,#00A676,#10B981) !important; color:white !important; font-weight:950 !important; box-shadow:0 16px 36px rgba(16,185,129,.24) !important; }
[data-testid="stExpander"] { border-radius:18px !important; background:rgba(15,23,42,.58) !important; border:1px solid rgba(255,255,255,.10) !important; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

SERVICE_ICONS = {
    "Website & SEO": "🌐", "Komputer & Laptop": "💻", "Cleaning / Repasta Laptop-PC": "🧰",
    "Rakit PC Sesuai Budget": "🖥️", "Penggantian Part Laptop-PC": "🔧", "Desain Promosi": "🎨",
    "Download, Print & Dokumen": "🖨️", "Maintenance Website": "🛠️", "Konsultasi Umum": "💬",
}
SERVICE_SHORT = {
    "Website & SEO": "Website custom, katalog, SEO, dan maintenance",
    "Komputer & Laptop": "Instal Windows, aplikasi, backup, dan optimasi",
    "Cleaning / Repasta Laptop-PC": "Perawatan suhu, debu, dan performa perangkat",
    "Rakit PC Sesuai Budget": "Rekomendasi part dan jasa perakitan PC",
    "Penggantian Part Laptop-PC": "RAM, SSD, keyboard, baterai, kipas, dan part lain",
    "Desain Promosi": "Logo, banner, poster, flyer, kartu nama, dan feed",
    "Download, Print & Dokumen": "Print, scan, jilid, ketik, dan download file legal",
    "Maintenance Website": "Update konten, backup, cek error, dan perawatan website",
    "Konsultasi Umum": "Bantu menentukan layanan yang paling sesuai",
}
agent_map = {
    "Generate Paket Layanan Lengkap": ("paket_layanan_lengkap", all_service_agent, False, False),
    "Sales Agent": ("sales", sales_agent, False, False),
    "Brief Agent": ("brief", brief_agent, False, False),
    "Penawaran/Proposal Agent": ("penawaran", proposal_agent, False, False),
    "Proposal Resmi": ("proposal_resmi", official_proposal_agent, True, False),
    "Presentasi PPTX": ("presentasi_zimeira", presentation_outline_agent, True, True),
    "Caption Agent": ("caption", caption_agent, False, False),
    "Checklist Agent": ("checklist", checklist_agent, False, False),
    "Codex Prompt / Catatan Teknis Agent": ("codex_or_teknis", codex_prompt_agent, False, False),
    "Reviewer Agent": ("review", reviewer_agent, False, False),
}

with st.sidebar:
    st.markdown("## ⚡ Zimeira Tech")
    st.caption("Panel internal untuk output kerja.")

    with st.expander("Model aktif", expanded=False):
        st.markdown(f"**PRIMARY**  \\n`{PRIMARY_MODEL}`")
        st.caption(MODEL_ROLE_DESCRIPTION.get("PRIMARY_MODEL", ""))

        st.markdown(f"**COPYWRITER**  \\n`{COPYWRITER_MODEL}`")
        st.caption(MODEL_ROLE_DESCRIPTION.get("COPYWRITER_MODEL", ""))

        st.markdown(f"**DESIGN**  \\n`{DESIGN_MODEL}`")
        st.caption(MODEL_ROLE_DESCRIPTION.get("DESIGN_MODEL", ""))

        st.markdown(f"**TECHNICAL**  \\n`{TECHNICAL_MODEL}`")
        st.caption(MODEL_ROLE_DESCRIPTION.get("TECHNICAL_MODEL", ""))

    menu = st.selectbox("Pilih output yang ingin dibuat", list(agent_map.keys()), index=0)

    guide = AGENT_GUIDE.get(menu, {})
    st.markdown(
        f"""
        <div class='z-card'>
            <div class='z-card-title'>Fungsi agent</div>
            <div class='z-card-desc'>{guide.get('fungsi','')}</div>
        </div>
        <div class='z-card'>
            <div class='z-card-title'>Data yang dibutuhkan</div>
            <div class='z-card-desc'>{guide.get('butuh_data','')}</div>
        </div>
        <div class='z-card'>
            <div class='z-card-title'>Hasil output</div>
            <div class='z-card-desc'>{guide.get('hasil','')}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("""<div class="z-hero"><div class="z-kicker">⚡ Panel Internal Zimeira Tech</div>
<div class="z-title">Buat output kerja berdasarkan <span class="z-gradient">data yang benar-benar diisi</span>.</div>
<div class="z-subtitle">Dashboard ini memproses data calon pelanggan menjadi balasan, brief, penawaran, proposal resmi, presentasi PPTX, checklist, caption, atau prompt teknis. Setiap agent punya kebutuhan data yang berbeda dan output disesuaikan dengan kategori layanan yang dipilih.</div></div>""", unsafe_allow_html=True)

left, right = st.columns([0.88, 1.12], gap="large")
with left:
    st.markdown("<div class='z-card'><div class='z-card-title'>Data calon pelanggan</div><div class='z-card-desc'>Isi data yang kamu terima dari chat, telepon, atau form pemesanan.</div></div>", unsafe_allow_html=True)
    nama = st.text_input("Nama pelanggan / usaha", placeholder="Contoh: Zimeira")
    kontak = st.text_input("Nomor WhatsApp jika ada", placeholder="Contoh: 08xxxxxxxxxx")
    lokasi = st.text_input("Lokasi pelanggan", placeholder="Contoh: Pagaralam, Sumatera Selatan")
    st.markdown("<div class='z-card'><div class='z-card-title'>Kategori layanan</div><div class='z-card-desc'>Pilih kategori. Pertanyaan akan berubah sesuai pilihan.</div></div>", unsafe_allow_html=True)
    category = st.selectbox("Pilih kategori layanan", SERVICE_CATEGORIES, index=0)
    st.markdown(f"<div class='z-card' style='border-color: rgba(110,231,183,.18);'><div class='z-badge'>{SERVICE_ICONS.get(category,'✨')} {category}</div><div class='z-card-desc' style='margin-top:12px;'>{SERVICE_SHORT.get(category,'Layanan Zimeira Tech')}</div></div>", unsafe_allow_html=True)
with right:
    st.markdown("<div class='z-card'><div class='z-card-title'>Pertanyaan sesuai layanan</div><div class='z-card-desc'>Isi berdasarkan informasi dari pelanggan. Output agent akan mengikuti data ini.</div></div>", unsafe_allow_html=True)
    answers = {}
    for idx, q in enumerate(QUESTION_FLOWS.get(category, []), start=1):
        st.markdown(f"<div class='z-question-card'><span class='z-badge z-badge-blue'>Pertanyaan {idx}</span><div class='z-card-title' style='font-size:16px; margin-top:10px;'>{q['label']}</div><div class='z-card-desc'>{q['help']}</div></div>", unsafe_allow_html=True)
        answers[q["key"]] = st.text_area(q["label"], placeholder=q["placeholder"], label_visibility="collapsed", height=88)

data = build_client_data({"nama": nama, "kontak": kontak, "lokasi": lokasi}, category, answers)
st.markdown("<div class='z-card'><div class='z-card-title'>Cek data & buat output</div><div class='z-card-desc'>Proposal Resmi membuat HTML. Presentasi PPTX membuat file PowerPoint. Semua hasil tersimpan di folder output.</div></div>", unsafe_allow_html=True)
preview_col, action_col = st.columns([1.3, 0.7], gap="large")
with preview_col:
    with st.expander("Lihat data yang akan diproses", expanded=True):
        st.code(data, language="text")
with action_col:
    st.markdown(f"<div class='z-card'><div class='z-card-title'>Output yang dibuat</div><div class='z-badge'>{menu}</div><div class='z-card-desc' style='margin-top:12px;'>{guide.get('hasil','')}</div></div>", unsafe_allow_html=True)
    generate_clicked = st.button("Buat Output")

def make_download_button(path):
    p = Path(path)
    if not p.exists():
        return
    with open(p, "rb") as f:
        st.download_button(label=f"Download {p.name}", data=f.read(), file_name=p.name, mime="application/octet-stream")

if generate_clicked:
    filename, func, export_html, export_pptx = agent_map[menu]
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    progress = st.progress(0)
    status = st.empty()
    with st.spinner("Memproses data calon pelanggan..."):
        status.info("Membaca data...")
        progress.progress(20)
        status.info("Membuat output sesuai agent...")
        progress.progress(60)
        result = clean_ai_text(ensure_text(func(data)))
        progress.progress(82)
        saved = []
        if export_html:
            paths = save_text_markdown_html(stamp, filename, menu, result)
            saved.extend(paths.values())
        else:
            saved.append(save_output(f"{stamp}_{filename}.txt", result))
        if export_pptx:
            saved.append(create_pptx_from_outline(stamp, filename, result, project_title=menu))
        progress.progress(100)
    status.success("Output berhasil dibuat.")
    st.markdown("<div class='z-output'><div class='z-card-title'>Output berhasil dibuat</div><div class='z-card-desc'>File tersimpan di folder output.</div></div>", unsafe_allow_html=True)
    tab_result, tab_files, tab_client, tab_next = st.tabs(["Hasil", "File", "Data yang diproses", "Langkah berikutnya"])
    with tab_result:
        st.markdown(result)
    with tab_files:
        for path in saved:
            st.code(path, language="text")
            make_download_button(path)
    with tab_client:
        st.code(data, language="text")
    with tab_next:
        st.markdown("""
        ### Langkah berikutnya
        1. Cek ulang hasil sebelum dikirim ke client.
        2. Untuk proposal resmi, buka file `.html` lalu print/save as PDF.
        3. Untuk presentasi, buka file `.pptx` di PowerPoint/WPS/LibreOffice.
        4. Jika ingin desain lanjut di Canva, upload file `.pptx` ke Canva.
        5. Jika layanan website, gunakan prompt teknis untuk Codex.
        """)
