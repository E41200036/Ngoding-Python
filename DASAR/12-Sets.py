"""
SET
---
[set] digunakan untuk menyimpan banyak data dalam satu variabel
Data didalam [set] tidak boleh <duplikat> dan diubah.
Data didalam [set] tidak terurut.
"""

# contoh :
# untuk membuat [set] gunakan tanda [ {} ] 
siswa = {'ibnu', 'putri', 'iza'}
print(siswa) # {'ibnu', 'putri', 'iza'}

# cek type
print(type(siswa)) # <class 'set'>

# membuat [set] menggunakan constructor
buah = set(('apel', 'nanas', 'mangga'))
print(buah) # {'nanas', 'apel', 'mangga'}