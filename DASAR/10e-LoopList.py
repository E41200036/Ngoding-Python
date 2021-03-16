"""
LOOPING LIST
------------
untuk memunculkan semua item dalam [list], kamu bisa menggunakan perintah looping [for]
"""

# contoh :
names = ["ibnu", 'putri', 'edotensei']
for x in names:
    print(x)

"""
LOOPING ITEM BY INDEX
---------------------
untuk mengakses item berdasarkan index kami bisa menggunakan :
"""

# contoh:
fruits = ["appple", "orange", "pir"]
for i in range(len(fruits)) :
    print(fruits[i])

"""
LOOP USING WHILE
----------------
melakukan looping menggunakan [while] kamu bisa menggunakan kata kunci [len] untuk mengidentifikasi panjang dari [list]
"""
# contoh :
siswa = ['ibnu', 'putri', 'jhon']
i = 0
while i < len(siswa):
    print(siswa[i])
    i = i + 1
    
"""
LOOPING USING LIST COMPREHENSION
--------------------------------
[list comprehension] merupakan kode pendek yang digunakan untuk mencetak semua item list
"""
# contoh
[print(x) for x in siswa]