"""
data structure yang digunakan
data = {
    'A': ('B', 10),
    'B': ('C', 100)
}
"""

data = {}

# Menerima input dari user dan berhenti jika menemui input selesai


def get_input():
    while True:
        user_input = input()
        if user_input == "SELESAI":
            break
        nama, kenalan, jarak = user_input.split()
        data[nama] = (kenalan, float(jarak))  # Menambahkan data ke dict

# melakuan search dan menghitung jarak dari awal dan akhir


def search(start, finish):
    # base case, jika tidak dapat dilakukan search lebih lanjut
    # dan finish masih belum ditemukan maka raise ValueError
    if start not in data:
        raise ValueError()
    # ambil data next node yang akan menggantikan start dan juga jarak
    next_node, path_len = data[start]
    # jika next_node yang akan dicari merupakan finish
    # maka langsung return jarak
    if next_node == finish:
        return path_len
    # jika bukan maka tambahkan jarak lalu lanjut kan rekursi dengan next_node
    return path_len + search(next_node, finish)

# main function


def main():
    print("Masukkan data hubungan:")
    get_input()
    print()
    start = input("Masukkan nama awal: ")
    end = input("Masukkan nama tujuan: ")
    try:  # Melakukan printing output sesuai dengan nilai jarak total
        jarak_total = search(start, end) * 10
        print(f"Jarak total: {int(jarak_total)}")
        if jarak_total > 1000:
            print(f"{start} dan {end} tidak saling kenal.")
        elif 100 < jarak_total <= 1000:
            print(f"{start} dan {end} mungkin saling kenal.")
        elif 0 < jarak_total <= 100:
            print(f"{start} dan {end} kenal dekat.")
    except ValueError:  # jika function search mendapatkan value error berarti user tidak ditemukan
        print(f"Tidak ada hubungan antara {start} dan {end}.")


if __name__ == '__main__':
    main()
