"""
LIST COMPREHENSION
------------------
merupakan sebuah metode penulisan kode dengan singkat.

aturan penulisan : 
newlist = [expression for item in iterable if condition == True]

"""
# contoh
# berdasarkan [list] yang ada, kita akan menambahkan [item] yang mengandung karakter 'a' saja kedalam list baru

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newFruits = []

for x in fruits:
    if "a" in x :
        newFruits.append(x)
    
print(newFruits)

# dengan list comprehension, kamu bisa membuatnya menjadi satu baris
newFruits2 = [x for x in fruits if "a" in x]
print(newFruits2)


# contoh 2
siswa = ['ibnu', 'putri', 'jhon']
siswaU = []
for x in siswa:
    if 'u' in x:
        siswaU.append(x)
        
print(siswaU)


number = [1,2,3,4,5,6,7,8,9,10]
newNumber = [i for i in number if i%2 == 0]
print(newNumber)




