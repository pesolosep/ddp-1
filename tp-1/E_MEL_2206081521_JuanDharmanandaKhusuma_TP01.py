# Nama  : Juan Dharmananda Khusuma
# NPM   : 2206081521
# Kelas : E

from tkinter.messagebox import showinfo
from turtle import *  # Import utility function dari module turtle
from random import randint  # Import randint untuk nilai RGB random

setup(1.0, 1.0)
bgcolor("green")

WARNA_BATA_LUAR = "#BC4A3C"
# Meminta input dari user sekaligus validasi input
n_bawah = numinput(
    "Input", "Jumlah batu bata pada lapisan paling bawah:", minval=1, maxval=25)
while not n_bawah.is_integer():
    showinfo("Error", "Maaf input tidak valid, input harus berbentuk integer")
    n_bawah = numinput(
        "Input", "Jumlah batu bata pada lapisan paling bawah:", minval=1, maxval=25)

n_atas = numinput(
    "Input", "Jumlah batu bata pada lapisan paling atas:", minval=1, maxval=25)
while not (n_atas.is_integer() and n_atas <= n_bawah):
    showinfo("Error", "Maaf input tidak valid, input harus berbentuk integer dan harus bernilai lebih kecil dari lapisan paling bawah")
    n_atas = numinput(
        "Input", "Jumlah batu bata pada lapisan paling atas:", minval=1, maxval=25)

w_bata = numinput(
    "Input", "Panjang satu buah batu bata (pixel):", minval=1, maxval=35)
while not w_bata.is_integer():
    showinfo("Error", "Maaf input tidak valid, input harus berbentuk integer")
    w_bata = numinput(
        "Input", "Panjang satu buah batu bata (pixel):", minval=1, maxval=25)

h_bata = numinput(
    "Input", "Lebar satu buah batu bata (pixel):", minval=1, maxval=25)
while not h_bata.is_integer():
    showinfo("Error", "Maaf input tidak valid, input harus berbentuk integer")
    h_bata = numinput(
        "Input", "Lebar satu buah batu bata (pixel):", minval=1, maxval=25)

nb_memo = n_bawah

colormode(255)

# Menghitug konstanta
TOTAL = (n_bawah - n_atas + 1) / 2 * (2*n_bawah + (n_bawah - n_atas) * (-1))
WIDTH = n_bawah * w_bata
HEIGHT = ((n_bawah - n_atas) + 1) * h_bata
speed("fastest")

# Control variable untuk arah gerak normal dan reversed
rot = 90

# Centering candi
penup()
right(180)
forward(WIDTH//2)
right(180)
right(90)
forward(HEIGHT//2)
right(-90)

# Menggambar candi, setiap loop menggambar 1 layer
while n_bawah >= n_atas:
    fillcolor("black")
    if n_bawah == nb_memo or n_bawah == n_atas:
        fillcolor(WARNA_BATA_LUAR)
    # Setiap loop menggambar 1 batu bata lalu melakukan offset
    for i in range(int(n_bawah)):
        fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
        if (i == 0 or i == n_bawah - 1) or n_bawah == nb_memo or n_bawah == n_atas:
            fillcolor(WARNA_BATA_LUAR)
        forward(w_bata)
        begin_fill()
        pendown()
        # Setiap loop menggambar 1/2 batu bata
        for _ in range(2):
            right(rot)
            forward(h_bata)
            right(rot)
            forward(w_bata)
        end_fill()
        penup()

    # Melakukan offset ke atas dan samping
    # setiap selesai menggambar satu lapis
    left(180)
    forward(w_bata//2)
    right(rot)
    forward(h_bata)
    right(-rot)

    # Setiap selesai menggambar layer
    # invert semua pergerakan karena
    # program akan menggambar dari
    # arah yang berlawanan
    rot *= -1
    n_bawah -= 1

right(90)
forward(HEIGHT + 50)
hideturtle()
write(
    f"Candi warna-warni dengan {int(TOTAL)} batu bata",
    move=True,
    align="center",
    font=("Arial", "12", "bold")
)

exitonclick()
