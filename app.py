import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import random

# 1. Konfigurasi Halaman (Hanya boleh sekali di paling atas)
st.set_page_config(layout="wide", page_title="MBG SENTRA | National Monitoring", page_icon="🥘")

# 2. Injection CSS untuk tampilan Pro
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background-color: #FBFBFE;
    }

    /* Card Styling */
    .metric-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #D1D5DB;
    }

    /* Red Accent for Button */
    .stButton>button {
        background-color: #EF4444 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        width: 100%;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Header Navbar Look */
    .nav-container {
        display: flex;
        align-items: center;
        padding: 1rem;
        background: white;
        border-radius: 12px;
        margin-bottom: 2rem;
        border-bottom: 3px solid #EF4444; /* Aksen Merah Rahma */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Data & State Management
if 'db_transaksi' not in st.session_state:
    st.session_state.db_transaksi = pd.DataFrame([
        {"ID": "TX001", "Waktu": "2026-03-22 09:00", "Bahan": "Beras", "Kategori": "Karbohidrat", "Harga": 12200, "Jumlah": 1000, "Supplier": "Koperasi Merah Putih", "Status": "Valid", "Anomali": False, "Verifikasi": "Diverifikasi Sistem"},
        {"ID": "TX002", "Waktu": "2026-03-22 10:30", "Bahan": "Telur Ayam Ras", "Kategori": "Protein Hewani", "Harga": 31000, "Jumlah": 500, "Supplier": "Vendor Luar X", "Status": "Bermasalah", "Anomali": True, "Verifikasi": "Belum Diverifikasi"}
    ])

KOMODITAS_MBG = {
    "Beras": {"kategori": "Karbohidrat", "ref": 12500},
    "Telur Ayam Ras": {"kategori": "Protein Hewani", "ref": 26000},
    "Daging Ayam": {"kategori": "Protein Hewani", "ref": 35000},
    "Susu": {"kategori": "Gizi Tambahan", "ref": 15000}
}

# 4. Sidebar Navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/EF4444/FFFFFF?text=MBG+SENTRA", use_container_width=True)
    st.overline("ADMIN DASHBOARD")
    menu = st.radio("Navigasi Utama", [
        "📊 Dashboard Utama", 
        "📑 Halaman Transaksi", 
        "📥 Input Data Koperasi",
        "🛡️ Whistleblower System"
    ])
    st.divider()
    st.markdown("### 🤖 AI Insight")
    st.info("Sistem mendeteksi 1 transaksi tidak wajar di wilayah Bengkulu. Segera cek menu Anomali.")

# 5. Header Section
st.markdown(f"""
    <div class="nav-container">
        <h2 style="margin:0; color:#1E293B;">🥘 MBG SENTRA <span style="font-size:14px; color:#64748B; font-weight:400;">| Digital Sovereignty System</span></h2>
    </div>
    """, unsafe_allow_html=True)

# 6. Logic Menu
if menu == "📊 Dashboard Utama":
    # Baris Pertama: Big Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card"><p style="color:#64748B; font-size:14px;">Total Anggaran</p><h2 style="margin:0; color:#1E293B;">Rp 12.5 T</h2><p style="color:#10B981; font-size:12px;">↑ 4.2%</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><p style="color:#64748B; font-size:14px;">Penerima Manfaat</p><h2 style="margin:0; color:#1E293B;">45.2 Jt</h2><p style="color:#10B981; font-size:12px;">↑ 12.5%</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><p style="color:#64748B; font-size:14px;">Skor Transparansi</p><h2 style="margin:0; color:#1E293B;">98%</h2><p style="color:#10B981; font-size:12px;">Grade A+</p></div>', unsafe_allow_html=True)
    with col4:
        # Anomali dikasih aksen Merah karena ini fokus Rahma
        st.markdown('<div class="metric-card" style="border-left: 5px solid #EF4444;"><p style="color:#64748B; font-size:14px;">Anomali Sistem</p><h2 style="margin:0; color:#EF4444;">1 Kasus</h2><p style="color:#EF4444; font-size:12px;">⚠ Investigasi</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Baris Kedua: Grafik
    c_left, c_right = st.columns([2, 1])
    with c_left:
        st.subheader("📍 Realisasi Program per Provinsi")
        df_geo = pd.DataFrame({
            "Wilayah": ["Bengkulu", "DKI Jakarta", "Jawa Barat", "Jawa Timur"],
            "Realisasi": [91.0, 85.2, 78.9, 80.1]
        })
        fig = px.bar(df_geo, x='Wilayah', y='Realisasi', color='Realisasi', 
                     color_continuous_scale='Reds', template='plotly_white')
        st.plotly_chart(fig, use_container_width=True)
        
    with c_right:
        st.subheader("📊 Komposisi Gizi")
        fig_pie = px.pie(values=[30, 40, 20, 10], names=["Karbo", "Protein", "Vitamin", "Susu"], 
                         hole=0.5, color_discrete_sequence=px.colors.sequential.Reds_r)
        st.plotly_chart(fig_pie, use_container_width=True)

elif menu == "📥 Input Data Koperasi":
    st.subheader("📥 Form Input Pengadaan Bahan")
    with st.container(border=True):
        with st.form("input_koperasi"):
            c1, c2 = st.columns(2)
            bahan = c1.selectbox("Jenis Bahan", list(KOMODITAS_MBG.keys()))
            supplier = c2.selectbox("Koperasi Supplier", ["Koperasi Merah Putih", "Vendor Luar X", "Koperasi Tani Jaya"])
            harga = c1.number_input("Harga per Kg (IDR)", min_value=0, value=15000)
            jumlah = c2.number_input("Volume (Kg)", min_value=1, value=100)
            
            submitted = st.form_submit_button("Validasi & Kirim ke Blockchain")
            if submitted:
                st.success(f"Data {bahan} dari {supplier} telah diverifikasi sistem!")

elif menu == "🛡️ Whistleblower System":
    st.markdown("""
        <div style="background-color:#FEE2E2; padding:20px; border-radius:12px; border-left: 6px solid #EF4444;">
            <h3 style="margin:0; color:#991B1B;">🛡️ WBS - Pelaporan Pelanggaran</h3>
            <p style="color:#B91C1C;">Laporan Anda akan dienkripsi dan anonimitas dijamin oleh standar LPSK.</p>
        </div>
    """, unsafe_allow_html=True)
    # Form WBS... (mirip kodemu tapi di dalam container)

# Footer
st.markdown("---")
st.caption(f"Admin: Rahma Oktavia Albar | NIM: 123450003 | Dashboard Session: {datetime.now().strftime('%H:%M:%S')}")
