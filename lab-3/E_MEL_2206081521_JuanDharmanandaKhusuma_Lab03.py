print("Selamat Datang di Bunker Hacker!\n")

# Menerima input jumlah angka yang ingin di konversi
banyak_angka = int(
    input("Masukkan berapa kali konversi yang ingin dilakukan: ")
)

# Melakukan iterasi sebanyak jumlah angka yang ingin dikonversi
# lalu menanyakan user mengenai nilai desimal yang ingin diubah
# ke octal, lalu melakukan print hasil konversi ke console
for i in range(banyak_angka):
    # Menerima input nilai desimal
    dec = int((
        input(
            f"Masukkan angka ke-{i+1} yang ingin dikonversikan (dalam desimal):")
    ))
    # Variable yang akan menampung nilai octal
    oct_ = ""

    # Melakukan konversi dari desimal ke octal
    # mengumpulkan X % N (modulo) ke sebuah string
    # dari setiap iterasi, lalu melakukan X // N
    # (floor division) hingga angka X sama dengan 0.
    while dec > 0:
        oct_ += str(dec % 8)
        dec //= 8
    # Mengurutkan digit dengan melakukan reverse dengan string slice
    oct_ = oct_[::-1]
    print(f"Hasil konversi desimal ke basis 8 : {oct_}\n")

print("\nTerima kasih telah menggunakan Bunker Hacker!")
