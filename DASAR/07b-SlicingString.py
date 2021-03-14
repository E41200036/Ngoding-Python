"""
SLICING STRING
--------------
kita juga bisa melakukan pengirisan [string], yang bertujuan untuk memisah karakter tertentu.
kita bisa menggunakan tanda [index_awal:index_akhir]

"""

# contoh
nama = 'ibnu ganteng'
print(nama[0 : 4]) # [ibnu] merupakan nilai yang didapat dari index 0 - 4

# untuk memotong dari depan kita bisa meninggalkan index pertama
print(nama[:7]) # [ibnu ga] merupakan nilai dari index 0 - 7

# untuk memotong sampai akhir kita bisa meninggalkan index terakhir
print(nama[2:]) # [nu ganteng] merupakan nilai dari index 2 - akhir


