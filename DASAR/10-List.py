"""

LIST 
----
[list] digunakan untuk menyimpan beberapa data dalam satu variabel
[list] merupakan 1 dari 4 tipe data bawaan python yang digunakan untuk menyimpan kumpulan data.

cara membuat list : 
*list dibuat dengan '[]'

[nama_list] = [ nilai1, nilai2, ... ]

"""

siswa = ['ibnu', 'putri', 'izah']
print(siswa)

# nilai pada [list] dapat diurutkan, diubah, dan di duplikat
# nilai pada [list] diurutkan berdasarkan [index] yang dimulai dari 0

"""
ketika data pada [list] terurut, itu berarti bahwa item tersebut memiliki urutan yang ditentukan dan urutan tersebut tidak akan berubah
jika kamu menambahkan nilai baru pada [list], item tersebut akan ditempatkan di akhir [list]

Catatan: Ada beberapa metode daftar yang akan mengubah urutan, tetapi secara umum: urutan item tidak akan berubah.
"""

"""
CHANGEABLE
----------
List is changeable, artinya kita bisa mengubah, menambah, dan menghapus item dalam list setelah dibuat.

dan sebuah list boleh memiliki nilai yang sama [duplikat]
"""

# contoh
kelas = [10,11,12,12]
print(kelas)

# untuk mengetahui panjang [list]
# gunakan method [len()]

# contoh
print(len(kelas))

"""
sebuah item [list] boleh bertipe apa saja. bahkan boleh dicampur
"""

# contoh
mahasiswa1 = ['E41200036', 'MOH IBNU ABDURROHMAN SUTIO', 2, 3.90, 'TIF']
print(mahasiswa1)


# untuk membuat [list] , kamu juga bisa menggunakan method [list( nilai1, nilai2, ... )]

# contoh
uniqueNumber = list((1,4,6,3,2,8,6,4))
print(uniqueNumber)


"""
Koleksi Python (Array)
----------------------
Ada empat tipe data kumpulan dalam bahasa pemrograman Python:

1. List adalah kumpulan yang dipesan dan diubah-ubah. Izinkan anggota duplikat.
2. Tuple adalah koleksi yang dipesan dan tidak dapat diubah. Izinkan anggota duplikat.
3. Set adalah koleksi yang tidak berurutan dan tidak terindeks. Tidak ada anggota duplikat.
4. Dictionary adalah kumpulan yang tidak berurutan dan dapat diubah. Tidak ada anggota duplikat.
5. Saat memilih tipe koleksi, ada gunanya untuk memahami properti dari tipe tersebut. Memilih jenis yang tepat untuk kumpulan data tertentu bisa berarti retensi makna, dan, itu bisa berarti peningkatan efisiensi atau keamanan.



"""