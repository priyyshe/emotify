# 🚀 Emotify Advanced: Chatbot Literasi Emosi Canggih untuk Remaja

## Deskripsi Singkat

Remaja sering mengalami kesulitan dalam memahami, mengekspresikan, dan mengelola emosinya. Emotify Advanced adalah chatbot edukatif interaktif berbasis AI yang dirancang untuk membantu remaja mengenali jenis emosi yang mereka alami berdasarkan teks yang mereka tulis. Lebih dari itu, Emotify kini dilengkapi dengan berbagai fitur canggih seperti mode curhat bebas (journaling), pelacakan riwayat emosi dengan visualisasi, tantangan interaktif untuk keseimbangan emosi, kamus emosi, dan ruang refleksi untuk mendukung perjalanan literasi emosi mereka secara menyeluruh.

---

## Fitur Utama

- ✨ **Deteksi Emosi Akurat**: Menggunakan model transformers (`j-hartmann/emotion-english-distilroberta-base`) untuk mengenali emosi dari teks.
- 💬 **Respons Edukatif Bervariasi**: Memberikan tanggapan yang dinamis, edukatif, dan suportif sesuai jenis emosi yang terdeteksi.
- ✍️ **Mode Curhat Bebas (Journaling)**: Ruang aman bagi pengguna untuk menuliskan curahan hati tanpa langsung dianalisis, dengan opsi analisis di kemudian waktu.
- 📊 **Riwayat & Peta Emosi Sesi Ini**: Melacak emosi yang terdeteksi selama sesi penggunaan dan menampilkannya dalam bentuk daftar serta grafik visual (bar chart) untuk membantu mengenali pola.
- 🎯 **Tantangan Keseimbangan Emosi Interaktif**: Menyediakan daftar tantangan harian/mingguan yang dapat dicentang pengguna untuk mendorong praktik kesejahteraan emosional.
- 📚 **Kamus Emosi**: Penjelasan singkat mengenai berbagai jenis emosi dasar untuk meningkatkan pemahaman.
- 🤔 **Refleksi Minggu Ini**: Kutipan atau pertanyaan reflektif untuk mendorong introspeksi.
- 📢 **Fitur Masukan Pengguna**: Memungkinkan pengguna memberikan saran untuk pengembangan Emotify.
- 🖥️ **Antarmuka Interaktif & Ramah Pengguna**: Dibangun dengan Streamlit untuk pengalaman pengguna yang mulus dan menarik.

---

## Cara Menjalankan di Lokal

1.  **Clone repositori ini** (jika sudah ada, pastikan versi terbaru):
    ```bash
    git clone [https://github.com/username/emotify.git](https://github.com/username/emotify.git) # Ganti dengan URL repo Anda
    cd emotify
    ```

2.  **Buat dan aktifkan environment virtual** (direkomendasikan):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependensi**:
    Pastikan kamu memiliki file `requirements.txt` yang berisi:
    ```txt
    streamlit
    transformers
    torch # atau tensorflow, tergantung backend transformers yang ingin digunakan
    matplotlib
    # Tambahkan library lain jika ada
    ```
    Kemudian jalankan:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan aplikasi**:
    ```bash
    streamlit run app.py
    ```
    *Catatan: `app.py` adalah nama file utama aplikasi Streamlit Anda.*

---

## Preview Aplikasi

*(Anda bisa menambahkan screenshot atau GIF dari aplikasi Emotify Advanced di sini)*

---

## Link Deploy

Aplikasi ini dapat diakses secara online melalui Streamlit Cloud (jika sudah di-deploy):
🔗 [Link ke Aplikasi Emotify Anda di Streamlit Cloud]
*(Contoh: https://emotify-advanced-xxxx.streamlit.app/)*

---

## Teknologi yang Digunakan

* Python
* Streamlit
* Hugging Face Transformers (`pipeline`)
* Matplotlib (untuk visualisasi grafik emosi)
* Model AI: `j-hartmann/emotion-english-distilroberta-base`

---

## Potensi Pengembangan di Masa Depan

* Integrasi model NLP yang secara spesifik dilatih atau di-*fine-tune* untuk Bahasa Indonesia untuk meningkatkan akurasi pada input berbahasa Indonesia.
* Fitur penyimpanan data pengguna (dengan izin dan enkripsi) untuk melacak progres emosi jangka panjang.
* Notifikasi atau pengingat untuk tantangan atau refleksi.

---

## Kontributor

* Apriyanti
* putu eka permata


