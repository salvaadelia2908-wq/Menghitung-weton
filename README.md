

## 1. Definisi (Proyek)

Secara sederhana, proyek "Menghitung Weton" adalah **proses merancang dan membangun sebuah sistem atau program (dalam kasus ini, menggunakan Python) yang mampu mengkonversi tanggal dalam kalender Masehi (Gregorian) menjadi sistem penanggalan Jawa**, yaitu **Weton**.

🌹Weton sendiri adalah gabungan dari dua siklus hari:
1.  **Saptawara (Dina):** Siklus 7 harian (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu).
2.  **Pancawara (Pasaran):** Siklus 5 harian (Legi, Pahing, Pon, Wage, Kliwon).

Jadi, definisi proyek ini adalah membuat alat otomatis yang bisa menerima input (misalnya: 23 Oktober 2025) dan menghasilkan output (misalnya: Kamis Wage).

---

## 2. Manfaat

🌹Manfaat dari proyek ini dapat dibagi menjadi beberapa kategori:

* **Manfaat Praktis (Efisiensi):**
    * **Kecepatan & Akurasi:** Menghilangkan kebutuhan perhitungan manual yang rumit dan rentan kesalahan (*human error*).
    * **Aksesibilitas:** Siapa saja dapat mengetahui weton mereka atau tanggal tertentu dengan mudah tanpa perlu memiliki buku Primbon atau almanak Jawa fisik.

* **Manfaat Kultural (Pelestarian):**
    * **Digitalisasi Budaya:** Mentransformasikan warisan budaya leluhur (ilmu titen Jawa) ke dalam format digital yang relevan dengan generasi modern.
    * **Edukasi:** Menjadi sarana pembelajaran bagi orang yang ingin belajar tentang budaya Jawa dan sistem penanggalannya.

* **Manfaat Teknis (Bagi Developer):**
    * **Pembelajaran Algoritma:** Melatih logika pemrograman, terutama dalam menangani perhitungan tanggal, tahun kabisat, dan operasi matematika (khususnya *modulo*).

---

## 3. Ide Karya

Ide karya (konsep inti) dari proyek ini adalah **menggunakan logika matematika untuk meniru perhitungan kalender tradisional.**

Inti dari ide ini adalah **Sistem Perhitungan Berbasis Titik Acuan (Reference Point)**.

🌹Algoritma dasarnya bekerja seperti ini:
1.  **Tentukan Titik Acuan:** Anda harus memiliki satu tanggal Masehi yang Anda tahu pasti apa wetonnya. Contoh: **1 Januari 1900 adalah Senin Pon**.
2.  **Hitung Selisih Hari:** Program menghitung total jumlah hari antara tanggal acuan (1 Jan 1900) dan tanggal yang ingin dicari (misalnya, 23 Oktober 2025). Perhitungan ini harus memperhitungkan **tahun kabisat**.
3.  **Gunakan Modulo (Sisa Bagi):**
    * Untuk mencari *Dina* (hari ke-7): `Total Selisih Hari % 7`
    * Untuk mencari *Pasaran* (hari ke-5): `Total Selisih Hari % 5`
4.  **Konversi Hasil:** Hasil angka dari modulo tadi (misal 0, 1, 2, 3...) kemudian dipetakan ke nama hari dan pasaran yang sesuai (misal 0=Senin, 1=Selasa... dan 0=Pon, 1=Wage...).

Ide karya ini adalah tentang **transformasi** dari pengetahuan kualitatif (Primbon) menjadi algoritma kuantitatif (kode Python).

---

## 4. Kreativitas

🌹Banyak orang mungkin berpikir proyek perhitungan seperti ini "tidak kreatif" karena hanya berdasarkan rumus pasti. Ini salah. Kreativitas dalam proyek ini terletak pada:

* **Desain Algoritma:** Menemukan cara paling efisien untuk menghitung selisih hari. Bagaimana Anda menangani tahun kabisat (misalnya, `(tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)`) adalah sebuah proses pemecahan masalah yang kreatif.
* **Antarmuka (Interface):** Kreativitas muncul saat Anda memutuskan *bagaimana* hasil disajikan.
    * *Dasar:* Hanya menampilkan teks "Kamis Wage".
    * *Kreatif:* Menampilkan "Kamis Wage", ditambah **Nilai Neptu** (Kamis=8, Wage=4, total 12), dan ditambah **interpretasi watak** berdasarkan nilai neptu tersebut (misal: "Lakuning Kembang").
* **Pengembangan Fitur (Ekspansi Ide):**
    * Kreativitas tertinggi muncul saat Anda mengembangkan ide dasar ini. Dari sekadar menghitung weton, program Anda bisa dikembangkan menjadi:
        * Kalkulator kecocokan pasangan (berdasarkan pertemuan neptu).
        * Penentu hari baik untuk pindah rumah atau memulai usaha.
        * Pencari "Malam Jumat Kliwon" atau "Selasa Kliwon" terdekat.
        * Membuat *web app* atau *bot Telegram/WhatsApp* untuk cek weton.
 ## 5. Cara Kerja
 1. **Buka aplikasi "menghitung weton"**
 2. **Klik "pilih hari" dan "pilih pasaran"**
 3. **Setelah itu klik "hitung", jawaban akan muncul dibawah**
  
