"""

Output Variables
----------------
[print] sering digunakan untuk menampilkan output dalam python
untuk menggabungkan teks dan variabel, kamu bisa menggunakan [+]

"""

nama = 'ibnu'
print('Hei! nama saya ' + nama)

# Untuk teks / huruf, kamu juga bisa menggunakan [+] untuk menggabung variabel ke variabel lain
namaDepan = 'putri '
namaBelakang = 'latifatus salamah'
namaLengkap = namaDepan + namaBelakang
print('perkenalkan nama saya ' + namaLengkap)

# untuk angka, kamu bisa menggunkan [+] untuk menjumlahkan variabel
nilai1 = 20
nilai2 = 23
print(nilai1 + nilai2)

# tapi, jika kamu mencoba menggabung string dan angka, Python akan memberi peringatan kesalahan
ipK = 3.90
nim = 'E41200036'
print('nim dengan nomor ' + nim + ' mendapat ipK sebesar ' + ipK)

"""
Error yang dihasilkan : 

Traceback (most recent call last):
  File "e:\PYTHON\DASAR\03d-OutputVariable.py", line 27, in <module>
    print('nim dengan nomor ' + nim + ' mendapat ipK sebesar ' + ipK)
TypeError: can only concatenate str (not "float") to str

"""