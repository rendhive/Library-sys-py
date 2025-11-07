import sys

print("Modul yang telah dimuat:")
for module in sys.modules:
    print(module)

#Fungsi: Menampilkan semua modul yang telah dimuat dalam sesi saat ini.
#Kondisi: Saat Anda perlu memeriksa modul yang diimpor dan statusnya.