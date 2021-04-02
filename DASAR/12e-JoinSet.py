"""
JOIN SET
--------
ada beberapa  cara untuk menggabung 2 atau lebih set dalam python
bisa dengan : 
1. [union()] : mengembalikan nilai set baru
2. [update()] : memasukan semua elemen dari suatu set ke set baru
"""

# contoh

# 1. union()
set1 = {'a','b','c'}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3) # {'ibnu', 'putri', 'iza'}

# 2. update()
siswa1 = {'ibnu', 'putri'}
siswa2 = {'iza'}

siswa1.update(siswa2)
print(siswa1) # {'ibnu', 'putri', 'iza'}

# Catatan: Keduanya union()dan update() akan mengecualikan item duplikat.

"""
DITAMBAHKAN HANYA DUPLIKATNYA
---------------------------
kamu bisa menggunakan method [intersection_update()]
"""

# contoh : 
angka1 = {1,2,3,4}
angka2 = {5,6,7,8,2}
angka1.intersection_update(angka2)
print(angka1)

# intersection() : menampilkan item yang sama diantara dua set yang ada
num1 = {1,2,3,4}
num2 = {2,3,4,5}
num1.intersection(num2)
print(num1)

# symmetric_difference_update() : menggabung semua kecuali data yang sama
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) 

# symmetric_difference() : Kembalikan satu set yang berisi semua item dari kedua set, kecuali item yang ada di keduanya:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) 