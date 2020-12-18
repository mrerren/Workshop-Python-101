# -*- coding: utf-8 -*-

""" Variabel merupakan tempat/wadah pada memori komputer yang 
digunakan untuk menampung  nilai.

Sintaks:    
    variable_name: type_name
    
Python memiliki aturan dalam penamaan variabel, seperti:
 1. Nama variabel harus diawali dengan huruf atau karakter.underscore _
    contoh:
        _var
        mVar

 2. Dapat menggunakan karakter alpha-numeric dan hanya dapat 
 menggunakan karakter underscore.
    contoh:
        var_1
        m2Var
        
 3. Nama variabel bersifat case-sensitive.
    contoh: 
        var, Var, VAR adalah tiga variabel yang berbeda
 
 4. Tidak boleh diawali dengan angka.
    contoh:
        4var
        
"""

_var = 10
mVar = 'dua puluh'
var_1 = 30
m2Var = 'empat puluh'
var = 50
Var = 'enam puluh'
VAR = 70

print '%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (_var, mVar, var_1, m2Var, var, Var, VAR)