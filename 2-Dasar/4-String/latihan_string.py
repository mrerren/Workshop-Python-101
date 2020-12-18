# -*- coding: utf-8 -*-
""" pengkodean UTF-8 telah menjadi standarisasi untuk pengkodean dalam system operasi, bahasa 
pemrograman, API, dan software. Dengan mendeklarasikan UTF-8 berarti file tersebut telah memberi 
informasi terhadap browser dan search engine untuk melakukan pengkodean karakter sesuai ketentuan 
UTF-8.
"""


""" untuk mennambahkan string kedalam output yang akan ditampilkan, dapat menggunakan operator % atau menggunakan method format
"""
# contoh menggunakan operator %
print '%s menggunakan operator %s pada %s' % ('Latihan', '%', 'Python')

""" untuk menambahkan string kedalam output cukup dengan menggunakan tanda %s

kekurangan dengan menggunakan operator % ini adalah tidak dapat memposisikan string sesuai yang kita inginkan. String hanya dapat diposisikan dari kiri ke kanan.
"""

# contoh menggunakan method format
print '{2} menggunakan method {0} pada {1}'.format('Latihan', 'FORMAT', 'Python')

""" hampir serupa dengan menggunakan operator %, akan tetapi dibedakan dengan menggunakan kurung kurawal {} dalam menambahkan setiap string kedalam output.

jika pada operator % string tidak dapat diposisikan seperti yang kita mau. akan tetapi pada methdo format kita dapat memposisikan string dengan menambahkan angka di setiap kurung kurawal {}.

karena method format bertipe tuple, maka angka yang ditetapkan harus terurut dari 0.
"""