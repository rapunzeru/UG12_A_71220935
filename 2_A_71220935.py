nama = str(input('Masukkan nama: '))

for letter in range(len(nama)):
    print (nama[0:letter + 1])
for letter in range (len(nama)):
    print (nama[nama:letter - 1])