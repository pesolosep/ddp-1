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
                    # Menyimpan jenis menu pada iterasi ini
                    curr = line.replace("===", "")
                    # Menyimpan informasi menu dalam bentuk yang dapat dipilih bedasarkan nama ataupun kode
                    # Jenis menu dijadikan key
                    # value di set ke empty dict
                    token[curr] = {}

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
                    token[curr] = [*token[curr], (code, name, price, info)]
    except Exception as e:
        print(e)
        print("Daftar menu tidak valid, cek kembali menu.txt!")
        sys.exit(1)
    return token


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
            self, text="Kembali", bg="#4472C4", fg="white", width=20, command=self.destroy)
        self.next_btn = tk.Button(
            self, text="Lanjut", bg="#4472C4", fg="white", width=20, command=self.lanjut)
        self.back_btn.grid(column=0, row=1, padx=(30, 40))
        self.next_btn.grid(column=1, row=1)

        self.mainloop()

    def lanjut(self):
        Table(menu, self.nama.get(), self.master)


class TampilanMeja(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.list_meja = []
        self.render_meja()

    def meja_select(self, event):
        pass

    def warna_meja(self, num):
        return "#ccc"

    def update_nomor(self, *_):
        self.destroy()

    def render_meja(self, *_):
        self.container = tk.Frame(self)
        [btn.destroy for btn in self.list_meja]
        for num in meja:
            meja_btn = tk.Button(
                self.container, text=f"{num}", bg=self.warna_meja(num), width=10, fg="white")
            meja_btn.bind("<Button-1>", lambda event: self.meja_select(event))
            self.list_meja.append(meja_btn)
            meja_btn.grid(row=(num) % 5, column=(
                0 if num < 5 else 1), padx=(5, 5), pady=(5, 5))
        self.info_container = tk.Frame(self)
        self.info_label = tk.Label(
            self.info_container, text="Info", font="Arial 11 bold")
        self.info_1 = tk.Label(self.info_container, text="Merah: Terisi")
        self.info_2 = tk.Label(self.info_container, text="Abu-abu: Kosong")
        self.info_3 = tk.Label(self.info_container, text="Biru: Meja Anda")

        self.info_label.grid(row=0, column=0)
        self.info_1.grid(row=1, column=0)
        self.info_2.grid(row=2, column=0)
        self.info_3.grid(row=3, column=0)
        self.container.grid(row=1, column=0, padx=(
            40, 40), pady=(5, 5), columnspan=3)
        self.info_container.grid(row=2, column=0)


class SelesaiGunakanMeja(TampilanMeja):
    def __init__(self, master=None):
        super().__init__(master)

    def warna_meja(self, num):
        if meja[num] > -1:
            return "#f00"
        return "#bbb"

    def meja_select(self, event):
        if meja[int(event.widget["text"])] > -1:
            meja[int(event.widget["text"])] = -1
            self.destroy()

    def render_meja(self, *_):
        self.title = tk.Label(
            self, text="Silahkan klik meja kosong yang diinginkan:")
        self.title.grid(row=0, column=0, padx=(40, 40))
        return super().render_meja(*_)


class PilihMeja(TampilanMeja):
    def __init__(self, master=None):
        self.master = master
        self.curr = tk.IntVar(self.master, self.master.nomor_meja.get())
        self.curr.trace("w", self.render_meja)
        super().__init__(master)

    def update_nomor(self, *_):
        self.master.nomor_meja.set(self.curr.get())
        self.destroy()

    def warna_meja(self, num):
        if num == self.curr.get():
            return "#4472C4"
        elif meja[num] > -1:
            return "#f00"
        return "#bbb"

    def meja_select(self, event):
        if meja[int(event.widget["text"])] > -1:
            return

        self.curr.set(int(event.widget["text"]))

    def render_meja(self, *_):
        self.title = tk.Label(
            self, text="Silahkan klik meja kosong yang diinginkan:")
        self.title.grid(row=0, column=0, padx=(40, 40))
        super().render_meja(*_)
        self.back_btn = tk.Button(
            self, bg="#4472C4", text="Kembali", fg="#fff", command=self.destroy, width=20)
        self.next_btn = tk.Button(
            self, bg="#4472C4", fg="#fff", text="OK", command=self.update_nomor, width=20)
        self.back_btn.grid(row=3, column=0)
        self.next_btn.grid(row=3, column=1)


class Table(tk.Toplevel):
    def __init__(self, data, nama, master=None):
        super().__init__(master)
        self.data = data
        self.nama = nama
        self.total = 0
        self.int_var = []
        self.prices = []
        self.nomor_meja = tk.IntVar(self, self.get_available_table(meja))
        self.nomor_meja.trace("w", self.update_nomor_meja)
        self.generate_table()

    def update_nomor_meja(self, *_):
        self.nomor_meja_label["text"] = f"No Meja: {self.nomor_meja.get()}"

    # Mencari meja tersedia dengan nomor terkecil
    def get_available_table(self, table):
        min_val = 100  # Batas perbandingan
        for num in table:  # Algoritma minimum search dengan metode iterasi
            if table[num] == -1 and num < min_val:
                min_val = num
        return min_val  # jika ada meja yang tersedia maka hasilnya nomor meja minimum jika tidak maka hasilnya 100

    def generate_table(self):
        self.content = tk.Frame(self)
        self.nama_label = tk.Label(
            self.content, text=f"Nama pemesan: {self.nama}")
        self.nama_label.grid(row=0, column=0, pady=(0, 20))

        self.meja_container = tk.Frame(self.content)
        self.nomor_meja_label = tk.Label(
            self.meja_container, text=f"No Meja: {self.nomor_meja.get()}")
        self.ganti_nomor_btn = tk.Button(
            self.meja_container, text="Ubah", command=self.pilih_meja)
        self.nomor_meja_label.grid(row=0, column=0)
        self.ganti_nomor_btn.grid(row=0, column=1)
        self.meja_container.grid(row=0, column=3, columnspan=2)

        k = 3
        for key in self.data:
            label = tk.Label(self.content, text=key)
            label.grid(row=k, column=0)
            k += 1
            kode_label = tk.Entry(self.content, width=20, fg="black")
            nama_label = tk.Entry(self.content, width=20, fg="black")
            harga_label = tk.Entry(self.content, width=20, fg="black")
            kode_label.insert(tk.END, "Kode")
            kode_label.grid(row=k, column=0)
            kode_label['state'] = 'readonly'
            nama_label.insert(tk.END, "Nama")
            nama_label.grid(row=k, column=1)
            nama_label['state'] = 'readonly'
            harga_label.insert(tk.END, "Harga")
            harga_label.grid(row=k, column=2)
            harga_label['state'] = 'readonly'

            info_label = tk.Entry(self.content, width=20, fg="black")
            if key == "MEALS":
                info_label.insert(tk.END, "Kegurihan")
            elif key == "DRINKS":
                info_label.insert(tk.END, "Kemanisan")
            else:
                info_label.insert(tk.END, "Keviralan")
            info_label.grid(row=k, column=3)
            info_label['state'] = 'readonly'

            jumlah_label = tk.Entry(self.content, width=20, fg="black")
            jumlah_label.insert(tk.END, "Jumlah")
            jumlah_label.grid(row=k, column=4)
            jumlah_label['state'] = 'readonly'

            k += 1
            for i in range(len(self.data[key])):
                for j in range(len(self.data[key][0])):
                    entry = tk.Entry(self.content, width=20, fg='black')
                    entry.grid(row=k, column=j)
                    entry.insert(tk.END, self.data[key][i][j])
                    entry['state'] = 'readonly'

                # kolom paling kanan -> combobox
                values = tuple([k for k in range(10)])
                var = tk.IntVar()
                opsi_jumlah = ttk.Combobox(
                    self.content, values=values, textvariable=var)
                var.trace("w", self.update_total)
                self.int_var.append(var)
                self.prices.append(int(self.data[key][i][2]))
                opsi_jumlah.grid(
                    row=k, column=len(self.data[key][0]))
                k += 1

        self.total_label = tk.Label(
            self.content, text="Total harga: 0", font="Arial 12 bold")
        self.total_label.grid(row=k+1, column=4, pady=(40, 0))
        self.btn_container = tk.Frame(self)

        self.kembali_btn = tk.Button(
            self.btn_container, text="Kembali", fg="#fff", bg="#4472C4", command=self.destroy, width=20)
        self.ok_btn = tk.Button(self.btn_container, fg="#fff", text="OK",
                                bg="#4472C4", width=20, command=self.lanjut)
        self.kembali_btn.grid(row=0, column=0, padx=(5, 5))
        self.ok_btn.grid(row=0, column=1, padx=(5, 5))
        self.btn_container.grid(row=k+2, column=0, pady=(0, 40))

        self.content.grid(row=0, column=0, padx=(40, 40), pady=(40, 40))

    def lanjut(self):
        meja[self.nomor_meja.get()] = self.total
        self.destroy()

    def pilih_meja(self):
        PilihMeja(self)

    def update_total(self, *_):
        self.total = 0
        for i, var in enumerate(self.int_var):
            self.total += var.get() * self.prices[i]
        self.total_label["text"] = f"Total harga: {self.total}"


def main():
    global meja, menu
    meja = {i: -1 for i in range(10)}
    menu = parse_menu()

    # TODO mengolah data menu

    window = tk.Tk()
    cafe = Main(window)
    # Table(menu, window)
    window.mainloop()


if __name__ == '__main__':
    main()
