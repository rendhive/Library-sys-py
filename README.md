Contoh Pustaka sys Python 🚀

Modul sys itu alat wajib kalau lo mau ngatur hal-hal yang berhubungan langsung sama interpreter Python. Mulai dari baca argumen, keluarin program, cek versi Python, sampai utak-atik path import. Simple tapi kepake banget.


---

Apa yang Bisa sys Lakuin?

• Baca argumen dari command line 🧾
• Keluar dari program dengan rapi ✅
• Cek versi Python yang lagi dipakai 🐍
• Lihat dan ubah path import 📂
• Interaksi langsung sama lingkungan interpreter ⚙️


---

Contoh Cepat

import sys

print("Argumen:", sys.argv)
print("Versi Python:", sys.version)
print("Path Import:", sys.path)


---

Contoh Penggunaan Argumen

import sys

if len(sys.argv) < 2:
    print("Masukin nama dulu dong!")
    sys.exit(1)

nama = sys.argv[1]
print(f"Halo {nama}, selamat datang!")

Jalanin via terminal:

python app.py


---

Kapan sys Dipake?

• Kalau script lo butuh input dari user lewat command line
• Kalau mau handle exit program biar lebih proper
• Kalau pengen tau info interpreter Python
• Kalau mau oprek path import modul

sys itu ringan tapi penting buat bikin script yang berasa kayak tool beneran. Selamat ngulik! 😎🐍

Udah gue sulap jadi gaya yang enak dibaca kayak contoh screenshot lo. Kalau mau ditambah emoji, warna, atau struktur lain tinggal bilang, gue gas terus.
