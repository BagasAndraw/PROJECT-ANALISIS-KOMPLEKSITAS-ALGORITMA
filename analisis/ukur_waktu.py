import time
import matplotlib.pyplot as plt
import csv

from iteratif import pantulan_iteratif
from rekursif import pantulan_rekursif

# ===== PARAMETER =====
h0 = 0.0
e = 0.0
h_min = 0.0
REPEAT = 0


def ukur_waktu(func, *args, repeat=1000):
    """
    Mengukur waktu eksekusi rata-rata suatu fungsi
    """

def main():
    # SIMULASI
    hasil_iteratif = None
    hasil_rekursif = None

    # PENGUKURAN WAKTU 
    waktu_iteratif = None
    waktu_rekursif = None
    selisih = None

    # OUTPUT TERMINAL 
    print("=== HASIL ANALISIS (RATA-RATA) ===")

    # GRAFIK TINGGI PANTULAN 
    plt.figure()
    # TO DO: plot hasil iteratif & rekursif
    plt.show()

    #  GRAFIK WAKTU EKSEKUSI 
    plt.figure()
    # TO DO: plot perbandingan waktu
    plt.show()

    #  SIMPAN KE CSV 
    with open("hasil_pengukuran.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        # TO DO: tulis header
        # TO DO: tulis data


if __name__ == "__main__":
    main()
