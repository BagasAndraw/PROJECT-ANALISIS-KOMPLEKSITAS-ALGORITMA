def pantulan_iteratif(h0, e, h_min):

    tinggi = h0
    hasil = []

    while tinggi >= h_min:
        hasil.append(tinggi)
        tinggi *= e

    return hasil

if __name__ == "__main__":

    h0 = 10.0
    e = 0.6
    h_min = 0.01

    hasil = pantulan_iteratif(h0, e, h_min)

    print("Jumlah pantulan (iteratif):", len(hasil))