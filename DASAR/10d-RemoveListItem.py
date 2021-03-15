"""
REMOVE LIST ITEM
----------------
untuk menghapus item dari list tertentu, kamu bisa menggunakan method [remove(value)]
"""

# contoh:
# menghapus nilai 2
num = [1,2,3,4,5]
num.remove(2)
print(num) # [1, 3, 4, 5]

"""

MENGHAPUS INDEKS TERTENTU
-------------------------
untuk menghilangkan index tertentu, kamu bisa menggunakan method [pop(index)]

"""

# contoh : 
# menghapus index ke [2]
names = ["ibnu", "putri", "jhon"]
names.pop(2)
print(names) # ['ibnu', 'putri']

# untuk menghapus index terakhir, kamu tidak perlu menuliskan indeksnya
# contoh
names.pop()
print(names) # ['ibnu']


"""
menggunkan kata kunci [del] 
dengan format : 
del list[index]

*untuk menghapus semua nilai dari list
del list
"""

myList = [1,2,3,4,5,6]
del myList[2]
# print(myList) # [1, 2, 4, 5, 6]

# menghapus semua nilai dari index
x = [1,2,3,4]
del x
# print(x) # ini akan muncul error karena kamu sudah menghapus [list]nya dengan baris kode diatas.


"""
MENGHAPUS DAFTAR
-----------------
kamu bisa menggunakan method [clear()]
"""

# contoh
kelas = [10,11,12]
kelas.clear()
print(kelas) # []
# ini hanya akan menghapus nilainya. bukan listnya.





