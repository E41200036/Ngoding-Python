"""
NUMBERS
-------
Tipe data number pada python ada beberapa, contoh :
1.  int
2.  float
3.  complex
"""

# int : tipe data yang menampung bilangan bulat positif dan negatif
x = 12
print(type(x))

# float : tipe data yang menampung bilangan bulat positif dan negatif
x = 3.14
print(type(x))

# complex : tipe data yang menampung bilangan complex
x = 3 + 5j
print(type(x))

"""
KONVERSI TIPE DATA NUMBER
-------------------------
Konversi bisa dilakukan seperti cara sebelumnya : 
"""

# convert int to float
kelas = 12
fKelas = float(kelas)

# convert float to int
nilai = 95.5
iNilai = int(nilai)

# convert int to complex
anak = 2
cAnak = complex(anak)

print(type(fKelas)) # <class 'float'>
print(type(iNilai)) # <class 'int'>
print(type(cAnak))  # <class 'complex'>


"""
RANDOM NUMBER
-------------
Python tidak punya fungsi [random()]. Tapi python menyediakan module untuk membuat angka random
"""
# ex : 
import random

print(random.randrange(1, 10))