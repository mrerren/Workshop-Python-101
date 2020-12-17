# lat38.py

import pickle

daftar_belanja_file = 'daftar.data'
daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']

# membuka file penyimpanan obyek dengan mode tulis binary
f = open(daftar_belanja_file, 'wb')

# dump obyek ke file
pickle.dump(daftar_belanja, f)
f.close()

# hapus daftar_belanja dari memori
del daftar_belanja

# membaca dari file
f = open(daftar_belanja_file, 'rb')
daftar_tersimpan = pickle.load(f)
print daftar_tersimpan