# Pencarian Buku Pengembangan Diri
Program ini adalah aplikasi sederhana untuk mencari buku pengembangan diri berdasarkan kata kunci pencarian. Aplikasi ini menggunakan teknik pemrosesan teks, Term Frequency-Inverse Document Frequency (TF-IDF), dan Cosine Similarity untuk menemukan buku-buku yang paling relevan dengan kata kunci yang dimasukkan oleh pengguna.

## Persiapan Lingkungan Pengembangan
Sebelum menjalankan program, Anda perlu membuat dan mengaktifkan lingkungan virtual Python. Langkah-langkah ini dapat dilakukan dengan perintah berikut:

1. Buka terminal atau command prompt di direktori proyek Anda.
2. Buat lingkungan virtual dengan menjalankan perintah:

  ```
  python -m venv .venv
  ```
3. Aktifkan lingkungan virtual sesuai dengan sistem operasi Anda:

```
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```

## Penggunaan
1. Pastikan Anda telah menginstal semua library yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt:
```
pip install streamlit pandas scikit-learn nltk
```

2. Jalankan program dengan perintah:
```
streamlit run app.py
```
atau
```
python -m streamlit run app.py
```
3. Buka web browser dan akses alamat yang diberikan oleh Streamlit.
4. Anda akan melihat antarmuka pengguna sederhana yang meminta Anda untuk memasukkan kata kunci pencarian.
5. Masukkan kata kunci pencarian Anda ke dalam kotak teks yang tersedia.
6. Klik tombol "Cari" untuk memulai pencarian.
7. Hasil pencarian akan ditampilkan di bawahnya, termasuk judul buku, penulis, dan sinopsisnya.
