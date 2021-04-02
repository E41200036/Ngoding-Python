"""
MENAMBAH ITEM SET
-----------------
untuk menambah item baru pada [set], kamu bisa gunakan method [add()]
"""

# contoh
buah = { "apel", "jeruk" }
buah.add('nanas')
print(buah) # {'nanas', 'apel', 'jeruk'}

# sedangkan untuk menambah item dari [set] lain, kamu bisa menggunakan method [update]
# contoh
siswa = { 'ibnu', 'putri' }
siswaBaru = { 'iza' }
siswa.update(siswaBaru)
print(siswa) # {'putri', 'iza', 'ibnu'}

# semisal untuk menambah item dari iterable berbeda
# contoh: set + list
mif = set(('jhon', 'reiner', 'mikasa'))
tif = list(('ibnu', 'banu'))
mif.update(tif)
print(mif) # {'ibnu', 'banu', 'mikasa', 'jhon', 'reiner'}

"""
KESIMPULAN : 
1. untuk menambah item gunakan [add()]
2. untuk menambah item dari iterable berbeda gunakan [update()]
"""