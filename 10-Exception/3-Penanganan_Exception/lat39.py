# lat39.py

try:
    teks = raw_input('Ketikkan sesuatu: ')
except EOFError:
    print '\nKenapa sudah EOF?'
except KeyboardInterrupt:
    print '\nAnda membatalkan operasi'
else:
    print 'Anda mengetikkan "%s"' % teks