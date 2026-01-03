# Analisis Kompleksitas Algoritma Iteratif dan Rekursif  
## pada Simulasi Gerak Bola Pantul

## Deskripsi Studi Kasus
Proyek ini merupakan tugas besar mata kuliah Analisis Algoritma yang bertujuan untuk menganalisis dan membandingkan efisiensi algoritma iteratif dan rekursif dalam menyelesaikan suatu studi kasus, yaitu simulasi gerak bola pantul.

Simulasi bola pantul menggambarkan pergerakan sebuah bola yang dijatuhkan dari ketinggian awal tertentu dan memantul berulang kali dengan tinggi pantulan yang menurun berdasarkan koefisien elastisitas. Proyek ini tidak hanya menampilkan simulasi secara visual, tetapi juga menganalisis kompleksitas waktu dan running time dari kedua algoritma.

---

## Tujuan
1. Mengimplementasikan algoritma iteratif dan rekursif untuk studi kasus yang sama.
2. Membandingkan hasil keluaran kedua algoritma untuk memastikan konsistensi hasil.
3. Menganalisis efisiensi algoritma berdasarkan kompleksitas waktu (teoretis) dan running time (eksperimental).
4. Menyajikan hasil analisis dalam bentuk grafik, tabel, dan visualisasi interaktif.

---

## Studi Kasus
Studi kasus yang digunakan adalah simulasi gerak bola pantul dengan parameter utama:
- `h0` : tinggi awal bola
- `e`  : koefisien elastisitas (0 < e < 1)
- `h_min` : tinggi minimum untuk menghentikan simulasi

Tinggi pantulan berikutnya dihitung menggunakan relasi:
```
h(n+1) = e × h(n)
```

---

## Algoritma yang Digunakan

### Algoritma Iteratif
Algoritma iteratif diimplementasikan menggunakan perulangan `while` untuk menghitung tinggi pantulan bola hingga mencapai batas minimum. Kompleksitas waktu algoritma ini adalah **O(n)**, dengan n adalah jumlah pantulan.

### Algoritma Rekursif
Algoritma rekursif diimplementasikan menggunakan pemanggilan fungsi secara rekursif hingga mencapai kondisi dasar (*base case*). Kompleksitas waktu algoritma ini juga **O(n)**.

Kedua algoritma menghasilkan keluaran yang sama, sehingga perbandingan difokuskan pada efisiensi waktu eksekusi.

---

## Visualisasi
Aplikasi dibuat dalam bentuk website sederhana menggunakan HTML, CSS, dan JavaScript (Canvas). Fitur visualisasi yang disediakan meliputi:
- Simulasi live gerak bola pantul
- Input interaktif nilai `h0` dan `e`
- Counter jumlah pantulan
- Tabel log tinggi pantulan
- Sumbu X dan Y dengan skala

Catatan: Visualisasi hanya digunakan sebagai ilustrasi gerak bola dan tidak digunakan dalam pengukuran kompleksitas algoritma.

---

## Analisis Running Time
Pengukuran running time dilakukan menggunakan Python dengan ketentuan:
- Menggunakan `time.perf_counter()` untuk presisi tinggi
- Pengukuran dilakukan menggunakan nilai rata-rata dari 1000 pengulangan
- Pengujian dilakukan pada algoritma iteratif dan rekursif dengan parameter input yang sama

Hasil pengukuran disimpan dalam file `hasil_pengukuran.csv`.

---

## Eksperimen Variasi Ukuran Input
Eksperimen dilakukan dengan memvariasikan ukuran input, antara lain:
1. Variasi nilai koefisien elastisitas (`e`) terhadap jumlah pantulan
2. Variasi tinggi awal (`h0`) terhadap running time algoritma

Hasil eksperimen disajikan dalam bentuk grafik dan tabel untuk mempermudah analisis.

---

## Struktur Project
```
project/
├── iteratif.py
├── rekursif.py
├── ukur_waktu.py
├── eksperimen_variatif.py
│
├── hasil_pengukuran.csv
│
└── web/
    ├── index.html
    ├── style.css
    ├── script.js
    └── assets/
        ├── grafik_waktu.png
        ├── grafik_pantulan.png
        └── grafik_variatif.png
```

---

## Kesimpulan
1. Algoritma iteratif dan rekursif menghasilkan hasil simulasi yang sama.
2. Algoritma iteratif memiliki running time yang lebih efisien dibandingkan algoritma rekursif.
3. Kompleksitas waktu kedua algoritma adalah **O(n)**, namun algoritma iteratif memiliki overhead yang lebih kecil.
4. Visualisasi membantu pemahaman konsep, sedangkan analisis algoritma dilakukan melalui pengukuran running time secara terpisah.

---


