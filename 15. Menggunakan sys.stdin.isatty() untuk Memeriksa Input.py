import sys

if sys.stdin.isatty():
    print("Input dari terminal.")
else:
    print("Input tidak dari terminal.")

#Fungsi: Memeriksa apakah input saat ini berasal dari terminal atau dari penyimpanan.
#Kondisi: Ketika kode perlu menangani input dari berbagai sumber dengan berbeda cara.