"""
ACCESS ITEM OF TUPLE
--------------------
untuk mengakses item data [tuple] kita bisa menggunakan index

"""
# contoh
# mengakses data ke 2
siswa = ("ria", "otong", "ucup", "mario")
print(siswa[1]) # otong

# mengakses data menggunakan negatif index
print(siswa[-1]) # mario

# untuk mengakses range data tertentu
# akses data ke 1 - 3
print(siswa[0:3]) # ('ria', 'otong', 'ucup')

# untuk mengakses data sampai akhir seperti berikut :
print(siswa[0:]) # ('ria', 'otong', 'ucup', 'mario')

# untuk mengakses data dari awal
# akses data dari awal - 3
print(siswa[:3]) # ('ria', 'otong', 'ucup')

"""
CHECK IF ITEM EXIST
------------------
untuk cek apakah data ada atau tidak, kita bisa menggunakan method (if)
"""

# contoh
kelas = (10, 11, 12)
if 11 in kelas :
    print("kelas 11 ada") # kelas 11 ada



