"""
METHOD TUPLE
------------
ada 2 method bawaan python yang bisa kamu gunakan:
1. [count()]	Returns the number of times a specified value occurs in a tuple
2. [index()]	Searches the tuple for a specified value and returns the position of where it was found
"""

# ex :

# count() : digunakan untuk menampilkan data array, dan mengembalikan nilai integer
# tuple.count(value)
fruits = tuple(('apple', 'pir', 'mango'))
show = fruits.count('apple')
print(show)

# index() untuk 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)