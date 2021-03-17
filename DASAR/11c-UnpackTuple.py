"""
UNPACK TUPLE
------------
ketika kita membuat tuple seperti ini :

"""
# ini disebut dengan packing tuple
siswa = ("ibnu", "putri")

# tapi di python, memungkinkan kita untuk mengekstrak nilainya kedalam variabel
# contoh
siswa = ("ibnu", "putri", "edi")
(siswa1, siswa2, siswa3) = siswa # nilai dalam tuple di taruh di variabel siswa1, siswa2, siswa3
print(siswa1) # ibnu
print(siswa2) # putri
print(siswa3) # edi
# perlu diingat : variabel yang menampung nilai tersebut harus sama banyaknya dengan jumlah nilai tuple


"""
USING ASTERIK (*)
-----------------
ketika variabel yang digunakan untuk menampung data tuple kurang. kamu bisa menggunkan simbol [*]
dan nilai akan ditetapkan ke variabel sebagai [list]
"""
number = (1,2,3,4,5,6,7)
(number1, number2, *number3) = number
print(number1) # 1
print(number2) # 2
print(number3) # [3, 4, 5, 6, 7] : data ini berubah menjadi [list]

# jika kamu mmenaruh asterik tidak pada elemen akhir, maka python akan menaruh datanya sesuai jumlah
# dan menyisakan data terakhir untuk variable paling akhir.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


"""
KESIMPULAN
-----------
1. python memungkinkan data [tuple] untuk di ekstrak dalam variabel
2. jumlah variabel penampung harus sama banyak dengan jumlah value dalam [tuple]
3. jika variabel penampung tidak cukup , maka gunakan simbol asterik (*)
"""
