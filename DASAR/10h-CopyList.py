"""
MENYALIN LIST/COPY LIST
-----------------------
ada berbagai cara untuk melakukan copy list 
1. menggunakan keyword [copy()]
2. menggunakan keyword list(list)
"""

num = [1,2,3,4,5]

# 1 : copy()
newNum = num.copy()
print(newNum) # [1, 2, 3, 4, 5]

# 2 : list(list)
newNum2 = list(num)
print(newNum2) # [1, 2, 3, 4, 5]
