print("SISD - Menghitung Faktorial")

n = 5
hasil = 1

for i in range(1, n+1):
    hasil *= i
    print("Langkah", i, "=", hasil)

print("Faktorial =", hasil)