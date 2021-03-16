"""
JOIN LIST
---------
Ada beberapa cara untuk menggabungkan, atau menggabungkan, dua atau lebih daftar dengan Python.
Salah satu cara termudah adalah dengan menggunakan + operator.
"""
# contoh (+) : 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]

# menggunakan looping untuk menambahkannya satu per satu
list4 = []
for x in list1:
    list4.append(x)
    
print(list4)


# menggunakan method [extend()] untuk menaruh itemnya di akhir
number = [1,2,3,4,5]
number2 = [6,7,8,9,10]
number.extend(number2) # menambahkan item list [number2] ke list [number]

print(number) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""
RINGKASAN :
1. kamu bisa menggunakan [+] untuk melakukan join
2. kamu bisa menggunakan [append()] untuk melakukan join per item satu per satu
3. kamu bisa menggunakan [extend()] untuk melakukan join dan elemennya ditaruh di akhir list
"""


