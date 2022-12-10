# import modul
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg
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
    except Exception:
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

    # Mencari meja tersedia dengan nomor terkecil
    def get_available_table(self, table):
        min_val = 100  # Batas perbandingan
        for num in table:  # Algoritma minimum search dengan metode iterasi
            if table[num] == -1 and num < min_val:
                min_val = num
        return min_val  # jika ada meja yang tersedia maka hasilnya nomor meja minimum jika tidak maka hasilnya 100

    def lanjut(self):
        nomor_meja = self.get_available_table(meja)
        for val in meja.values():
            if type(val) == int:
                continue

            if self.nama.get() in val:
                tkmsg.showinfo(title="Nama telah digunakan",
                               message=f"Mohon maaf, nama {self.nama.get()} telah digunakan untuk memesan meja.")
                return self.destroy()
        if nomor_meja == 100:
            tkmsg.showinfo(
                title="Meja Penuh", message="Mohon maaf, meja sedang penuh. Silakan datang kembali di lain kesempatan.")
            return self.destroy()
        Table(menu, self.nama.get(), self)

# Abstract class untuk membentuk tabel pilihan meja
# pada buat pesanan dan selesai menggunakan meja


class TampilanMeja(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.list_meja = []
        self.render_meja()

    def meja_select(self, event):  # handling ketika meja dipilih
        pass

    def warna_meja(self, num):  # menentukan warna dari tombol meja
        return "#ccc"

    def update_nomor(self, *_):  # handling ketika user menekan tombol meja lain
        self.destroy()

    def render_meja(self, *_):
        # container untuk semua widget dalam layar agar dapat diberi padding secara keseluruhan
        self.container = tk.Frame(self)
        # setiap kali re-render, maka tombol dan widget sebelumnya akan di destroy dahulu
        [btn.destroy for btn in self.list_meja]
        self.list_meja = []
        for num in meja:
            # buat tombol meja
            meja_btn = tk.Button(
                self.container, text=f"{num}", bg=self.warna_meja(num), width=10, fg="white")
            # jika tombol ditekan maka akan di handle
            meja_btn.bind("<Button-1>", lambda event: self.meja_select(event))
            self.list_meja.append(meja_btn)
            # membuat tampilan meja yang dibagi menjadi 2 column (0-4) dan (5-9)
            meja_btn.grid(row=(num) % 5, column=(
                0 if num < 5 else 1), padx=(5, 5), pady=(5, 5))
        # render ke layar
        self.container.grid(row=1, column=0, padx=(
            40, 40), pady=(5, 20), columnspan=3)


class TablePesanan(tk.Toplevel):
    def __init__(self, num, data, master):
        super().__init__(master)
        self.num = num  # nomor meja yang ditampilkan
        self.data = data  # data menu
        self.generate_table()

    # menghasilkan table yang akan ditampilkan ke layar
    def generate_table(self):
        # sebagai container semua konten dalam layar agar dapat dengan mudah diberi padding bersama sama
        self.content = tk.Frame(self)
        # nama pemesan
        self.nama_label = tk.Label(
            self.content, text=f"Nama pemesan: {meja[self.num]['nama']}")
        self.nama_label.grid(row=0, column=0, pady=(0, 20))

        # nomor meja yang sedang ditampilkan
        self.nomor_meja_label = tk.Label(
            self.content, text=f"No Meja: {self.num}")
        self.nomor_meja_label.grid(row=0, column=3, columnspan=2)

        k = 3  # untuk mengatur posisi vertikal dari widget di table
        x = 0  # untuk memilih jumlah pesanan yang tepat dengan baris yang ditampilkan
        for key in self.data:
            # nama kategori menu
            label = tk.Label(self.content, text=key)
            label.grid(row=k, column=0)
            k += 1

            # menampikan header dari table beserta nama dari semua kolom
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
            # menampilkan semua data menu pada baris baris selanjutnya
            for i in range(len(self.data[key])):
                for j in range(len(self.data[key][0])):
                    entry = tk.Entry(self.content, width=20, fg='black')
                    entry.grid(row=k, column=j)
                    # menambil data dari list menu pada kategori tertentu
                    entry.insert(tk.END, self.data[key][i][j])
                    entry['state'] = 'readonly'
                x += 1

                # memasukan jumlah pesanan dari masing masing menu
                jumlah = tk.Entry(self.content, width=20, fg="black")
                jumlah.insert(tk.END, meja[self.num]
                              ["pesanan"][x-1])
                jumlah.grid(
                    row=k, column=len(self.data[key][0]))
                k += 1

        # menampilkan total harga yang harus dibayar
        self.total_label = tk.Label(
            self.content, text=f"Total harga: {meja[self.num]['total']}", font="Arial 12 bold")
        self.total_label.grid(row=k+1, column=4, pady=(40, 0))
        self.btn_container = tk.Frame(self)

        # tombol kembali yang akan menutup window ini
        self.kembali_btn = tk.Button(
            self.btn_container, text="Kembali", fg="#fff", bg="#4472C4", command=self.destroy, width=20)
        # tombol konfirmasi selesai menggunakan meja
        self.ok_btn = tk.Button(self.btn_container, fg="#fff", text="OK",
                                bg="#4472C4", width=20, command=self.lanjut)
        self.kembali_btn.grid(row=0, column=0, padx=(5, 5))
        self.ok_btn.grid(row=0, column=1, padx=(5, 5))
        self.btn_container.grid(row=k+2, column=0, pady=(0, 40))

        self.content.grid(row=0, column=0, padx=(40, 40), pady=(40, 40))

    # jika selesai menggunakan meja
    def lanjut(self, *_):
        meja[self.num] = -1  # set nomor meja sekarang ke -1
        # -1 adalah nilai yang mengindikasikan kalau meja itu kosong
        self.master.render_meja()  # render ulang display tampilan pilih meja
        self.destroy()  # tutup window ini


class SelesaiGunakanMeja(TampilanMeja):
    def __init__(self, master=None):
        super().__init__(master)

    def warna_meja(self, num):  # memilih warna dari tombol meja
        if meja[num] != -1:  # merah jika tidak bernilai -1 yaitu jika tidak kosong
            return "#f00"
        return "#bbb"  # jika tidak return warna abu abu

    def meja_select(self, event):
        # cek jika meja itu kosong atau tidak
        # jika tidak kosong yaitu tidak bernilai -1 maka buka window table pesanan
        if meja[int(event.widget["text"])] != -1:
            # masukan nomor meja dan data data yang diperlukan
            TablePesanan(int(event.widget["text"]), menu, self)

    def render_meja(self, *_):
        # menambahkan judul
        self.title = tk.Label(
            self, text="Silahkan klik meja kosong yang diinginkan:")
        self.title.grid(row=0, column=0, padx=(40, 40), pady=(20, 20))
        # menampilkan tampilan pilih meja
        super().render_meja(*_)
        # menambahkan info / legend
        self.info_container = tk.Frame(self)
        self.info_label = tk.Label(
            self.info_container, text="Info", font="Arial 11 bold")
        self.info_1 = tk.Label(self.info_container, text="Merah: Terisi")
        self.info_2 = tk.Label(self.info_container, text="Abu-abu: Kosong")
        self.info_label.grid(row=0, column=0)
        self.info_1.grid(row=1, column=0)
        self.info_2.grid(row=2, column=0)
        self.info_container.grid(row=2, column=0)
        # tombol untuk kembali yang akan menutup window ini
        self.back_btn = tk.Button(
            self, bg="#4472C4", fg="#fff", text="Kembali", command=self.destroy, width=20)
        self.back_btn.grid(row=3, column=0, pady=(40, 20))


class PilihMeja(TampilanMeja):
    def __init__(self, master=None):
        self.master = master
        # mengingat nomor meja berapa yang sekarang dipilih user
        self.curr = tk.IntVar(self.master, self.master.nomor_meja.get())
        # setiap kali nomor meja yang dipilih user berubah maka render ulang tampilan pilih meja
        self.curr.trace("w", self.render_meja)
        super().__init__(master)

    # jika user telah mengonfirmasi maka IntVar nomor meja dari master yakni class Table akan di update
    def update_nomor(self, *_):
        self.master.nomor_meja.set(self.curr.get())
        self.destroy()  # tutup window

    # mengembalikan warna biru jika nomor meja sesuai dengan yang sekarang dipilih user
    def warna_meja(self, num):
        if num == self.curr.get():
            return "#4472C4"
        elif meja[num] != -1:  # merah jika tidak kosong atau tidak bernilai -1
            return "#f00"
        return "#bbb"  # abu abu jika kosong

    def meja_select(self, event):  # jika meja sedang di klik
        # jika tidak kosong maka tidak dapat dipilih
        if meja[int(event.widget["text"])] != -1:
            return

        # jika kosong maka self.curr akan di update
        self.curr.set(int(event.widget["text"]))

    def render_meja(self, *_):
        #  penambahan judul
        self.title = tk.Label(
            self, text="Silahkan klik meja kosong yang diinginkan:")
        self.title.grid(row=0, column=0, padx=(40, 40), pady=(20, 20))
        # tampilan pilih meja
        super().render_meja(*_)
        # informasi dan legend
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

        self.info_container.grid(row=2, column=0)
        self.btn_container = tk.Frame(self)
        # tombol untuk kembali yang akan menutup window
        self.back_btn = tk.Button(
            self.btn_container, bg="#4472C4", text="Kembali", fg="#fff", command=self.destroy, width=20)
        # tombol konfirmasi yang akan memanggil function update nomor yang akan merubah nomor meja di class Table
        self.next_btn = tk.Button(
            self.btn_container, bg="#4472C4", fg="#fff", text="OK", command=self.update_nomor, width=20)
        self.back_btn.grid(row=0, column=0, padx=(0, 5))
        self.next_btn.grid(row=0, column=1, padx=(5, 0))
        self.btn_container.grid(row=3, column=0, padx=(40, 40), pady=(20, 20))


class Table(tk.Toplevel):
    def __init__(self, data, nama, master=None):
        super().__init__(master)
        self.data = data  # menyimpan informasi menu
        self.nama = nama  # menyimpan nama pemesan
        self.total = 0  # total harga pesanna
        self.int_var = []  # menyimpan semua intvar dari selection combobox
        self.prices = []  # menyimpan semua harga dari menu
        self.nomor_meja = tk.IntVar(
            self, self.master.get_available_table(meja))  # membuat intvar dengan nilai awal, nomor meja kosong terkecil
        # jika nomor meja berubah maka nilai text pada label akan diubah pula
        self.nomor_meja.trace("w", self.update_nomor_meja)
        self.generate_table()  # tampikan table di layar

    def update_nomor_meja(self, *_):
        # ubah isi text pada label dengan nomor meja baru
        self.nomor_meja_label["text"] = f"No Meja: {self.nomor_meja.get()}"

    def generate_table(self):
        self.content = tk.Frame(self)
        # tampilkan informasi tentang nama pemesan, nomor meja, serta tombol untuk mengubah nomor meja
        self.nama_label = tk.Label(
            self.content, text=f"Nama pemesan: {self.nama}")
        self.nama_label.grid(row=0, column=0, pady=(0, 20))

        self.meja_container = tk.Frame(self.content)
        self.nomor_meja_label = tk.Label(
            self.meja_container, text=f"No Meja: {self.nomor_meja.get()}")
        # jika ditekan akan membuka window pilih meja
        self.ganti_nomor_btn = tk.Button(
            self.meja_container, text="Ubah", command=self.pilih_meja, bg="#4472C4", fg="#fff", width=10)
        self.nomor_meja_label.grid(row=0, column=0)
        self.ganti_nomor_btn.grid(row=0, column=1, padx=(5, 0))
        self.meja_container.grid(row=0, column=3, columnspan=2)

        k = 3  # tracking posisi vertikal widget
        for key in self.data:
            label = tk.Label(self.content, text=key)
            label.grid(row=k, column=0)
            k += 1
            # header table dengan isi nama nama kolom
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
            # menampilkan isi data dari setiap kolom
            for i in range(len(self.data[key])):
                for j in range(len(self.data[key][0])):
                    entry = tk.Entry(self.content, width=20, fg='black')
                    entry.grid(row=k, column=j)
                    entry.insert(tk.END, self.data[key][i][j])
                    entry['state'] = 'readonly'

                # kolom paling kanan -> combobox
                # membuat opsi combobox 0-9
                values = tuple([k for k in range(10)])
                var = tk.IntVar()  # intvar untuk menyimpan nilai combobox
                opsi_jumlah = ttk.Combobox(  # binding intvar dengan combobox
                    self.content, values=values, textvariable=var)
                # jika terjadi perubahan pada var maka total akan di update juga
                var.trace("w", self.update_total)
                # simpan intvar di instance variable self.int_var
                self.int_var.append(var)
                # simpan juga harga dari menu tersebut agar dapat dihitung harga total pesanan
                self.prices.append(int(self.data[key][i][2]))
                opsi_jumlah.grid(
                    row=k, column=len(self.data[key][0]))
                k += 1

        # display total harga pesanan
        self.total_label = tk.Label(
            self.content, text="Total harga: 0", font="Arial 12 bold")
        self.total_label.grid(row=k+1, column=4, pady=(40, 0))
        self.btn_container = tk.Frame(self)

        # tombol untuk kembali yang akan menutup window ketika ditekan
        self.kembali_btn = tk.Button(
            self.btn_container, text="Kembali", fg="#fff", bg="#4472C4", command=self.destroy, width=20)
        # tombol konfirmasi yang akan mengupdate data meja dengan nama dan pesanan serta total harga pesanan pengguna
        self.ok_btn = tk.Button(self.btn_container, fg="#fff", text="OK",
                                bg="#4472C4", width=20, command=self.lanjut)
        self.kembali_btn.grid(row=0, column=0, padx=(5, 5))
        self.ok_btn.grid(row=0, column=1, padx=(5, 5))
        self.btn_container.grid(row=k+2, column=0, pady=(0, 40))

        self.content.grid(row=0, column=0, padx=(40, 40), pady=(40, 40))

    def lanjut(self):
        # set data pada nomor meja tertentu menjadi data nama, total harga pesanan serta list jumlah pesanan per menu
        meja[self.nomor_meja.get()] = {"nama": self.nama, "total": self.total, "pesanan": [
            var.get() for var in self.int_var]}
        self.destroy()  # lalu tutup window ini dan window sebelumnya
        self.master.destroy()

    # buka window class pilih meja
    def pilih_meja(self):
        PilihMeja(self)

    # mengubah text pada total pesanna
    def update_total(self, *_):
        self.total = 0  # reset total ke 0
        # lalu loop semua intvar dan kalikan dengan harga masing masing menu
        for i, var in enumerate(self.int_var):
            self.total += var.get() * self.prices[i]
        # ubah text pada label
        self.total_label["text"] = f"Total harga: {self.total}"


def main():
    # membuat menu dan meja menjadi global variable sehingga dapat diakses oleh semua class
    global meja, menu
    meja = {i: -1 for i in range(10)}  # data semua meja
    menu = parse_menu()  # data menu dari menu.txt
    window = tk.Tk()  # membuat main window root
    # buat main window dari aplikasi
    Main(window)
    window.mainloop()  # jalankan loop program


# entry point program
if __name__ == '__main__':
    main()
