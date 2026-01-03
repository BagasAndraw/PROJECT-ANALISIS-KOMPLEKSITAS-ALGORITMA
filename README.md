# Analisis Kompleksitas Algoritma Iteratif dan Rekursif  
## pada Simulasi Gerak Bola Pantul

## 📌 Deskripsi Proyek
Proyek ini merupakan tugas besar mata kuliah Analisis Algoritma yang bertujuan untuk
menganalisis dan membandingkan efisiensi algoritma iteratif dan rekursif dalam
menyelesaikan suatu studi kasus, yaitu simulasi gerak bola pantul.

Simulasi bola pantul menggambarkan pergerakan sebuah bola yang dijatuhkan dari ketinggian
awal tertentu dan memantul berulang kali dengan tinggi pantulan yang menurun berdasarkan
koefisien elastisitas. Proyek ini tidak hanya menampilkan simulasi secara visual, tetapi
juga menganalisis kompleksitas waktu dan running time dari kedua algoritma.

---

## 🎯 Tujuan
1. Mengimplementasikan algoritma iteratif dan rekursif untuk studi kasus yang sama.
2. Membandingkan hasil keluaran kedua algoritma untuk memastikan konsistensi hasil.
3. Menganalisis efisiensi algoritma berdasarkan:
   - Kompleksitas waktu (teoretis)
   - Running time (eksperimental)
4. Menyajikan hasil analisis dalam bentuk grafik, tabel, dan visualisasi interaktif.

---

## 🧠 Studi Kasus
Studi kasus yang digunakan adalah **simulasi gerak bola pantul**, dengan parameter utama:
- `h0` : tinggi awal bola
- `e`  : koefisien elastisitas (0 < e < 1)
- `h_min` : tinggi minimum untuk menghentikan simulasi

Tinggi pantulan berikutnya dihitung menggunakan relasi:

---

## ⚙️ Algoritma yang Digunakan

### 1️⃣ Algoritma Iteratif
- Diimplementasikan menggunakan perulangan `while`
- Menghitung tinggi pantulan hingga mencapai batas minimum
- Kompleksitas waktu: **O(n)**, dengan n adalah jumlah pantulan

### 2️⃣ Algoritma Rekursif
- Diimplementasikan menggunakan pemanggilan fungsi secara rekursif
- Menggunakan base case untuk menghentikan proses
- Kompleksitas waktu: **O(n)**

> Kedua algoritma menghasilkan output yang identik, sehingga perbedaan performa hanya
> disebabkan oleh cara implementasi algoritma.

---

## 🖥️ Aplikasi (Visualisasi)
Aplikasi dibuat dalam bentuk **website sederhana** menggunakan:
- HTML
- CSS
- JavaScript (Canvas)

Fitur visualisasi:
- Simulasi live gerak bola pantul
- Input interaktif (`h0` dan `e`)
- Counter jumlah pantulan
- Tabel log tinggi pantulan
- Sumbu X dan Y dengan skala

> Catatan: Visualisasi hanya digunakan sebagai ilustrasi gerak bola dan **tidak digunakan
> untuk pengukuran kompleksitas algoritma**.

---

## ⏱️ Analisis Running Time
Pengukuran running time dilakukan menggunakan Python dengan ketentuan:
- Menggunakan `time.perf_counter()` untuk presisi tinggi
- Pengukuran dilakukan secara **rata-rata dari 1000 pengulangan**
- Pengujian dilakukan pada algoritma iteratif dan rekursif dengan input yang sama

Hasil pengukuran disimpan dalam file:

---

## 📊 Eksperimen Variasi Ukuran Input
Untuk memenuhi analisis pada berbagai ukuran masukan, dilakukan beberapa eksperimen:
1. Variasi nilai koefisien elastisitas (`e`) terhadap jumlah pantulan
2. Variasi tinggi awal (`h0`) terhadap running time algoritma

Hasil eksperimen ditampilkan dalam bentuk:
- Grafik
- Tabel data

---

## 🧩 Struktur Proyek

---

## 📌 Kesimpulan
1. Algoritma iteratif dan rekursif menghasilkan hasil simulasi yang sama.
2. Algoritma iteratif memiliki running time yang lebih efisien dibandingkan rekursif.
3. Kompleksitas waktu kedua algoritma adalah **O(n)**, namun implementasi iteratif
   memiliki overhead yang lebih kecil.
4. Visualisasi membantu pemahaman konsep, sedangkan analisis algoritma dilakukan secara
   terpisah melalui pengukuran running time.

---

## 👨‍💻 Catatan
Proyek ini dikembangkan sebagai bagian dari tugas besar Analisis Algoritma dan
ditujukan untuk keperluan akademik.
