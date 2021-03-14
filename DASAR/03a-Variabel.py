"""
VARIABEL
--------

*sebuah wadah untuk menampung nilai/data

python tidak menetapkan aturan deklarasi untuk variabel.
variabel dibuat ketika dibutuhkan dan ketika memberi nilai awal.

"""

# membuat variabel
i = 20
j = 'ibnu'
print(i)
print(j)

"""
*Variabel tidak perlu dideklarasikan dengan jenis tertentu , dan bahkan dapat mengubah jenis setelah ditetapkan.
"""
x = 20 # variabel x bertipe int
print(x)
x = 'jhonny' # saat ini variable x bertipe string
print(x)

"""
CASTING
-------
Jika Anda ingin menentukan tipe data variabel, ini dapat dilakukan dengan casting.
"""

nama = str('kirana') # nama bertipe str
kelas = int(12) # kelas bertipe int
nilai = float(4.00) # nilai bertipe float
print(nama)
print(kelas)
print(nilai)

"""
CARA MELIHAT TIPE DATA
* type()
"""

prodi = "TIF"
print(type(prodi)) # prodi bertipe <'str'>

"""
LEBIH BAIK KUTIP [""] ATAU ['']

Variabel string dapat dideklarasikan baik dengan menggunakan tanda kutip tunggal atau ganda:
"""

nama = "ibnu"
# sama saja dengan
nama = 'ibnu'

# CASE SENSITIVE
# python membedakan besar kecil huruf dalam variabel

a = 20
# tidak sama dengan : 
A = 30
