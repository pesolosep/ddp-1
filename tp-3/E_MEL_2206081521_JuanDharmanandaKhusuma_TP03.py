import sys

# Menyimpan pesanan pada suatu nomor meja
table = {(i+1): {} for i in range(10)}
# Menyimpan nama pengunjung yang duduk pada suatu nomor meja
names = {(i+1): {} for i in range(10)}


# Melakukan formating angka menjadi nominal rupiah, dengan pemisah ribuan titik
def format_money(amount):
    return f"Rp{amount:,}".replace(",", ".")


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
                    code, name, price = line.split(";")
                    if name in check or code in check:  # jika nama ataupun kode ada dalam list check maka nama ataupun kode itu tidak unik
                        raise Exception()
                    # Menambahkan nama dan kode kedalam list check jika bukan duplikat
                    check = [*check, name, code]
                    # Memasukan data-data jika semua data sebelumnya valid
                    # apakah harga merupakan int atau bukan dapat divalidasi dengan fungsi int
                    token[curr]['codes'][code] = {
                        'name': name, 'price': int(price)}
                    token[curr]['names'][name] = {
                        'code': code, 'price': int(price)}
    except Exception as e:
        print("Daftar menu tidak valid, cek kembali menu.txt!")
        sys.exit(1)
    return token

# Melakukan printing pada semua menu yang tersedia


def print_menu(menu):
    print("Berikut ini adalah menu yang kami sediakan:")
    for menu_type in menu:
        # membuang === dari jenis menu
        print(f"{menu_type.replace('===', '')}:")
        for key in menu[menu_type]['codes']:
            data = menu[menu_type]['codes']
            print(
                f"{key} {data[key]['name']}, {format_money(data[key]['price'])}")  # printing kode, nama, dan harga menu
    print()


def merge_menu(menu):  # Mengubah menu menjadi bentuk yang lebih mudah diproses
    merged_menu = {}
    for item in menu.values():
        # membuang layer pertama dari nested dict
        merged_menu = {**merged_menu, **item['names']}
    # hasil return merupakan {nama_menu: { kode:..., harga: ...}}
    return merged_menu


def get_available_table():  # Mencari meja tersedia dengan nomor terkecil
    min_val = 100  # Batas perbandingan
    for num in table:  # Algoritma minimum search dengan metode iterasi
        if table[num] == {} and num < min_val:
            min_val = num
    return min_val  # jika ada meja yang tersedia maka hasilnya nomor meja minimum jika tidak maka hasilnya 100


def display_order(menu, ordered):  # menunjukan hasil pesanan
    print("\nBerikut adalah pesanan anda:")
    merged_menu = merge_menu(menu)
    total = 0
    for key in ordered:
        # menghitung harga total suatu item pesanan
        price = merged_menu[key]['price'] * ordered[key]
        total += price  # menghitung total
        print(
            f"{key} {ordered[key]} buah, total Rp{format_money(price)}")  # print informasi pesanan
    print(f"\nTotal pesanan: {format_money(total)}")  # Printing total


def assign_table(ordered, name):  # Menempatkan user pada suatu meja
    table_num = get_available_table()  # Mengambil meja tersedia
    if table_num < 11:  # Mengecek jika ada meja yang tersedia
        names[table_num] = name  # set nama user ke nomor meja
        table[table_num] = ordered  # set pesanan ke nomor meja
        print(
            f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {table_num}. Terima kasih.")
    else:  # handle jika meja penuh
        print("Mohon maaf meja sudah penuh, silakan kembali nanti.")
    print("\n---")


def select_menu(menu):  # Mwmilih menu makanan
    ordered = {}
    prev_order = ""
    while True:
        if prev_order:  # jika sudah ada pesanan sebelumnya yang berhasil
            print(
                f"Berhasil memesan {prev_order}. ", end="")
        order_input = input("Masukkan menu yang ingin Anda pesan: ")
        if order_input == "SELESAI":  # break jika input nya SELESAI
            break
        for listing in menu.values():  # Jika ada dalam menu maka tambahkan ke orderer
            if order_input in listing['codes']:
                ordered[listing['codes'][order_input]['name']] = ordered.get(
                    listing['codes'][order_input]['name'], 0) + 1
                prev_order = listing['codes'][order_input]['name']
                break
            if order_input in listing['names']:
                ordered[order_input] = ordered.get(order_input, 0) + 1
                prev_order = order_input
                break
        else:  # Jika tidak maka print error
            print(f"Menu {order_input} tidak ditemukan. ", end="")
            prev_order = ""
    display_order(menu, ordered)  # print hasil pesanan
    return ordered


def add_order(menu, ordered):  # fungsi implementasi fitur TAMBAH PESANAN
    menu_input = input("Menu apa yang ingin Anda pesan: ")
    menu_name = ""
    for listing in menu.values():  # Cek jika pesanan ada di menu
        if menu_input in listing['codes']:
            prev_order = listing['codes'][menu_input]['name']
            menu_name = prev_order
            break
        if menu_input in listing['names']:
            prev_order = menu_input
            menu_name = prev_order
            break
    else:  # Handle jika tidak ditemukan
        print(f"Menu {menu_input} tidak ditemukan! ", end=" ")
        return ordered
    # if ordered.get(menu_name, 0) != 0:
    # Jika ditemukan tambahkan ke pesanan
    ordered[menu_name] = ordered.get(menu_name, 0) + 1
    print(f"Berhasil memesan {menu_name}.", end=" ")
    # else:
    # print(f"Menu {menu_input} tidak ditemukan! ", end=" ")
    return ordered


def change_amount(menu, ordered):  # fungsi implementasi fitur GANTI JUMLAH
    menu_input = input("Menu apa yang ingin Anda ganti jumlahnya: ")
    menu_name = ""
    try:  # cek jika terdapat di menu
        for listing in menu.values():
            if menu_input in listing['codes']:
                prev_order = listing['codes'][menu_input]['name']
                menu_name = prev_order
                break
            if menu_input in listing['names']:
                prev_order = menu_input
                menu_name = prev_order
                break
        else:
            print(f"Menu {menu_input} tidak ditemukan! ", end="")
            return ordered
        if not ordered.get(menu_name, None):  # cek jika terdapat di pesanan sebelumnya
            print(f"Menu {menu_input} tidak Anda pesan sebelumnya. ", end="")
            prev_order = ""
        else:
            # ganti jumlah pesanan
            amount = int(input("Masukkan jumlah pesanan yang baru: "))
            ordered[menu_name] = amount
            if amount <= 0:  # jika nol atau kurang maka input tidak valid
                raise ValueError
            print(
                f"Berhasil mengubah pesanan {menu_name} {amount} buah.", end="")
    except (ValueError, TypeError):
        print("Jumlah harus bilangan positif.")
    finally:
        return ordered


def delete_order(menu, ordered):
    menu_input = input("Menu apa yang ingin Anda hapus dari pesanan: ")

    for listing in menu.values():  # cek jika input ada dalam menu
        if menu_input in listing['codes']:
            prev_order = listing['codes'][menu_input]['name']
            menu_name = prev_order
            break
        if menu_input in listing['names']:
            prev_order = menu_input
            menu_name = prev_order
            break
    else:
        print(f"Menu {menu_input} tidak ditemukan! ", end="")
        return ordered
    if not ordered.get(menu_name, None):  # cek jika ada pada pesanan sebelumnya
        print(f"Menu {menu_input} tidak Anda pesan sebelumnya. ", end="")
        prev_order = ""
    else:
        print(
            f"{ordered[menu_name]} buah {menu_name} dihapus dari pesanan.", end="")
        del ordered[menu_name]  # jika ada hapus dari ordered
    return ordered


def main():
    menu = parse_menu()  # membaca menu dari file txt
    while True:
        print("Selamat datang di Kafe Daun Daun Pacilkom")
        command = input("Apa yang ingin Anda lakukan? ")
        # handling input command
        if command == "BUAT PESANAN":  # fitur BUAT PESANAN
            nama = input("Siapa nama Anda? ")
            print()
            print_menu(menu)
            assign_table(select_menu(menu), nama)
        if command == "UBAH PESANAN":  # fitur UBAH PESANAN
            while True:
                try:
                    # meminta dan memvaliasi nomor meja pengguna
                    table_num = int(input("Nomor meja berapa? "))
                    if table.get(table_num, {}) == {}:
                        raise ValueError
                    print()
                    print_menu(menu)
                    # tampilkan menu dan pesanan pengguna
                    display_order(menu, table[table_num])
                    print()
                    order_to_update = table[table_num]
                    while True:
                        # handling action ubah pesanan, setiap aksi memodifikasi pesanan di meja tersebut
                        action = input(
                            "Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                        if action == "SELESAI":
                            display_order(menu, order_to_update)
                            table[table_num] = order_to_update
                            print("\n---")
                            break
                        elif action == "GANTI JUMLAH":
                            table[table_num] = change_amount(
                                menu, order_to_update)
                        elif action == "HAPUS":
                            table[table_num] = delete_order(
                                menu, order_to_update)
                        elif action == "TAMBAH PESANAN":
                            table[table_num] = add_order(menu, order_to_update)
                        else:
                            print(f"Input {action} tidak valid!")
                except ValueError:
                    print("Nomor meja kosong atau tidak sesuai!")
                    break
        if command == "SELESAI MENGGUNAKAN MEJA":
            try:
                # minta dan validasi input nomor meja
                table_num = int(input("Nomor meja berapa? "))
                if table.get(table_num, {}) == {}:
                    raise ValueError
                print()
                # print informasi pengguna
                print(
                    f"Pelanggan atas nama {names[table_num]} selesai menggunakan meja {table_num}.")
                ordered = table[table_num]
                table[table_num] = {}
                merged_menu = merge_menu(menu)
                receipt_list = []
                total = 0
                # susun baris dari receipt
                for menu_name in ordered:
                    receipt_list.append(";".join([
                        merged_menu[menu_name]['code'],
                        menu_name,
                        str(ordered[menu_name]),
                        str(merged_menu[menu_name]['price']),
                        str(merged_menu[menu_name]
                            ['price'] * ordered[menu_name])
                    ]) + "\n")
                    total += merged_menu[menu_name]['price'] * \
                        ordered[menu_name]
                # tambahkan jumlah di akhir receipt
                receipt_list.append(f"\nTotal {total}\n")
                # export receipt ke sebuah file txt
                with open(f"receipt_{names[table_num]}.txt", "w+") as receipt:
                    receipt.writelines(receipt_list)

            except ValueError:
                print("Nomor meja kosong atau tidak sesuai!")


if __name__ == '__main__':
    main()
