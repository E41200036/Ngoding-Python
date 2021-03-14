"""
Variabel Global
---------------
Variabel yang dibuat di luar fungsi (seperti dalam semua contoh di atas) dikenal sebagai variabel global.
Variabel global dapat digunakan oleh semua orang, baik di dalam fungsi maupun di luar.
"""

# contoh : Buat variable di luar fungsi, dan gunakan di dalam fungsi

x = 12
def cetakAngka():
    print(x)

cetakAngka() # nilai [x] diambil dari nilai variabel global diluar fungsi

"""
Jika kamu membuat variabel dengan nama yang sama di dalam fungsi, variabel ini akan menjadi variabel lokal, dan hanya dapat digunakan di dalam fungsi. Variabel global dengan nama yang sama akan tetap seperti sebelumnya, global dan dengan nilai aslinya.
"""

nilai = 80
def cetakNilai():
    nilai = 90
    print('nilai saya = ' + str(nilai))

cetakNilai() # nilai dari variabel [nilai] diambil dari variabel lokal / variabel yang ada didalam fungsi
print(nilai) # nilai dari variabel [nilai] diambil dari variabel global / variabel yang ada diluar fungsi

"""
GLOBAL KEYWORD
--------------
Biasanya, saat Anda membuat variabel di dalam fungsi, variabel itu bersifat lokal, dan hanya dapat digunakan di dalam fungsi itu.

Untuk membuat variabel global di dalam suatu fungsi, Anda dapat menggunakan kata kunci [global]
"""

def namaHewan():
    global hewan
    hewan = 'koala'
    print('nama hewannya adalah ' + hewan)

namaHewan() # nilai yang dicetak diambil dari variabel global [hewan] yang ada didalam fungsi
print('nama hewan saya : ' + hewan) # nilai yang dicetak diambil dari variabel global [hewan] yang ada didalam fungsi


"""
Selain itu, gunakan globalkata kunci jika Anda ingin mengubah variabel global di dalam fungsi.

Contoh : 
Untuk mengubah nilai variabel global di dalam fungsi, lihat variabel dengan menggunakan globalkata kunci:
"""

slogan = 'sip'

def myFunction():
    global slogan
    slogan = 'kreatif'
    print('polije '+ slogan)
    
myFunction() # nilai yang dicetak diambil dari variabel [slogan] yang ada di dalam fungsi