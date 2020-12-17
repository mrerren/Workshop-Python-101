# lat17.py

def fungsi():
    global x
    print 'x = ', x

def fungsi2():
    global x
    x = 200  # menulis ke lokal variabel
    print 'x = ', x

def fungsi3():
    global x
    x = 100
    print 'x = ', x

fungsi2()
print 'nilai x = ', x

print 'nilainya = ', x

fungsi3()
print 'nilai x = ', x

print 'nilai nya = ', x

x = 50
fungsi()
print 'nilai x = ', x