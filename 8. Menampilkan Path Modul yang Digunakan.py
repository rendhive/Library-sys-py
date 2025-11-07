import sys

print("Path modul yang sedang digunakan:")
for path in sys.path:
    print(path)

#Fungsi: Menampilkan direktori tempat Python mencari modul.
#Kondisi: Memeriksa lokasi pencarian modul untuk debugging atau pengembangan.
