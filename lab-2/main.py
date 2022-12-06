# Juan Dharmananda Khusuma
# 2206081521
# DDP E

from math import pi, ceil # Import function dari module math

# Meminta input dari user
nama = input("Nama: ")
n = float(input("Panjang Persegi Nametag (cm): "))
m = float(input("Panjang Trapesium Nametag (cm): "))
banyak_nametag = int(input("Banyak Nametag: "))

hc = 1/2 * pi * ( (n/2) ** 2 ) # Luas 1/2 Lingkaran
sg = 1/2 * n * n # Luas Segitiga
pr = n ** 2 # Luas Persegi
tr = n * (n + m) / 2 # Luas Trapesium

luas = hc + sg + pr + tr # Luas total, lalu round ke 2 digit di belakang koma 
total = luas * banyak_nametag # Luas total semua nametag
harga = ceil(total * 0.4 / 1000) * 1000 # Biaya yang diperlukan lalu di ceil ke 1000 terdekat

# Output 
print(f"Halo {nama}!, berikut informasi terkait nametag kamu: \n")
print(f"Luas 1 nametag: {round(luas, 2)} cm^2")
print(f"Luas total nametag: {round(total, 2)} cm^2")
print(f"Uang yang diperlukan: Rp.{harga} ")
