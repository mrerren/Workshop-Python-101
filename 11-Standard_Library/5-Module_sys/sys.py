# contoh penggunaan modul sys / System-specific Configuration

import sys

# argumen terminal
print sys.argv
# versi python
print 'versi python: ', sys.version
# platform
print 'platform : ', sys.platform
# letak python interpreter
print 'executable : ', sys.executable
# byteorder
print 'byteorder : ', sys.byteorder

# module yang diimport
print 'modul yang diimport : ', sys.modules
# module built-in
print 'modul built-in : ', sys.builtin_module_names

# path import
print 'path import : ', sys.path