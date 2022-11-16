# Juan Dharmananda Khusuma
# 2206081521
# MEL DDP 1 E

kunci = []  # list untuk menyimpan semua input kunci jawaban dari user
jawaban = []  # list untuk menyimpan semua input jawaban dari user

print("Selamat mencoba Program Pemeriksa Nilai Dek Depe!")
print("=================================================")

print("Masukan kunci jawaban:")

# Mengecek apakah input dari user valid
# (merupakan huruf kapital, hanya terdiri dari satu karakter, dan hanya berupa karakter A, B, C, D, dan E saja)


def valid(inp):
    return inp.isupper() and len(inp) == 1 and inp in "ABCDE"


# Melakukan looping hingga user memberi input STOP
while True:
    input_kunci = input()  # Menerima input dari user
    if input_kunci == "STOP":  # Jika user memasukan input STOP, loop dihentikan
        break
    if not valid(input_kunci):  # Validasi input, jika tidak valid user disuruh menginput kembali
        print("Input tidak valid ulangi lagi")
        continue
    # Jika input valid, tambahkan input ke list kunci jawaban
    kunci.append(input_kunci)

print("Masukan jawaban kamu:")
i = 0
while i < len(input_kunci) - 1:  # Melakukan loop sebanyak jumlah kunci jawaban
    input_jawaban = input()  # Menerima input dari user
    # Validasi input, jika input tidak valid maka user disuruh menginput kembali
    if not valid(input_jawaban):
        print("Input tidak valid ulangi lagi")
        continue
    # Jika valid maka tambahkan input ke list jawaban
    jawaban.append(input_jawaban)
    i += 1

# Menghitung jumlah jawaban yang benar, dengan list comprehension yang cukup mereturn None
# object jika jawaban dan kunci jawaban merupakan string yang sama, lalu menghitung panjang list
correct = len([None for x, y in zip(kunci, jawaban) if x == y])
total = len(kunci)  # Total soal sama dengan panjang list kunci jawaban

nilai = int(correct/total*100)  # Menghitung nilai ujian

# Melakukan printing output sesuai hasil perhitungan diatas
if nilai >= 85:
    print("Selamat :D")
elif 55 <= nilai <= 85:
    print("Semangat :)")
else:
    print("nt")
print(f"Total jawaban benar adalah {correct} dari {total} soal")
print(f"Nilai yang kamu peroleh adalah {nilai}")
