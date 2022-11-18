import sys


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
                if line[0:2] == "==":
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
        print(e)
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


def merge_menu(menu):
    merged_menu = {}
    for item in menu.values():
        merged_menu = {**merged_menu, **item['names']}
    return merged_menu


def select_menu(menu):
    ordered = {}
    prev_order = ""
    while True:
        if prev_order:
            print(
                f"Berhasil memesan {prev_order}. Masukkan menu yang ingin Anda pesan: ")
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
    print("\nBerikut adalah pesanan anda:")
    merged_menu = merge_menu(menu)
    total = 0
    for key in ordered:
        price = merged_menu[key]['price'] * ordered[key]
        total += price
        print(
            f"{key} {ordered[key]} buah, total Rp{format_money(price)}")
    print(f"\nTotal pesanan: {format_money(total)}\n\n---")
    return ordered


def main():
    menu = parse_menu()
    while True:
        print("Selamat datang di Kafe Daun Daun Pacilkom")
        command = input("Apa yang ingin Anda lakukan? ")
        if command == "BUAT PESANAN":
            nama = input("Siapa nama Anda? ")
            print_menu(menu)
            select_menu(menu)


if __name__ == '__main__':
    main()
