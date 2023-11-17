# Contoh penggunaan package rumus untuk menghitung luas trapesium

from rumus import trapesium

# Input panjang alas, atas, dan tinggi dari pengguna
alas = float(input("Masukkan panjang alas trapesium: "))
atas = float(input("Masukkan panjang atas trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

# Hitung luas trapesium menggunakan fungsi dari package
luas = trapesium.luas_trapesium(alas, atas, tinggi)

# Tampilkan hasil
print("Luas trapesium adalah:", luas)
