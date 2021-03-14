"""

CHANGE LIST ITEM
----------------
untuk mengganti item spesifik, mengacu pada indexnya

"""

# contoh
# mengganti nilai 3 dengan 100

number = [3, 4, 5, 6, 7, 8, 9]
number[0] = 100
print(number[0])

# mengganti item dengan range tertentu
# contoh : mengganti nilai banana dan cherry dengan leci, pinaple

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits[1:3] = ["leci", "pinaple"]
print(fruits) # ['apple', 'leci', 'pinaple', 'orange', 'kiwi', 'mango']

# jika kamu mengubah nilai, tapi index yang dituju melebihi rangenya.
# maka nilai tersebut akan diisi menjadi nilai baru pada posisi yang ditentukan

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)