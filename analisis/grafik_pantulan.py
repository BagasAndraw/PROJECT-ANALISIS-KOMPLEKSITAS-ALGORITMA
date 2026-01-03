import matplotlib.pyplot as plt

from iteratif import pantulan_iteratif
from rekursif import pantulan_rekursif
from ukur_waktu import ukur_waktu

# PARAMETER GLOBAL
h_min = 0.0
e = 0.0


def eksperimen_jumlah_pantulan():
    """
    Eksperimen 1:
    Pengaruh koefisien elastisitas (e) terhadap jumlah pantulan
    """
    h0 = 0
    e_values = []
    pantulan_counts = []

    # TODO: loop perhitungan jumlah pantulan

    # TODO: visualisasi grafik
    plt.figure()
    plt.show()


def eksperimen_waktu_eksekusi():
    """
    Eksperimen 2:
    Pengaruh tinggi awal (h0) terhadap waktu eksekusi
    """
    h0_values = []
    iter_times = []
    rek_times = []

    # TO DO: loop pengukuran waktu iteratif & rekursif

    # TO DO: visualisasi grafik
    plt.figure()
    plt.show()


def main():
    eksperimen_jumlah_pantulan()
    eksperimen_waktu_eksekusi()


if __name__ == "__main__":
    main()
