print("Selamat Datang di Pacil Mart!")
try:
    # Mencoba membaca file dari input user
    file_path = input("Masukan nama file input: ")
    file = open(file_path, "r")
    # Menyimpan lines dari file
    lines = file.readlines()
    # Menghandle kasus ketika file kosong
    if len(lines) == 0:
        print("File input ada tapi kosong")
    # Jika file ada, print output
    else:
        # Print header dari output
        print("\nBerikut adalah daftar belanjaanmu: \n")
        print("Nama Barang |  Jumlah| Kembalian")
        print("—-------------------------------")
        # Print barang, jumlah, dan kembalian
        for line in lines:
            nama_barang, uang, harga = line.strip().split()
            jumlah = int(uang) // int(harga)
            kembalian = int(uang) - (int(harga) * jumlah)
            print(f"{nama_barang:<12}|{jumlah:>8}|{kembalian:>10}")
        print("\nTerima kasih sudah belanja di Pacil Mart!")
    # Menutup file
    file.close()

except FileNotFoundError:
    print("File tidak tersedia")
