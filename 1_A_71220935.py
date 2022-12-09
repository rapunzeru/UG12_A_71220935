awal = int(input('Masukkan angka awal: '))
akhir = int(input('Masukkan angka akhir: '))

for i in range (awal, akhir):
    if i%6!=0 and i%3!=0 and i%2!=0:
        print (i, end='\t')
    i = i + 1
