import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def renderPage():
    st.markdown(
        '''
        <style>
        div[data-testid="stHorizontalBlock"] > div:first-of-type {
            background-color: #31495D;
            margin: 5px
        }
        </style>''',
        unsafe_allow_html = True
    )

    col_1, col_2 = st.columns([1, 2.25])

    with col_1:
        with st.container(height = 10, border = False):
            pass

        #foto
        with st.container():
            img_path = st.secrets.path_configuration['path_image']
            berkas_foto = "foto_diri.PNG"
            col_1_c1_col_1, col_1_c1_col_2, col_1_c1_col_3 = st.columns([1,8,1])
            with col_1_c1_col_1:
                st.write("")
            with col_1_c1_col_2:
                st.image(image = f"{img_path}/{berkas_foto}")
            with col_1_c1_col_3:
                st.write("")
        
        with st.container(height = 50, border = False):
            pass

        #kontak
        with st.container():
            original_title = '<p style = "font-family: Courier; color: white; text-decoration: underline; text-decoration-thickness: 5px; font-size: 30px; margin-left: 10px;">KONTAK</p>'
            st.markdown(original_title, unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">Email : janvier.r.r.tarigan@gmail.com</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">LinkedIn : linkedin.com/in/janvierrichardricardo/</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">Github : github.com/janvierrichard</p>', unsafe_allow_html = True)
        
        with st.container(height = 50, border = False):
            pass

        #biodata
        with st.container():
            original_title = '<p style = "font-family: Courier; color: white; text-decoration: underline; text-decoration-thickness: 5px; font-size: 30px; margin-left: 10px;">BIODATA</p>'
            st.markdown(original_title, unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">Tanggal Lahir : 16 Januari 1997</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">Kota Asal : Kota Bekasi</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">Alamat : Jl. Salak no. 100</p>', unsafe_allow_html = True)
        
        with st.container(height = 50, border = False):
            pass

        #kemampuan bahasa
        with st.container():
            original_title = '<p style = "font-family: Courier; color: white; text-decoration: underline; text-decoration-thickness: 5px; font-size: 30px; margin-left: 10px;">KEMAMPUAN BAHASA</p>'
            st.markdown(original_title, unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">Indonesia : Ahli</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">Inggris : Ahli</p>', unsafe_allow_html = True)
        
        with st.container(height = 50, border = False):
            pass

        #tech stack yang dikuasai
        with st.container():
            original_title = '<p style = "font-family: Courier; color: white; text-decoration: underline; text-decoration-thickness: 5px; font-size: 30px; margin-left: 10px;">PENGUASAAN TEKNOLOGI</p>'
            st.markdown(original_title, unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• Python</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• SQL</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• Pandas</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• MongoDB</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• Hadoop</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• Visualisasi Data</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• PowerBI</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• Tableau</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• Oracle</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• PostgreSQL</p>', unsafe_allow_html = True)
            st.markdown('<p style = "font-family: Courier; color: white; font-size: 12px; margin-left: 10px;">• MySQL</p>', unsafe_allow_html = True)
        
        with st.container(height = 500, border = False):
            pass

    with col_2:
        #perkenalan
        with st.container():
            st.header("JANVIER RICHARD RICARDO")
            st.markdown(
                '''
                <p style = "font-family: Courier; color: black; font-size: 12px;">
                Saya adalah seorang data analyst yang memiliki 2+ pengalaman kerja di industri konsultan dan multifinance.
                Saya memberikan impact pada proses bisnis dengan kemampuan berpikir strategis dan digital savvy yang saya
                miliki. Memiliki kemampuan fokus pada detail dan menonjol dalam kolaborasi tim, saya memiliki fundamental
                yang kuat dalam berpikir analitis untuk konsisten dalam memberikan actionable insights dengan track record
                yang sudah terbukti. Saya juga sangat mengedepankan proses belajar hal baru dan siap mengatasi tantangan
                serta masalah industri saat ini.
                </p>
                ''', unsafe_allow_html= True
            )
        
        with st.container(height = 10, border = False):
            pass

        st.divider()

        #pendidikan
        with st.container():
            st.header("Pendidikan")
            #pendidikan S1
            with st.container():
                col_2_c1_col_1, col_2_c1_col_2, col_2_c1_col_3 = st.columns([1, 15, 25])
                col_2_c1_col_2.markdown('<p style = "font-family: Courier; color: black; font-size: 12px;">2015-2020</p>', unsafe_allow_html= True)
                col_2_c1_col_3.markdown(
                                '''
                                <p style = "font-family: Courier; color: black; font-size: 12px;">INSTITUT TEKNOLOGI BANDUNG</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">FAKULTAS TEKNIK MESIN DAN DIRGANTARA</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">S1 TEKNIK MESIN</p>
                                ''', unsafe_allow_html = True
                                )
            
            st.container(height = 20, border = False)

            #pendidikan SMA
            with st.container():
                col_2_c2_col_1, col_2_c2_col_2, col_2_c2_col_3 = st.columns([1, 15, 25])
                col_2_c2_col_2.markdown('<p style = "font-family: Courier; color: black; font-size: 12px;">2012-2015</p>', unsafe_allow_html= True)
                col_2_c2_col_3.markdown(
                                '''
                                <p style = "font-family: Courier; color: black; font-size: 12px;">SMA NEGERI 81 JAKARTA</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">ILMU PENGETAHUAN ALAM (IPA)</p>
                                ''', unsafe_allow_html = True
                                )
            
        with st.container(height = 30, border = False):
            pass

        #pekerjaan
        with st.container():
            st.header("Pengalaman Kerja")
            #pekerjaan 1
            with st.container():
                col_2_c3_col_1, col_2_c3_col_2, col_2_c3_col_3 = st.columns([1, 15, 25])
                col_2_c3_col_2.markdown('<p style = "font-family: Courier; color: black; font-size: 12px;">Sep 2022 - Apr 2023</p>', unsafe_allow_html = True)
                col_2_c3_col_3.markdown(
                                '''
                                <p style = "font-family: Courier; color: black; font-size: 12px;">PT HOME CREDIT INDONESIA</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">Management Trainee</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Menjalankan strategi campaign untuk meningkatkan awareness karyawan HCID terkait strategi utama perusahaan tahun 2022, menghasilkan peningkatan awareness dari 37,5% menjadi 79,2%</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Menjalankan queri SQL dan menganalisis isu harian terkait analisis kredit</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Membangun dashboard dengan menggunakan PowerBI terkait profiling user</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Menginisiasi project penggunaan GPS sebagai salah satu feature analisis kredit, menghasilkan penurunan default rate dari 2,5% menjadi 2,2%</p>
                                ''', unsafe_allow_html= True
                                )
            
            st.container(height = 20, border = False)

            #pekerjaan 2
            with st.container():
                col_2_c4_col_1, col_2_c4_col_2, col_2_c4_col_3 = st.columns([1, 15, 25])
                col_2_c4_col_2.markdown('<p style = "font-family: Courier; color: black; font-size: 12px;">Des 2020 - Agu 2022</p>', unsafe_allow_html = True)
                col_2_c4_col_3.markdown(
                                '''
                                <p style = "font-family: Courier; color: black; font-size: 12px;">PT NIELSENIQ INDONESIA</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">Graduate Trainee</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Mengadakan survey tiap kuartal dengan memberikan insight kemajuan bisnis pada klien bumbu kecap, menghasilkan kenaikan nilai kontrak dari Rp240 juta menjadi Rp280 juta</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Berkolaborasi dengan tim untuk mengolah survey bulanan dari salah satu klien rokok dan memproses big data (>100.000 row) menghasilkan kenaikan nilai kontrak sebesar 9,1% (Rp44 milyar menjadi Rp48 milyar)</p>
                                ''', unsafe_allow_html = True
                                )
        
        with st.container(height = 30, border = False):
            pass

        #pengalaman pelatihan
        with st.container():
            st.header("Pengalaman Pelatihan")
            #pelatihan 1
            with st.container():
                col_2_c8_col_1, col_2_c8_col_2, col_2_c8_col_3 = st.columns([1, 15, 25])
                col_2_c8_col_2.markdown('<p style = "font-family: Courier; color: black; font-size: 12px;">Oct 2023 - Feb 2024</p>', unsafe_allow_html = True)
                col_2_c8_col_3.markdown(
                                '''
                                <p style = "font-family: Courier; color: black; font-size: 12px;">SANBERCAMPUS X ITB</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">Fullstack Data Science</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Menganalisis data sebuah LSM yang bertujuan untuk memberikan bantuan dana kepada negara prioritas berdasarkan beberapa indikator</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Memprediksi sentimen dari suatu marketplace dengan menggunakan NLP vectorizer dan machine learning</p>
                                <p style = "font-family: Courier; color: black; font-size: 12px;">• Membuat sebuah chatbot sederhana dengan kemampuan pencarian informasi</p>
                                ''', unsafe_allow_html = True
                                )