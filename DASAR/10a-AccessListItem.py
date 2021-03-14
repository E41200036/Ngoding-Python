"""

ACCESS LIST ITEM
----------------
[item] pada list merupakan [index] yang tersusun. jadi, kamu bisa akses posisi [index]nya untuk melihat nilai itemnya.

"""

# contoh :
siswa = ["ibnu", "putri", "jhon"]
print(siswa[0]) # [nilai] diperoleh dari posisi indeks yang dimulai dari 0
print(siswa[1])
print(siswa[2])

# contoh : 
# mengakses [index] dengan [negative / - ]
kelas = [10,11,12]
print(kelas[-1]) 
print(kelas[-2]) 
print(kelas[-3]) 
# catatan : jika menggunakan nilai negatif maka nilai yang akan dipanggil dimulai dari belakang.
# seperti : -3 -2 -1 0 1 2

"""

RANGE OF INDEX
---------------
untuk mengakses item dengan [range] tertentu kamu bisa menggunakan tanda [:]
dengan format : 

namaList[start_index:end_index]

"""
# saya akan mengakses nilai [apple] sampai [orange]

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[0:4])

# [0] merupakan range start dan [4] merupakan end index, dan nilai nya akan diabaikan

# jika ingin memanggil nilai dari awal kamu tidak perlu menuliskan start indexnya
# contoh :

number = [1,2,3,4,5,6,7,8,9]
print(number[:5]) # [1, 2, 3, 4, 5]

# nilai yang dipanggil akan muncul kecuali index [5]

# jika ingin memanggil sampai index akhir tidak perlu menulis end indexnya
print(number[2:]) # [3, 4, 5, 6, 7, 8, 9]
# nilai yang terpanggil mulai dari index [2] sampai akhir

"""
CHECK [IF] ITEM EXIST
---------------------
untuk melakukan check, apakah item ada atau tidak. kamu bisa menggunakan perintah [if]
"""

# contoh : 
# cek jika surakarta ada dalam list
kota = ["malang", "surabaya", "jakarta", "surakarta", "probolinggo"]
if "surakarta" in kota:
    print('ya, surakarta ada di list')






