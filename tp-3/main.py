import sys

table = {(i+1): {} for i in range(10)}


def format_money(amount):
    return f"Rp{amount:,}".replace(",", ".")


def parse_menu():
    token = {}
    check = []
    curr = ""
    try:
        with open("./menu.txt", "r") as menu:
            for line in menu:
                line = line.strip()
                if line[0:3] == "===":
                    if token.get(line, None):
                        raise Exception()
                    curr = line
                    token[line] = {}
                    if not token[line].get('codes', {}):
                        token[line]['codes'] = {}
                    if not token[line].get('names', {}):
                        token[line]['names'] = {}

                else:
                    code, name, price = line.split(";")
                    if name in check or code in check:
                        raise Exception()
                    check = [*check, name, code]
                    token[curr]['codes'][code] = {
                        'name': name, 'price': int(price)}
                    token[curr]['names'][name] = {
                        'code': code, 'price': int(price)}
    except Exception as e:
        print("Daftar menu tidak valid, cek kembali menu.txt!")
        sys.exit(1)
    return token


def print_menu(menu):
    print("Berikut ini adalah menu yang kami sediakan:")
    for menu_type in menu:
        print(f"{menu_type.replace('===', '')}:")
        for key in menu[menu_type]['codes']:
            data = menu[menu_type]['codes']
            print(
                f"{key} {data[key]['name']}, {format_money(data[key]['price'])}")
    print()


def merge_menu(menu):
    merged_menu = {}
    for item in menu.values():
        merged_menu = {**merged_menu, **item['names']}
    return merged_menu


def get_available_table():
    min_val = 100
    for num in table:
        if table[num] == {} and num < min_val:
            min_val = num
    return min_val


def display_order(menu, ordered):
    print("\nBerikut adalah pesanan anda:")
    merged_menu = merge_menu(menu)
    total = 0
    for key in ordered:
        price = merged_menu[key]['price'] * ordered[key]
        total += price
        print(
            f"{key} {ordered[key]} buah, total Rp{format_money(price)}")
    print(f"\nTotal pesanan: {format_money(total)}")


def assign_table(ordered):
    table_num = get_available_table()
    table[table_num] = ordered
    if table_num < 11:
        print(
            f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {table_num}. Terima kasih.")
    else:
        print("Mohon maaf meja sudah penuh, silakan kembali nanti.")
    print("\n---")


def select_menu(menu, ordered={}):
    prev_order = ""
    while True:
        if prev_order:
            print(
                f"Berhasil memesan {prev_order}. ", end="")
        order_input = input("Masukkan menu yang ingin Anda pesan: ")
        if order_input == "SELESAI":
            break
        for listing in menu.values():
            if order_input in listing['codes']:
                ordered[listing['codes'][order_input]['name']] = ordered.get(
                    listing['codes'][order_input]['name'], 0) + 1
                prev_order = listing['codes'][order_input]['name']
                break
            if order_input in listing['names']:
                ordered[order_input] = ordered.get(order_input, 0) + 1
                prev_order = order_input
                break
        else:
            print(f"Menu {order_input} tidak ditemukan. ", end="")
            prev_order = ""
    display_order(menu, ordered)
    return ordered


def add_order(menu, ordered):
    menu_input = input("Menu apa yang ingin Anda ganti jumlahnya: ")
    menu_name = ""
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
    ordered[menu_name] = ordered.get(menu_name, 0) + 1
    print(f"Berhasil memesan {menu_name}.")
    return ordered


def change_amount(menu, ordered):
    menu_input = input("Menu apa yang ingin Anda ganti jumlahnya: ")
    menu_name = ""
    try:
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
        if not ordered.get(menu_name, None):
            print(f"Menu {menu_input} tidak Anda pesan sebelumnya. ", end="")
            prev_order = ""
        else:
            amount = int(input("Masukkan jumlah pesanan yang baru: "))
            ordered[menu_name] = amount
            if amount <= 0:
                raise ValueError
            print(
                f"Berhasil mengubah pesanan {menu_name} {amount} buah.", end="")
    except (ValueError, TypeError):
        print("Jumlah harus bilangan positif.")
    finally:
        return ordered


def delete_order(menu, ordered):
    menu_input = input("Menu apa yang ingin Anda hapus dari pesanan: ")

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
    if not ordered.get(menu_name, None):
        print(f"Menu {menu_input} tidak Anda pesan sebelumnya. ", end="")
        prev_order = ""
    else:
        print(
            f"{ordered[menu_name]} buah {menu_name} dihapus dari pesanan.", end="")
        del ordered[menu_name]
    return ordered


def main():
    menu = parse_menu()
    while True:
        print("Selamat datang di Kafe Daun Daun Pacilkom")
        command = input("Apa yang ingin Anda lakukan? ")
        new_order = {}
        if command == "BUAT PESANAN":
            input("Siapa nama Anda? ")
            print()
            print_menu(menu)
            new_order = select_menu(menu)
            assign_table(new_order)
        if command == "UBAH PESANAN":
            try:
                table_num = int(input("Nomor meja berapa? "))
                if table.get(table_num, {}) == {}:
                    raise ValueError
                print()
                print_menu(menu)
                display_order(menu, new_order)
                print()
                order_to_update = table[table_num]
                while True:
                    action = input(
                        "Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                    if action == "SELESAI":
                        display_order(menu, order_to_update)
                        table[table_num] = order_to_update
                        print("\n---")
                        break
                    elif action == "GANTI JUMLAH":
                        new_order = change_amount(menu, order_to_update)
                    elif action == "HAPUS":
                        delete_order(menu, order_to_update)
                    elif action == "TAMBAH PESANAN":
                        change_amount(menu, order_to_update)
                    else:
                        print(f"Input {action} tidak valid!")

            except ValueError:
                print("Nomor meja kosong atau tidak sesuai!")
                break


if __name__ == '__main__':
    main()
