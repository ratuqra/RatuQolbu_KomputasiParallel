from multiprocessing import Process

def transfer():
    print("Memproses Transfer Uang...")

def tarik_tunai():
    print("Memproses Tarik Tunai...")

def cek_saldo():
    print("Memproses Cek Saldo...")

if __name__ == "__main__":
    p1 = Process(target=transfer)
    p2 = Process(target=tarik_tunai)
    p3 = Process(target=cek_saldo)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Semua transaksi selesai diproses.")
    