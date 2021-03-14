"""
Banyak Nilai untuk Banyak Variabel
----------------------------------
Python memungkinkan Anda untuk menetapkan nilai ke beberapa variabel dalam satu baris:
"""

nama,kelas,jurusan = 'ibnu', 12, 'RPL'
print(nama)
print(kelas)
print(jurusan)

# Catatan: Pastikan jumlah variabel sesuai dengan jumlah nilai, atau Anda akan mendapatkan error.

"""
Satu Nilai untuk Beberapa Variabel
----------------------------------
Dan Anda dapat menetapkan nilai yang sama ke beberapa variabel dalam satu baris:
"""

x = y = z = 20
print(x)
print(y)
print(z)

# catatan : yaitu dengan menggunakan [=] yang berarti memberi nilai baru pada tiap variabel

"""
Unpack a Collection
-------------------
Jika Anda memiliki kumpulan nilai dalam daftar, tuple dll. Python memungkinkan Anda mengekstrak nilai ke dalam variabel. Ini disebut [unpack].
"""

# 1. membuat daftar
siswa = ['ibnu', 'putri']
x, y = siswa
print(x)
print(y)
