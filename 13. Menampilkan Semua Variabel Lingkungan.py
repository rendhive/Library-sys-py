import sys

print("Variabel Lingkungan:")
for key, value in sys.environ.items():
    print(f"{key}: {value}")

#Fungsi: Menampilkan semua variabel lingkungan yang ada.
#Kondisi: Ketika Anda ingin menganalisa konfigurasi lingkungan sistem.
