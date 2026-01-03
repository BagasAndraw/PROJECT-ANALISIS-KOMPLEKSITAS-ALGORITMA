import time
import matplotlib.pyplot as plt
import csv

from iteratif import pantulan_iteratif
from rekursif import pantulan_rekursif

h0 = 10.0
e = 0.6
h_min = 0.01
REPEAT = 1000 

def ukur_waktu(func, *args, repeat=1000):
    total_time = 0.0
    for _ in range(repeat):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / repeat

hasil_iteratif = pantulan_iteratif(h0, e, h_min)
hasil_rekursif = pantulan_rekursif(h0, e, h_min)

waktu_iteratif = ukur_waktu(
    pantulan_iteratif, h0, e, h_min, repeat=REPEAT
)

waktu_rekursif = ukur_waktu(
    pantulan_rekursif, h0, e, h_min, repeat=REPEAT
)

selisih = abs(waktu_rekursif - waktu_iteratif)

print("=== HASIL ANALISIS (RATA-RATA) ===")
print(f"Jumlah pantulan (iteratif): {len(hasil_iteratif)}")
print(f"Jumlah pantulan (rekursif): {len(hasil_rekursif)}")
print(f"Waktu iteratif  (avg): {waktu_iteratif:.8f} detik")
print(f"Waktu rekursif  (avg): {waktu_rekursif:.8f} detik")
print(f"Selisih waktu         : {selisih:.8f} detik")
print(f"Pengulangan pengukuran: {REPEAT} kali")

plt.figure(figsize=(8, 5))
plt.plot(hasil_iteratif, marker='o', label='Iteratif')
plt.plot(hasil_rekursif, marker='x', linestyle='--', label='Rekursif')
plt.title("Grafik Tinggi Pantulan Bola")
plt.xlabel("Pantulan ke-n")
plt.ylabel("Tinggi Pantulan (meter)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.bar(
    ["Iteratif", "Rekursif"],
    [waktu_iteratif, waktu_rekursif]
)
plt.title("Perbandingan Waktu Eksekusi (Rata-rata)")
plt.ylabel("Waktu (detik)")
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

with open("hasil_pengukuran.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Metode",
        "Waktu Rata-rata (detik)",
        "Jumlah Pantulan",
        "Jumlah Pengulangan"
    ])
    writer.writerow([
        "Iteratif",
        waktu_iteratif,
        len(hasil_iteratif),
        REPEAT
    ])
    writer.writerow([
        "Rekursif",
        waktu_rekursif,
        len(hasil_rekursif),
        REPEAT
    ])
    writer.writerow([
        "Selisih",
        selisih,
        "-",
        "-"
    ])
