"""
PYTHON TUPLES
-------------
[tuple] digunakan untuk menaruh berbagai nilai didalam satu variabel
[tuple] adalah koleksi yang terstruktur dan tidak bisa diubah
[tuple] ditulis menggunakan simbol kurung [ () ]
"""

# contoh : 
myTuple = ("ibnu", "putri", 12)
print(myTuple) # ('ibnu', 'putri', 12)

"""
TUPLE ITEM
----------
data didalam [tuple] : terstruktur, tidak bisa diubah, dan mengijinkan dupllikat data
data dalam [tuple] mengacu pada penggunaan index untuk data 1 maka berada di index ke [0] etc.
"""
# contoh
number = (1,2,3,4,5,6,1)
print(number) # (1, 2, 3, 4, 5, 6, 1)

"""
TUPLE LENGTH
------------
untuk mengetahui berapa panjang data yang terdapat dari sebuah variabel [tuple]
kita bisa menggunakan method [len()]
"""
# contoh
student = ("ibnu", "putri", "iza")
print(len(student)) # 3
 
# untuk membuat [tuple] , perlu diingat bahwa kamu haru menggunakan koma [,]
myTuple = ("ibnu", )
print(myTuple) # (ibnu)

# bukan tuple
myTuple = ("ibnu")
print(type(myTuple)) # <class 'str'>

"""
TUPLE CONSTRUCTOR
-----------------
untuk membuat data [tuple], python menggunakan juga method [tuple()]
"""
# contoh
uniqueNumber = tuple((1,2,3,4,5,5,65,32,1))
print(uniqueNumber) # (1, 2, 3, 4, 5, 5, 65, 32, 1)
