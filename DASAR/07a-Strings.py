"""
STRING PYTHON
-------------
untuk menulis sebuah [string] python menyediakan 2 aturan:
"""

# menggunakan ['']
print('ibnu')

# menggunakan [""]
print("putri")

# cara menaruh String ke variabel
nama = 'putri'
print(nama)


"""
STRING ARRAY
------------
[string] merupakan kumpulan beberapa karakter yang tergabung dalam susunan [array]
"""

# untuk mendapatkan elemen tertentu gunakan []
jurusan = 'TI'
print(jurusan[1]) #  nilai [I] merupakan index 1

"""
LOOPING STRING
--------------
karena [string] merupakan sekumpulan karakter, jadi kita bisa melakukan perulangan karakter didalam [string] menggunakan [for]
"""

surat = 'nama saya ibnu'
for x in surat: 
    print(x)
    
# mendapatkan panjang string menggunakan [len]
print(len('ibnu ganteng')) # [12] merupakan panjang string
