import sys

sys.tracebacklimit = 1
try:
    x = 1 / 0
except Exception as e:
    print("Kesalahan:", e)

#Fungsi: Mengatur berapa banyak traceback yang ditampilkan saat terjadi kesalahan.
#Kondisi: Untuk mengendalikan informasi kesalahan yang ditampilkan di log.