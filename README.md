# Aplikasi Prediksi Harga Kos Madiun (Sistem Cerdas - Pertemuan 14)

Aplikasi web berbasis Django dan Machine Learning (Linear Regression) untuk memprediksi estimasi harga sewa bulanan kos di wilayah Madiun berdasarkan jarak ke kampus, rating kos, dan ketersediaan fasilitas AC. Aplikasi ini juga dilengkapi visualisasi grafik batang perbandingan rata-rata harga kos berdasarkan kategori AC.

## Identitas Pengembang (Pengerjaan Mandiri)
- Nama: Fikka Dwy Ayu Nur Mutoharoh
- NIM: 253307034
- Kelas: 2B - D3 Teknologi Informasi, Politeknik Negeri Madiun
- Mata Kuliah: Sistem Cerdas (TI24317)
- Ruang Lingkup: Perancangan arsitektur proyek, pelatihan & pembekuan model ML (joblib), pengembangan backend layanan prediksi (services.py), antarmuka pengguna & grafik (Chart.js), serta dokumentasi.

## Informasi Dataset
- Nama File: web_kos/dataset/kos_madiun.csv
- Fitur Input (X): jarak_km (numerik), rating (numerik), dan ac (ya/tidak yang dipetakan menjadi 1/0).
- Target (y): harga (dalam satuan ribu rupiah per bulan).
- Sumber & Lisensi: Dataset praktikum internal Mata Kuliah Sistem Cerdas, Program Studi Teknologi Informasi, Politeknik Negeri Madiun (digunakan khusus untuk keperluan akademik dan edukasi).

## Struktur Proyek
- SistemCerdas_P14/.gitignore : Daftar pengecualian file agar .venv dan database lokal tidak ikut ter-upload.
- SistemCerdas_P14/web_kos/apps/prediksi/services.py : Logika pemuatan model (.joblib) & kalkulasi prediksi.
- SistemCerdas_P14/web_kos/apps/prediksi/urls.py : Konfigurasi routing aplikasi.
- SistemCerdas_P14/web_kos/apps/prediksi/views.py : Controller penghubung form input, model ML, & grafik.
- SistemCerdas_P14/web_kos/config/settings.py : Konfigurasi utama proyek Django.
- SistemCerdas_P14/web_kos/config/urls.py : Routing utama proyek.
- SistemCerdas_P14/web_kos/dataset/kos_madiun.csv : Dataset harga kos Madiun.
- SistemCerdas_P14/web_kos/dataset/latih_model.py : Skrip pelatihan & pembekuan model Linear Regression.
- SistemCerdas_P14/web_kos/dataset/model_kos.joblib : Model ML terlatih yang siap digunakan.
- SistemCerdas_P14/web_kos/static/css/style.css : Styling antarmuka pengguna.
- SistemCerdas_P14/web_kos/static/js/chart_ac.js : Skrip rendering grafik batang dengan Chart.js.
- SistemCerdas_P14/web_kos/templates/base.html : Template kerangka utama HTML.
- SistemCerdas_P14/web_kos/templates/prediksi/index.html : Halaman form prediksi & visualisasi grafik.
- SistemCerdas_P14/web_kos/manage.py : Utilitas baris perintah Django.
- SistemCerdas_P14/web_kos/README.md : Dokumentasi proyek.
- SistemCerdas_P14/web_kos/requirements.txt : Daftar dependensi Python.

## Cara Menjalankan Aplikasi
1. Clone repositori dan masuk ke direktori proyek:
   git clone https://github.com/fikkadwy21-rgb/SistemCerdas_P14.git
   cd SistemCerdas_P14

2. Buat dan aktifkan virtual environment:
   python -m venv .venv
   .venv\Scripts\activate

3. Instal seluruh pustaka yang dibutuhkan:
   pip install -r web_kos/requirements.txt

4. Jalankan migrasi database dan server lokal Django:
   cd web_kos
   python manage.py migrate
   python manage.py runserver

5. Buka browser dan akses http://127.0.0.1:8000/