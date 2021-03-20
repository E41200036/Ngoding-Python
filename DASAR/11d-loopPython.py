"""
LOOPING TUPLE
-------------
kamu bisa melakukan perulangan dengan berbagai cara :
"""

# contoh
students = tuple(('ibnu', 'putri', 'dela', 'rima'))

# perulangan dengan for
for x in students: 
    print(x, end=' ') # ibnu putri dela rima
    
# perulangan dengan range
for i in range(len(students)) :
    print(students[i], end=' ') # ibnu putri dela rima  
    
# perulangan menggunakan while
while i < len(students):
    print(students[i]) # ibnu putri dela rima rima
    i += 1
    
    
"""
KESIMPULAN 
----------
1. untuk melakukan mengakses data tuple kamu bisa menggunakan perulangan
2. ada banyak macam perulangan contoh : 
3. for - mengakses data langsung
4. for - menggunakan range(len(tuple)) untuk mengakses data berdasarkan index
5 while - untuk mengakses data menggunakan index juga
"""



# ex : 
# rata rata array 5 bilangan
dataArray = list((1,2,3,4,5))
total = 0
for i in dataArray:
    total = total + i
print(int(total / len(dataArray)))

# mencari bilangan terbesar
num = tuple((1,2,3,4,5,6,7,8,9))
min = num[0]
max = num[0]

for i in num:
    if(max < i):
        max = i
    if(min > i):
        min = i
print('nilai terbesarnya : ' + str(max))
print('nilai terkecilnya : ' + str(min))