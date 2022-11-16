import math


user_input = ""
HARGA = 700
print("Selamat datang di Depot Minuman Dek Depe!")
print("==========================================")

# Menghitung volume balok


def v_balok(p, l, t):
    return p * l * t

# Menghitung volume kerucut


def v_kerucut(r, t):
    return 1/3 * math.pi * (r ** 2) * t

# Mencari volume dan meminta informasi ukuran dari string input user


def cari_volume(bangun_ruang):
    if bangun_ruang == "BALOK":
        p = float(input("Masukkan panjang balok : "))
        l = float(input("Masukkan lebar balok : "))
        t = float(input("Masukkan tinggi balok : "))
        return v_balok(p, l, t)
    else:
        r = float(input("Masukkan jari-jari kerucut : "))
        t = float(input("Masukkan tinggi kerucut : "))
        return v_kerucut(r, t)


v = 0
# Loop meminta input galon ke user
while True:
    user_input = input(
        "Masukkan bentuk galon yang diinginkan (STOP untuk berhenti): ").strip()
    # Jika input STOP, break dari loop
    if user_input == "STOP":
        break

    # Jika input valid, tambahkan volume bangun tersebut ke variable v
    if user_input == "BALOK" or user_input == "KERUCUT":
        v += cari_volume(user_input)

    # Jika input tidak valid, kirim pesan ke user lalu loop kembali
    else:
        print("Input tidak benar, masukkan kembali\n")

# Print output ke user
print("====================================================")
if v == 0:
    print("Anda tidak memasukkan input satupun :(")
else:
    print(f"Total volume air yang dikeluarkan adalah : {v:.2f}")
    print(f"Total harga yang harus dibayar adalah : Rp{v*HARGA:.2f}")
print("\nTerima kasih telah menggunakan Depot Air Minum Dek Depe")
print("====================================================")
