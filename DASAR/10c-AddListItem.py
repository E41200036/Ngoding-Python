"""

ADD LIST ITEM
-------------
Untuk menambahkan item ke akhir daftar, gunakan metode [append()] :

"""

# contoh :
# menggunakan [append()] untuk menambahkan item
number = [1,2,4,5,6]
number.append(7)
print(number)
# nilai [7] akan ditambahkan di akhir index

"""
MENYISIPKAN ITEM
----------------
kamu bisa menggunakan method [insert( index, value )]
"""
# contoh :
fruits = ["apple", "banana", "cherry"]
fruits.insert(0, "pir")
print(fruits) # nilai [pir] akan ditaruh di index [0] dan menggeser nilai yang ada

"""

EXTEND LIST
-----------
Untuk menambahkan elemen dari daftar lain ke daftar saat ini, gunakan method [extend(list)].
* catatan : yang ditambahkan merupakan elemen saja. dan hanya boleh menggabung [list]
"""

# contoh
num1 = [1,2,3]
num2 = [4,5,6]
# menggabung num2 ke num1
num1.extend(num2)
print(num1) # [1, 2, 3, 4, 5, 6]
# begitupun sebaliknya. 


"""
Tambahkan Iterable Apapun
-------------------------
method [extend()] tidak harus menggabung list saja , Anda dapat menambahkan objek iterable (tupel, set, dict dll).
"""

# contoh : menambahkan objek [tuple] ke [list]
students = ["ibnu", "putri"]
newStudents = ("jhon")
students.append(newStudents)
print(students) # ['ibnu', 'putri', 'jhon']