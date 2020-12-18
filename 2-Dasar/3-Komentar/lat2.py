# lat2.py
# lat2.py adalah nama file ini
# program ini akan menampilkan 'Halo Indonesia!'
# kemudian akan menampilkan 'Halo Jakarta!'

print 'Halo Indonesia!'
print 'Halo Jakarta!'

# print 'Teks ini tidak akan dicetak.'


""" pada PEP 8 (Python Enhancement Proposal) tentang komentar
Guido Van Rossum dkk. membagi penejelasan tentang komentar pada python kedalam tiga bagian.

1. Block Comments
    Block Comments umumnya berlaku untuk beberapa (atau semua) kode yang mengikutinya, dan menjorok 
    ke tingkat yang sama dengan kode itu. Setiap baris dari komentar blok dimulai dengan
    tanda # dan satu spasi (kecuali jika teks itu menjorok ke dalam komentar).
    
    contoh:
    # example
    
2. Inline Comments
    Inline Comments adalah komentar di baris yang sama dengan pernyataan. Komentar sebaris harus dipisahkan oleh setidaknya dua spasi dari pernyataan atau lebih. Komentar harus dimulai dengan tanda # dan satu spasi.
    
    contoh:
    x = x + 1  # Compensate for border

3. Documentation Strings
    Documentation Stings dituliskan untuk mendeskripsikan dengan jelas untuk apa kegunaan semua 
    public modules, functions, classes, dan methods.
    
    Documentation Strings menggunakan tanda  tiga kali petik dua \""" atau tiga kali petik satu '''
    
    terdapat dua cara untuk menuliskan Documentation Strings.
    1. untuk multiple line Documentation Strings tanda \""" yang terakhir harus berada pada satu baris sendiri. contoh:
        \"""Return a foobang

        Optional plotz says to frobnicate the bizbaz first.
        \"""
        
    2. untuk one line Documentation Strings tanda \""" yang terakhir harus tetap berada satu baris dengan documentation Strings. contoh:
        \"""Return an ex-parrot.\"""
        
    catatan: abaikan tanda \ backslash pada penjelasan Documentation Strings diatas.

Guido menyarankan untuk menggunakan komentar yang jelas dan mudah dimengerti oleh orang lain dan 
guido menyarankan untuk membuat komentar dengan menggunakan bahasa inggris kecuali jika benar-benar
yakin 120% bahwa komentar tidak akan pernah dibaca oleh orang lain.

---------------
referensi:
https://www.python.org/dev/peps/pep-0008/#comments 

"""