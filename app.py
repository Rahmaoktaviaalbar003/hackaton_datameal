import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
mode = st.sidebar.selectbox("Pilih Tampilan:", ["Mockup/Demo", "Aplikasi Asli"])

if mode == "Mockup/Demo":
    st.set_page_config(layout="wide", page_title="Mockup MBG SENTRA")
    
    # Header Mockup
    st.title("🥘 Mockup Dashboard MBG SENTRA")
    st.info("💡 Anda sedang berada di mode **Preview/Mockup**. Pindah ke 'Aplikasi Asli' di sidebar untuk sistem real-time.")
    
    # Baris pertama: Metric
    m1, m2, m3 = st.columns(3)
    m1.metric("Target Penerima", "45.2 Juta Siswa", "Nasional")
    m2.metric("Anggaran Terkelola", "Rp 12.5 Triliun", "Stabil")
    m3.metric("Skor Transparansi", "98%", "A+")
    
    # Baris kedua: Tabel Dummy & Grafik Simpel
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("📍 Realisasi per Wilayah (Dummy)")
        mock_data = pd.DataFrame({
            "Wilayah": ["Bengkulu", "DKI Jakarta", "Jawa Barat", "Jawa Timur"],
            "Realisasi (%)": [91.0, 85.2, 78.9, 80.1],
            "Status": ["Optimal", "Optimal", "Waspada", "Waspada"]
        })
        st.table(mock_data)
    
    with col_b:
        st.subheader("📊 Komposisi Gizi")
        gizi_data = pd.DataFrame([30, 40, 20, 10], index=["Karbo", "Protein", "Vitamin", "Susu"])
        st.bar_chart(gizi_data)

    st.warning("⚠️ Untuk melihat Dashboard Monitoring Nasional yang lengkap dengan fitur Anomali, silakan pilih 'Aplikasi Asli' pada menu di samping kiri.")
    
    st.stop()
import random
# Pustaka Pillow untuk memproses gambar
from PIL import Image
st.set_page_config(layout="wide", page_title="Dashboard Monitoring Nasional")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #F8FAFC;
    }

    /* Styling Judul */
    h1 {
        font-weight: 700 !important;
        color: #1E293B !important;
        letter-spacing: -0.02em;
    }
    
    /* Styling Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #0F172A !important;
    }

    /* Garis pemisah */
    hr {
        margin-top: 0.5rem;
        margin-bottom: 2rem;
        border: 0;
        border-top: 1px solid #E2E8F0;
    }

    /* Menghilangkan menu Streamlit agar terlihat seperti aplikasi mandiri */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
df = pd.DataFrame([
    {"Wilayah": "DKI Jakarta", "Target": 150000, "Realisasi": 85.2, "Status": "Optimal"},
    {"Wilayah": "Jawa Barat", "Target": 220000, "Realisasi": 78.9, "Status": "Waspada"},
    {"Wilayah": "Jawa Tengah", "Target": 185000, "Realisasi": 82.5, "Status": "Optimal"},
    {"Wilayah": "Jawa Timur", "Target": 210000, "Realisasi": 80.1, "Status": "Waspada"},
    {"Wilayah": "Bengkulu", "Target": 95000, "Realisasi": 91.0, "Status": "Optimal"},
])

col_logo1, col_logo2, col_logo3, col_title = st.columns([0.5, 0.5, 0.5, 5], vertical_alignment="center")

with col_logo1:
    st.image("OJK_Logo.png", use_container_width=True)

with col_logo2:
    st.image("logo_bi.png", use_container_width=True)

with col_logo3:
    st.image("logo-bgn.png", use_container_width=True) 

with col_title:
    st.markdown("""
        <div style="margin-left: 20px;">
            <h1 style="margin-bottom: 0px; font-size: 2.2rem;">MBG SENTRA</h1>
            <p style="color: #64748B; font-size: 1.1rem; margin-top: 5px; font-weight: 400;">
                Sinergi Antar Lembaga untuk Kesejahteraan Masyarakat
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
KOMODITAS_MBG = {
    "Beras": {"kategori": "Karbohidrat", "ref": 12500},
    "Telur Ayam Ras": {"kategori": "Protein Hewani", "ref": 26000},
    "Daging Ayam": {"kategori": "Protein Hewani", "ref": 35000},
    "Ikan (Kembung/Lele)": {"kategori": "Protein Hewani", "ref": 28000},
    "Tempe": {"kategori": "Protein Nabati", "ref": 10000},
    "Tahu": {"kategori": "Protein Nabati", "ref": 8000},
    "Sayuran Hijau (Bayam)": {"kategori": "Vitamin & Serat", "ref": 5000},
    "Wortel": {"kategori": "Vitamin & Serat", "ref": 12000},
    "Susu": {"kategori": "Gizi Tambahan", "ref": 15000},
    "Minyak Goreng": {"kategori": "Lemak/Pengolah", "ref": 18000}
}
TOLERANSI = 0.15 

if 'db_transaksi' not in st.session_state:
    st.session_state.db_transaksi = pd.DataFrame([
        {"ID": "TX001", "Waktu": "2026-03-22 09:00", "Bahan": "Beras", "Kategori": "Karbohidrat", "Harga": 12200, "Jumlah": 1000, "Supplier": "Koperasi Merah Putih", "Status": "Valid", "Anomali": False, "Verifikasi": "Diverifikasi Sistem"},
        {"ID": "TX002", "Waktu": "2026-03-22 10:30", "Bahan": "Telur Ayam Ras", "Kategori": "Protein Hewani", "Harga": 31000, "Jumlah": 500, "Supplier": "Vendor Luar X", "Status": "Bermasalah", "Anomali": True, "Verifikasi": "Belum Diverifikasi"}
    ])

# Helper UI Components
def draw_card(label, value, delta, status="A++", is_crit=False):
    badge = "status-badge-red" if is_crit else "status-badge"
    d_class = "delta-down" if is_crit else "delta-up"
    st.markdown(f"""<div class="custom-card"><div class="{badge}">{status}</div><div class="card-label">{label}</div><div class="card-value">{value}</div><div class="card-delta {d_class}">{delta}</div></div>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="nav-title">MBG SENTRA</p>', unsafe_allow_html=True)
    st.markdown('<p class="nav-subtitle">DIGITAL SOVEREIGNTY</p>', unsafe_allow_html=True)
    
    menu = st.radio("Navigasi", [
        "Dashboard Utama", "Halaman Transaksi", "Koperasi (Input Data)",
        "Deteksi Anomali & Intel", "Manajemen Supplier",
        "Whistleblower System (WBS)", "Transparansi Publik"
    ])
    
    st.divider()
    st.subheader("🤖 MBG Sentra Assistant")
    st.info("Harga stabil dalam 7 hari terakhir. Terdapat kenaikan tidak wajar pada Supplier Vendor Luar X.")
    st.caption("Nutritional insight: Menjamin ketersediaan pangan sehat merata.")

def draw_card(title, value, delta, status="A++", is_crit=False):
    # Logika warna
    bg_color = "#FEE2E2" if is_crit else "#FFFFFF"
    border_color = "#FECACA" if is_crit else "#E2E8F0"
    badge_bg = "#EF4444" if is_crit else "#DCFCE7"
    badge_text = "#FFFFFF" if is_crit else "#15803D"
    delta_color = "#B91C1C" if is_crit else "#15803D"
    st.markdown(f"""
        <div style="
            background-color: {bg_color};
            padding: 20px;
            border-radius: 12px;
            border: 1px solid {border_color};
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
            min-height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        ">
            <div style="
                background-color: {badge_bg};
                color: {badge_text};
                padding: 2px 10px;
                border-radius: 20px;
                font-size: 10px;
                font-weight: bold;
                width: fit-content;
                margin-bottom: 10px;
            ">
                {status}
            </div>
            <div style="color: #64748B; font-size: 14px; font-weight: 500;">{title}</div>
            <div style="color: #1E293B; font-size: 24px; font-weight: 700; margin: 5px 0;">{value}</div>
            <div style="color: {delta_color}; font-size: 12px; font-weight: 600;">{delta}</div>
        </div>
    """, unsafe_allow_html=True)

if menu == "Dashboard Utama":
    st.markdown("## 📊 Dashboard Monitoring Nasional")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Anggaran", "Rp 12.5 T", "4.2%")
    m2.metric("Penerima Manfaat", "45.2 Jt", "12.5%")
    m3.metric("Indeks Kepuasan", "4.8/5.0", "0.5%")
    m4.metric("Cakupan Wilayah", "38 Prov", "Statis")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    st.markdown("### 🛡️ Status Operasional")
    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        draw_card("Total Transaksi", "2", "↑ 12% dari bulan lalu")
    with c2: 
        draw_card("Avg. Harga Pangan", "Rp 24.500", "Stable (Tetap)")
    with c3: 
        draw_card("Supplier Aktif", "18 Koperasi", "Verified (Valid)")
    with c4: 
        draw_card("Anomali Sistem", "1 Kasus", "⚠ Perlu Investigasi", status="CRITICAL", is_crit=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown("**Tren Harga Transaksi Terakhir**")
        st.line_chart(st.session_state.db_transaksi, x="Waktu", y="Harga")
    with col_b:
        st.markdown("**Status Distribusi**")
        fig = px.pie(values=[80, 10, 10], names=['Berhasil', 'Pending', 'Anomali'], 
                     hole=0.4, color_discrete_sequence=['#10B981', '#F59E0B', '#EF4444'])
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.markdown("### 📍 Detail Sebaran Realisasi Program")
    st.dataframe(
        df, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "Realisasi": st.column_config.ProgressColumn(
                "Persentase Realisasi",
                help="Data realisasi dibandingkan target",
                format="%.1f%%",
                min_value=0,
                max_value=100,
            ),
        }
    )

    st.markdown("---")
    st.caption("© 2026 Dashboard Monitoring Nasional - Update Terakhir: 23 Maret 2026")

elif menu == "Halaman Transaksi":
    st.subheader("📝 Halaman Transaksi & Verifikasi Berlapis")
    with st.expander("🛠️ Panel Verifikasi Manual"):
        col_v1, col_v2 = st.columns(2)
        target_id = col_v1.selectbox("Pilih ID Transaksi", st.session_state.db_transaksi['ID'])
        new_verif = col_v2.selectbox("Status Verifikasi Baru", ["Belum Diverifikasi", "Diverifikasi Sistem", "Diverifikasi Koperasi", "Diverifikasi Sekolah"])
        if st.button("Update Status Verifikasi"):
            st.session_state.db_transaksi.loc[st.session_state.db_transaksi['ID'] == target_id, 'Verifikasi'] = new_verif
            st.success(f"Status {target_id} diperbarui!")
    st.divider()
    f_sup = st.multiselect("Filter Supplier", st.session_state.db_transaksi['Supplier'].unique())
    df_res = st.session_state.db_transaksi
    if f_sup: df_res = df_res[df_res['Supplier'].isin(f_sup)]
    st.dataframe(df_res, use_container_width=True)

elif menu == "Koperasi (Input Data)":
    st.subheader("📥 Pencatatan Bahan Pangan Terintegrasi")
    with st.form("input_koperasi"):
        c1, c2 = st.columns(2)
        bahan = c1.selectbox("Jenis Bahan", list(KOMODITAS_MBG.keys()))
        harga = c2.number_input("Harga per Satuan (IDR)", min_value=0, value=15000)
        jumlah = c1.number_input("Volume/Jumlah (Kg/Unit)", min_value=1, value=10)
        supplier = c2.selectbox("Pilih Supplier/Koperasi", ["Koperasi Merah Putih", "Vendor Luar X", "Koperasi Tani Jaya"])
        if st.form_submit_button("Validasi & Simpan ›"):
            ref_harga = KOMODITAS_MBG[bahan]['ref']
            diff = (harga - ref_harga) / ref_harga
            anomali = True if diff > TOLERANSI else False
            new_data = {"ID": f"TX{random.randint(100,999)}", "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"), "Bahan": bahan, "Kategori": KOMODITAS_MBG[bahan]['kategori'], "Harga": harga, "Jumlah": jumlah, "Supplier": supplier, "Status": "Bermasalah" if anomali else "Valid", "Anomali": anomali, "Verifikasi": "Diverifikasi Sistem" if not anomali else "Belum Diverifikasi"}
            st.session_state.db_transaksi = pd.concat([pd.DataFrame([new_data]), st.session_state.db_transaksi], ignore_index=True)
            st.success("Data berhasil diinput!")

elif menu == "Deteksi Anomali & Intel":
    st.subheader("🔍 Sistem Deteksi Anomali")
    anomalies = st.session_state.db_transaksi[st.session_state.db_transaksi['Anomali'] == True]
    if not anomalies.empty:
        for i, r in anomalies.iterrows():
            st.error(f"**Indikasi Mark-up:** {r['Bahan']} | Rp {r['Harga']} (Ref: Rp {KOMODITAS_MBG[r['Bahan']]['ref']})")
    else: st.success("Data Aman")

elif menu == "Manajemen Supplier":
    st.subheader("🤝 Manajemen Supplier & Reliability Score")
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric("Total Supplier Terdaftar", "18 Koperasi", "Aktif")
    col_s2.metric("Rata-rata Skor Kepercayaan", "88/100", "+2 pts")
    col_s3.metric("Supplier Risiko Tinggi", "1 Vendor", "⚠️ Perlu Audit", delta_color="inverse")
    st.divider()
    st.markdown("### 📋 Daftar Evaluasi & Rekam Jejak")
    data_supplier = pd.DataFrame({
        "Nama Koperasi/Vendor": ["Koperasi Merah Putih", "Koperasi X", "Vendor Logistik Mandiri", "KUD Sentosa", "Vendor Luar X"],
        "Komoditas": ["Beras", "Sayuran", "Daging Ayam", "Telur", "Multi-Bahan"],
        "Rata-rata Penawaran": [12100, 5200, 34500, 26200, 31000],
        "Skor": [99, 95, 88, 82, 45],
        "Status Kepercayaan": ["🟢 Terpercaya", "🟢 Terpercaya", "🟡 Perlu Monitoring", "🟡 Perlu Monitoring", "🔴 Risiko Tinggi"]
    })
    st.dataframe(data_supplier, use_container_width=True)
    st.divider()
    col_intel1, col_intel2 = st.columns([2, 1])
    with col_intel1: st.info("**Analisis Jangka Panjang:**\n\nVendor Luar X mengindikasikan strategi 'Price Skimming'.")
    with col_intel2: st.warning("**Rekomendasi:**\n\n* Audit gudang\n* Bekukan hak input jika skor < 40.")
    st.divider()
    st.markdown("### ⚖️ Perbandingan Harga")
    pilih_bahan = st.selectbox("Bandingkan Harga Penawaran untuk:", ["Beras", "Telur Ayam Ras", "Daging Ayam"])
    compare_data = pd.DataFrame({"Supplier": ["Koperasi Merah Putih", "Koperasi Tani Jaya", "Vendor Luar X"], "Harga Penawaran": [12100, 12400, 15000], "Selisih vs Pasar": ["-3.2%", "-0.8%", "+20.0%"]})
    st.table(compare_data)

elif menu == "Whistleblower System (WBS)":
    st.markdown('<div class="wbs-header"><h3 style="margin:0;">WBS: Whistleblowing System MBG SENTRA</h3><p style="margin:5px 0 0 0; font-size:14px; opacity:0.9;">LPSK Standardized Protection.</p></div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="wbs-container">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        kategori = c1.selectbox("Jenis Pelanggaran", ["Manipulasi Harga", "Kualitas Buruk", "Pungli", "Vendor Fiktif"])
        lokasi = c2.text_input("Lokasi Kejadian", placeholder="Contoh: SPPG Pamekasan")
        deskripsi = st.text_area("Deskripsi Kronologi", height=150)
        st.markdown("**Bukti Pendukung**")
        st.file_uploader("Upload file", label_visibility="collapsed")
        st.warning("🛡️ **Anonimitas Terjamin:** Sistem tidak mencatat IP address Anda.")
        if st.button("Kirim Laporan Terenkripsi ›"):
            if deskripsi and lokasi: st.success("✅ Laporan dikirim."); st.balloons()
            else: st.error("Lengkapi data.")
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Transparansi Publik":
    st.subheader("🌐 Transparansi Harga")
    st.table(pd.DataFrame([{"Bahan": k, "Kategori": v['kategori'], "Harga Ref": v['ref']} for k, v in KOMODITAS_MBG.items()]))
