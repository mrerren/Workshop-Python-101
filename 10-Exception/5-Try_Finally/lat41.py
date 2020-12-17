# lat41.py

import time

try:
    while True:
        f = open('coba.txt')
        baris = f.readline()
        if len(baris) == 0:
            # EOF
            break
        print baris,
        time.sleep(2) # delay 2 detik
except KeyboardInterrupt:
    print '\nAnda membatalkan operasi'
finally:
    f.close()
    print '\nfile ditutup.'