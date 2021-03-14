"""
MODIFY STRING
-------------
python juga menyediakan fitur untuk mengubah string menjadi format tertentu

contoh :

"""

# mengubah tulisan menjadi kapital dengan fungsi [upper()]
nama = "ibnu"
print(nama.upper()) # [IBNU]

# mengubah tulisan menjadi huruf kecil dengan fungsi [lower()]
prodi = "TEKNIK INFORMATIKA"
print(prodi.lower()) # [teknik informatika]

# untuk menghapus spasi diawal dan akhir kalimat menggunakan [strip()]

say = " hello you "
print(say.strip()) # [hello you]

# memisahkan string menggunakan [split()]
# jadi nilai yang dihasilkan berdasarkan parameter yang dimasukan dan nilai tersebut diubah menjadi array
slogan = "hidup,adalah,kehidupan"
print(slogan.split(","))