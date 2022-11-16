data_mhs = {}  # Dictionary dat mahasiswa

print("Selamat datang di program Mengenal Angkatan!")
print("===========================================")
print("Masukkan identitas mahasiswa:")

# Menerima input data dan tanggal lahir mahasiswa
while True:
    user_input = input()
    if user_input == "STOP":  # Jika input STOP maka loop berhenti
        break
    # Memisahkan tanggal lahir dengan nama dan npm
    nama_npm, tgl = user_input.strip().split("-")
    nama, npm = nama_npm.split()  # Mengambil nama dan npm
    bulan = tgl.split()[1]  # Mengambil bulan dari tanggal lahir
    # Mengambil data dari dictionary
    # Disini key dari dict adalah bulan lahir dan value nya adalah set tuple dalam bentuk (nama, npm)
    # Jika key belum ada maka di initialize ke empty set
    data_mhs[bulan] = {(nama, npm), *data_mhs.get(bulan, set())}
print("\n")

# Menerima input search bulan lahir
while True:
    user_input = input("Cari mahasiswa berdasarkan bulan: ")
    if user_input == "STOP":  # Jika input STOP maka loop berhenti
        break
    print("================= Hasil ================")  # Print hasil search
    # Mengambil data bedasarkan bulan, jika tidak ada maka di initialize ke empty set
    data = data_mhs.get(user_input, {})
    if not data:
        # Jika user tidak ditemukan
        print("Tidak ditemukan mahasiswa dan NPM yang lahir di bulan oktober.")
    # Mengubah agar tidak ada nama yang duplikat dan nama case insensitive
    set_nama = {mhs[0].title() for mhs in data}
    # Mengumpulkan semua npm dan memastikan tidak ada npm yang duplikat
    set_npm = {mhs[1] for mhs in data}
    # Melakukan printing semua nama yang ditemukan
    print(f"Terdapat {len(set_nama)} nama yang lahir di bulan {user_input}:")
    for nama in set_nama:
        print(f"- {nama}")
    # Melakukan printing semua npm yang ditemukan
    print(f"Terdapat {len(set_npm)} NPM yang lahir di bulan {user_input}:")
    for npm in set_npm:
        print(f"- {npm}")
    print("\n")

print("\nTerima kasih telah menggunakan program ini, semangat PMB-nya!")
