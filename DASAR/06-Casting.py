"""
CASTING
-------
Ada kalanya ketika kamu ingin membuat variabel dengan nilai tertentu. Namun disini hanya menspesikan nilainya saja. Nah, kamu bisa lakukan [casting]. 
Berikut Beberapa contoh casting yang bisa dilakukan di Python : 

Oleh karena itu, casting dalam python dilakukan menggunakan fungsi konstruktor:

1.  int () - membangun bilangan bulat dari literal integer, literal float (dengan menghapus semua desimal), atau string literal (memberikan string mewakili bilangan bulat)
2.  float () - membangun angka float dari literal integer, literal float atau literal string (asalkan string mewakili float atau integer)
3.  str () - membangun string dari berbagai tipe data, termasuk string, literal integer dan literal float
"""

# casting int
print(int(1)) # ini akan menjadi 1
print(int(3.14)) # ini akan menjadi 3
print(int("5")) # ini akan menjadi 5

# casting float
print(float(1)) # ini akan menjadi 1.0
print(float(3.14)) # ini akan menjadi 3.14
print(float("5")) # ini akan menjadi 5.0

# casting complex
print(complex(1)) # ini akan menjadi (1+0j)
print(complex(3.14)) # ini akan menjadi (3.14+0j)
print(complex("5")) # ini akan menjadi (5+0j)

# casting string
print(str(1)) # ini akan menjadi "1"
print(str(3.14)) # ini akan menjadi "3.14"
print(str("5")) # ini akan menjadi "5"