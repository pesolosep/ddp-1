import tkinter as tk
import tkinter.messagebox as tkmsg


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Karung Ajaib")
        self.pack()
        self.create_widgets()

    # TODO : Lengkapi Binding Event Handler dengan buttons yang ada
    def create_widgets(self):
        self.label = tk.Label(self,
                              text='Selamat datang Dek Depe di Karung Ajaib. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_karung = tk.Button(self,
                                                 text="LIHAT DAFTAR KARUNG",
                                                 command=self.popup_lihat_karung)  # membuka popup lihat karung
        self.btn_masukkan_item = tk.Button(self,
                                           text="MASUKKAN ITEM",
                                           command=self.popup_add_item)  # membuka popup masukan item
        self.btn_keluarkan_item = tk.Button(self,
                                            text="KELUARKAN ITEM",
                                            command=self.popup_keluarkan_item)  # membuka popup keluarkan item
        self.btn_exit = tk.Button(self,
                                  text="EXIT",
                                  command=self.master.destroy)  # menutup window

        self.label.pack()
        self.btn_lihat_daftar_karung.pack()
        self.btn_masukkan_item.pack()
        self.btn_keluarkan_item.pack()
        self.btn_exit.pack()

    # semua item dalam karung
    def popup_lihat_karung(self):
        PopupLihatKarung(self.master)

    # menu masukkan item
    def popup_add_item(self):
        PopupAddItem(self.master)

    # menu keluarkan item
    def popup_keluarkan_item(self):
        PopupKeluarkanItem(self.master)


class PopupLihatKarung(object):
    def __init__(self, master):
        self.main_window = tk.Toplevel()
        self.main_window.geometry("280x100")
        self.main_window.wm_title("Lihat Karung")

        self.title = tk.Label(self.main_window, text='Daftar Karung Ajaib')
        self.nama = tk.Label(self.main_window, text='Nama Item')

        self.title.pack()
        self.nama.pack()

        # TODO: Tampilkan halaman Lihat Karung Ajaib
        # looping terhadap semua item dalam karung
        for i, j in enumerate(sorted(list(item_set))):
            # setiap item string akan menjadi label yang di pack ke window
            item = tk.Label(self.main_window, text=f"{i+1}.{j}")
            item.pack()

        self.exit_button = tk.Button(
            self.main_window, text="EXIT", command=self.main_window.destroy)
        self.exit_button.pack()

# Class Masukkan Item


class PopupAddItem(object):
    def __init__(self, master):
        self.main_window = tk.Toplevel()
        self.main_window.wm_title("Masukkan item")
        self.main_window.geometry("280x100")

        # TODO: Create Widget untuk tampilan Masukkan Item
        self.label = tk.Label(self.main_window, text="Input Masukan Item")
        self.item_input = tk.StringVar()

        self.input_label = tk.Label(self.main_window, text="Nama Item")

        self.input = tk.Entry(
            self.main_window, textvariable=self.item_input)

        self.submit_button = tk.Button(
            self.main_window, text='Masukkan', command=self.masukkan_item)
        self.input_label.grid(row=1, column=0)
        self.input.grid(row=1, column=1)
        self.label.grid(row=0, column=1)
        self.submit_button.grid(row=2, column=1)

    def masukkan_item(self):
        # TODO: Create Method untuk Masukkan Item
        item = self.item_input.get()  # mengambil input dari stringvar
        if item not in item_set:  # jika item tidak ada dalam set, tambahkan dan tunjukan pesan berhasil
            item_set.add(self.item_input.get())
            tkmsg.showinfo("Berhasil!", f"Berhasil memasukan item {item}")
        else:  # jika item sudah ada maka tampilkan error
            tkmsg.showwarning(
                "ItemHasFound", f"Item dengan nama {item} sudah ada di dalam KarungAjaib.\nItem {item} tidak bisa dimasukan lagi")
        self.main_window.destroy()


# Class Keluarkan Item
class PopupKeluarkanItem(object):

    def __init__(self, master):
        self.main_window = tk.Toplevel()
        self.main_window.wm_title("Keluarkan item")
        self.main_window.geometry("280x100")

        # TODO: Create Widget untuk tampilan Keluarkan Item

        self.label = tk.Label(self.main_window, text="Input Keluarkan Item")
        self.input_label = tk.Label(self.main_window, text="Nama Item")
        self.input_item = tk.StringVar()
        self.input = tk.Entry(self.main_window, textvariable=self.input_item)

        self.submit_button = tk.Button(
            self.main_window, text='Ambil', command=self.keluarkan_item)

        self.input_label.grid(row=1, column=0)
        self.input.grid(row=1, column=1)
        self.label.grid(row=0, column=1)
        self.submit_button.grid(row=2, column=1)

    def keluarkan_item(self):
        # TODO: Create Method untuk Keluarkan Item
        item = self.input_item.get()  # mengambil input dari stringvar
        if item in item_set:
            # jika item ada, maka buang item dari set, lalu tampilkan pesan berhasil
            item_set.remove(item)
            tkmsg.showinfo("Berhasil!", f"Berhasil mengeluarkan item {item}.")
        else:  # jika tidak tampilkan error
            tkmsg.showwarning(
                "ItemNotFound", f"Item dengan nama {item} tidak ditemukan di dalam KarungAjaib.")
        self.main_window.destroy()


item_set = set()
if __name__ == "__main__":
    root = tk.Tk()
    m = MainWindow(root)
    root.mainloop()
