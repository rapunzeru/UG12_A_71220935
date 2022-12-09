batas = int(input('Masukkan pembatas: '))
larang = int(input('Masukkan angka yang dilarang: '))

for i in range (0, batas):
    if i==larang:
        continue
    print (i, end='\t')
i = i + 1