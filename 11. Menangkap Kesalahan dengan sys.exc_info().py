import sys

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Terjadi kesalahan:", sys.exc_info())

#Fungsi: Menampilkan detail tentang kesalahan yang terjadi.
#Kondisi: Ketika Anda perlu mendapatkan informasi lebih lanjut tentang kesalahan yang terjadi.
