"""
UPDATE TUPLE
------------
seperti yang kita ketahui bahwa data [tuple] tidak bisa diubah
dan agak 'tricky' untuk mengubah datanya. caranya :
1. buat tuple
2. convert ke [list]
3. kembalikan lagi menjadi [tuple]
"""

tuples = (1,2,3,4)
x = list(tuples)
x.append(5)
tuples = tuple(x)
print(tuples) # (1, 2, 3, 4, 5)

# begitupun dengan menghapus datanya
x = list(tuples)
x.remove(4)
tuples = tuple(x)
print(tuples) # (1, 2, 3, 5) : data 4 hilang

# untuk menghapus data tuple kamu bisa pakai method [del]
siswa = ("ibnu", "putri")
print(siswa) # ('ibnu', 'putri')
del siswa
print(siswa) # NameError: name 'siswa' is not defined
# error karena data tuple nya sudah tidak ada / dihapus



"""
KESIMPULAN
-----------
untuk mengubah data dari tuple, maka dengan cara
1. convert ke list dulu
2. lalu update datanya
3. ubha lagi kedalam data tuple
"""