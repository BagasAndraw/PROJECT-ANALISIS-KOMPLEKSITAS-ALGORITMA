import matplotlib.pyplot as plt

from iteratif import pantulan_iteratif
from rekursif import pantulan_rekursif
from ukur_waktu import ukur_waktu

h_min = 0.01
e = 0.6

h0 = 300
e_values = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
pantulan_counts = []

for e_val in e_values:
    hasil = pantulan_iteratif(h0, e_val, h_min)
    pantulan_counts.append(len(hasil))

plt.plot(e_values, pantulan_counts, marker='o')
plt.xlabel("Koefisien Elastisitas (e)")
plt.ylabel("Jumlah Pantulan")
plt.title("Pengaruh koefisien (e) terhadap Jumlah Pantulan")
plt.grid(True)
plt.show()

h0_values = [200, 300, 500, 600]
iter_times = []
rek_times = []

for h0_val in h0_values:
    iter_times.append(
        ukur_waktu(pantulan_iteratif, h0_val, e, h_min)
    )
    rek_times.append(
        ukur_waktu(pantulan_rekursif, h0_val, e, h_min)
    )

plt.figure(figsize=(7, 5))
plt.plot(h0_values, iter_times, marker='o', label="Iteratif")
plt.plot(h0_values, rek_times, marker='x', linestyle='--', label="Rekursif")

plt.xlabel("Tinggi Awal (h₀)")
plt.ylabel("Waktu Eksekusi (detik)")
plt.title("Pengaruh Tinggi Awal (h₀) terhadap Waktu Eksekusi")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.ticklabel_format(style='plain', axis='y')
plt.show()