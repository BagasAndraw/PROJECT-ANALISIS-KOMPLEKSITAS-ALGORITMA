def pantulan_rekursif(tinggi, e, h_min, hasil=None):

    if hasil is None:
        hasil = []

    if tinggi < h_min:
        return hasil

    hasil.append(tinggi)
    return pantulan_rekursif(tinggi * e, e, h_min, hasil)


if __name__ == "__main__":
    h0 = 10.0
    e = 0.6
    h_min = 0.01

    hasil = pantulan_rekursif(h0, e, h_min)
    print("Jumlah pantulan (rekursif):", len(hasil))
