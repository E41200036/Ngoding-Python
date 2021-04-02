"""
MENGHAPUS ITEM SET
------------------
Untuk menghapus item dalam satu set, gunakan [remove()], atau [discard()]

"""
# contoh :
siswa = set(('ibnu', 'putri'))
siswa.remove('ibnu')
print(siswa) # {'putri'}

siswa.discard('putri')
print(siswa) # set()

# untuk menghapus item random gunakan [pop()]
# contoh :
buah = { 'apel', 'nanas', 'jeruk' }
buah.pop()
print(buah) # {'apel', 'jeruk'}

# untuk mengosongkan set gunakan method [clear()]
buah.clear()
print(buah) # set()

# untuk menghapus set sepenuhnya, gunakan [del]
# contoh
del buah
print(buah) # NameError: name 'buah' is not defined


"""
KESIMPULAN
1. method [remove(value)] : akan menghapus item
2. method [discard(value)] : akan menghapus item juga
3. method [clear()] : akan mengosongkan item set
4. method [del()] : akan menghapus set sepenuhnya
5. method [pop()] : akan menghapus item set secara random
"""
