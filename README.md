sys Modul Python

sys itu modul penting di Python buat ngatur hal-hal yang berhubungan langsung sama interpreter. Jadi kalau lo mau ambil argumen dari command line, keluarin program dengan rapi, cek versi Python, atau ngatur path import, semuanya lewat sini.

Apa Fungsi sys?

sys jadi penghubung antara kode Python yang lo tulis sama interpreter yang ngejalanin kode itu. Makanya modul ini sering banget dipakai kalau bikin script atau tool yang butuh interaksi sama lingkungan Python.

Fitur-Fitur yang Sering Dipakai

1. sys.argv
Buat ngambil argumen dari command line.

import sys
print(sys.argv)

2. sys.exit()
Buat keluar dari program dengan cara yang rapi.

import sys
sys.exit(0)

3. sys.version
Buat tau versi Python yang lagi dipakai.

import sys
print(sys.version)

4. sys.path
Buat lihat dan ngatur daftar folder yang dipakai Python buat nyari modul.

import sys
print(sys.path)

Contoh Pemakaian

import sys

if len(sys.argv) < 2:
    print("Masukin nama dulu dong!")
    sys.exit(1)

nama = sys.argv[1]
print(f"Halo {nama}, selamat datang!")

Cara jalannya:

python app.py Randy

Kapan sys Dipakai?

Kalau lo butuh:

Ambil input dari command line

Keluarin program dengan rapi

Cek lingkungan Python

Atur path import


Simpel tapi berguna banget. Cocok buat lo yang mau bikin script lebih fleksibel dan berasa kayak tool beneran.

Selamat ngulik!
