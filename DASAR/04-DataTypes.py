"""
TIPE DATA
---------
Tipe data adalah identitas yang menerangkan pada variabel tentang tipe dari nilai yang ditampung
Semisal : untuk variabel [nama] di menampung teks maka pakai tipe data [str / string]

Python memiliki tipe data bawaan berikut ini secara default, dalam kategori ini:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

"""

# cara melihat tipe data dari sebuah nilai variabel
nama = 'moh ibnu abdurrohman sutio'
kelas = 12
print(type(nama)) # <class 'str'> [string : kalimat / kata]
print(type(kelas)) # <class 'int'>  [int : angka / numerik]

"""
CARA MENGATUR TIPE DATA
-----------------------
Di Python, tipe data disetel saat kita menetapkan nilai ke variabel:
"""

# tipe data string
x = "Ibnu"
print(type(x))
# tipe data integer
x = 12
print(type(x))
# tipe data float
x = 3.90
print(type(x))
# tipe data complex
x = 1j
print(type(x))
# tipe data list
x = ["ibnu", "putri"]
print(type(x))
# tipe data tuple
x = ("RPL", "TKJ", "MM")
print(type(x))
# tipe data range
x = range(8)
print(type(x))
# tipe data boolean
x = True
print(type(x))
x = False
print(type(x))
# tipe data bytes
x = b"Hello"
print(type(x))

"""
CARA MENGATUR TIPE DATA TERTENTU
--------------------------------
"""
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
