print("MISD - Validasi Password")

password = "Atu123!"

def cek_panjang(pw):
    return len(pw) >= 8

def cek_angka(pw):
    return any(char.isdigit() for char in pw)

def cek_huruf_besar(pw):
    return any(char.isupper() for char in pw)

hasil1 = cek_panjang(password)
hasil2 = cek_angka(password)
hasil3 = cek_huruf_besar(password)

print("Cek panjang:", hasil1)
print("Cek ada angka:", hasil2)
print("Cek huruf besar:", hasil3)

if hasil1 and hasil2 and hasil3:
    print("Password Valid")
else:
    print("Password Tidak Valid")
    