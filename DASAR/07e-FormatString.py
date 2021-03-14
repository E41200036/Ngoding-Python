"""
Format String
=============
Seperti yang kita pelajari di bab Variabel Python, kita tidak bisa menggabungkan string dan angka seperti ini:
----------------code----------------
age = 36
txt = "My name is John, I am " + age
print(txt)
------------------------------------
Tapi kita bisa menggabungkan string dan angka dengan menggunakan method [format()] ini!

method [format()] mengambil argumen berlalu, format mereka, dan tempat-tempat mereka dalam string mana placeholder {}adalah:

"""
kelas = 12
say = 'nama saya ibnu kelas {}'
print(say.format(kelas))


# contoh 2
nama = 'ibnu'
kelas = 12
jurusan = 'RPL'

biodata = 'nama saya {}, kelas {}, jurusan {}'
print(biodata.format(nama, kelas, jurusan))

