"""
SORT LIST
---------
untuk melakukan sorting, kamu bisa menggunakan method [sort()] untuk mengurutkan secara alfanumerik / menaik.
"""

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)

# untuk mengurutkan secara menurun gunakan kata kunci [reverse = True]
num = [1,3,2,4,6,8,7,9,10]
num.sort(reverse=True)
print(num)

"""
SORTING ADJUST FUNCTION
-----------------------
Anda juga dapat menyesuaikan fungsi Anda sendiri dengan menggunakan argumen kata kunci [key = function]

Fungsi tersebut akan mengembalikan angka yang akan digunakan untuk mengurutkan daftar (angka terendah terlebih dahulu):
"""

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


"""
REVERSE SORTING
---------------
untuk membalik posisi item dalam list, kamu bisa menggunakan [reverse]
"""
newList = ["banana", "Orange", "Kiwi", "cherry"]
newList.reverse()
print(newList) # ['cherry', 'Kiwi', 'Orange', 'banana']

