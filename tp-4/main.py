# import modul
import tkinter as tk
import tkinter.ttk as ttk
import sys


def parse_menu():
    # Membuka dan memroses menu.txt serta melakukan validasi
    token = {}
    check = []  # untuk memastikan tidak ada kode atau nama menu yang duplikat
    curr = ""
    try:
        with open("./menu.txt", "r") as menu:
            for i, line in enumerate(menu):
                line = line.strip()
                if i == 0 and line[0:3] != "===":
                    raise Exception()
                if line[0:3] == "===":  # jika terdapat baris yang diawali ===, maka itu adalah jenis menu
                    # jika sudah terdapat dalam list check, maka string itu duplikat dan menu tidak valid
                    if token.get(line, None):
                        raise Exception()
                    curr = line  # Menyimpan jenis menu pada iterasi ini
                    # Menyimpan informasi menu dalam bentuk yang dapat dipilih bedasarkan nama ataupun kode
                    # Jenis menu dijadikan key
                    # value di set ke empty dict
                    token[line] = {}
                    if not token[line].get('codes', {}):
                        token[line]['codes'] = {}
                    if not token[line].get('names', {}):
                        token[line]['names'] = {}

                else:
                    # Jika bukan jenis menu, maka dilakukan splitting
                    # Jika hasil split menjadi 3 tidak berhasil maka menu tidak valid
                    code, name, price, info = line.split(";")
                    if name in check or code in check:  # jika nama ataupun kode ada dalam list check maka nama ataupun kode itu tidak unik
                        raise Exception()
                    # Menambahkan nama dan kode kedalam list check jika bukan duplikat
                    check = [*check, name, code]
                    # Memasukan data-data jika semua data sebelumnya valid
                    # apakah harga merupakan int atau bukan dapat divalidasi dengan fungsi int
                    token[curr]['codes'][code] = {
                        'name': name, 'price': int(price), 'info': int(info)}
                    token[curr]['names'][name] = {
                        'code': code, 'price': int(price), 'info': int(info)}
    except Exception as e:
        print(e)
        print("Daftar menu tidak valid, cek kembali menu.txt!")
        sys.exit(1)
    return token


def merge_menu(menu):  # Mengubah menu menjadi bentuk yang lebih mudah diproses
    merged_menu = {}
    for item in menu.values():
        # membuang layer pertama dari nested dict
        merged_menu = {**merged_menu, **item['names']}
    # hasil return merupakan {nama_menu: { kode:..., harga: ...}}
    return merged_menu

def get_available_table(table):  # Mencari meja tersedia dengan nomor terkecil
    min_val = 100  # Batas perbandingan
    for num in table:  # Algoritma minimum search dengan metode iterasi
        if table[num] == {} and num < min_val:
            min_val = num
    return min_val  # jika ada meja yang tersedia maka hasilnya nomor meja minimum jika tidak maka hasilnya 100


class Menu:
    def __init__(self, kode_menu, nama_menu, harga):
        self.kode_menu = kode_menu
        self.nama_menu = nama_menu
        self.harga = int(harga)


class Meals(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan


class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan


class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        # TODO handle info tambahan


class Main(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        button1 = tk.Button(self, text="Buat Pesanan", width=30,
                            command=self.buat_pesanan, bg="#4472C4", fg="white")
        button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30,
                            command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        button1.grid(row=0, column=0, padx=10, pady=40)
        button2.grid(row=1, column=0)

    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        SelesaiGunakanMeja(self.master)


class BuatPesanan(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.lbl_nama.grid(column=0, row=0, pady=(50, 80), padx=(30, 0))

        # TODO
        self.nama = tk.StringVar()
        self.input_nama = tk.Entry(self, textvariable=self.nama)
        self.input_nama.grid(column=1, row=0, pady=(50, 80))
        self.back_btn = tk.Button(
            self, text="Kembali", bg="#4472C4", fg="white", width=20)
        self.next_btn = tk.Button(
            self, text="Lanjut", bg="#4472C4", fg="white", width=20)
        self.back_btn.grid(column=0, row=1, padx=(30, 40))
        self.next_btn.grid(column=1, row=1)

        self.mainloop()


class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        self.lbl_command = tk.Label(
            self, text="Silakan klik meja yang selesai digunakan:")
        self.lbl_command.grid(column=0, row=0)

        # TODO

        self.mainloop()


def main():
    meja = {}
    menu = parse_menu()

    # TODO mengolah data menu

    window = tk.Tk()
    cafe = Main(window)
    window.mainloop()


if __name__ == '__main__':
    main()
