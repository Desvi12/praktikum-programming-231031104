a = [6,0,0,2,0,1,0,1,4]

# akses item
print(a)
print(f'item indeks:0 {a[0]}')
print(f'item indeks:3 {a[3]}')
print(f'item indeks:terakhir {a[len(a)-1]}')
# akses item indeks negatif
print(f'item indeks:terakhir (-1) {a[-1]}')
print(f'item indeks:pertama  (-9) {a[-len(a)]}' )
print(f'item indeks:1 (-8) {a[-8]}')
print(f'item indeks:5 (-4) {a[-4]}')
# akses indeks batas
print(f'item indeks:1,2,... {a[1:]}')
print(f'item indeks:3,4,... {a[3:]}')
print(f'item indeks:0,1,2 {a[:3]}')
print(f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'item indeks:semua {a[:]}')
# pengirisan indeks
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8] {a[1:-1]}')


# Nested list
kelas = [('Pengantar pemrograman',3),
         ('Agama Islam',2),
         ('Bahasa Indonesia',2)
         ]

print(f'data kelas {kelas}')
kelas.append(('Kalkulus Dasar 1',3))
kelas.append(('Sains Terpadu',3))
print(f'data kelas {kelas}')

# Nama Mata kuliah 1: Matkul1 dengan jumlah sks:3
# Nama Mata kuliah 2: Matkul2 dengan jumlah sks:2
# Nama Mata kuliah 3: Matkul3 dengan jumlah sks:2
# Nama Mata kuliah 4: Matkul4 dengan jumlah sks:3
# Nama Mata kuliah 5: Matkul5 dengan jumlah sks:3

data = [('Thomas',2023,'Aktif'),
        ('600201014'),
        (90,89,93,97,100),
        (20,22),
        ('S1-Reguler','Sistem Informasi D','-Ganjil')]

        
print(f'Nama Mahasiswa:', data[0][0])         
print(f'NIM Thomas:', data[1])
print(f'program pendidikan Thomas:', data[4][1],data[4][0])
print(f'Angkatan Thomas:', data[0][1],data[4][2])
print(f'jumlah nilai Thomas adalah:', len(data[2]))
print(f'Data terbesar Thomas adalah:', max(data[2]))
print(f'Data terbesar Thomas adalah:', min(data[2]))
print(f'Rata-rata nilai Thomas adalah:', data[3]) 


data = [('Desvi',2023,'Aktif'),
        ('231031104'),
        (90,89,93,97,100),
        (92,25),
        ('S1-Reguler','Sistem Informasi D','-Ganjil')]


print(f'Nama Mahasiswa:', data[0][0])         
print(f'NIM Desvi:', data[1])
print(f'program pendidikan Desvi:', data[4][1],data[4][0])
print(f'Angkatan Desvi:', data[0][1],data[4][2])
print(f'jumlah nilai Desvi adalah:', len(data[2]))
print(f'Data terbesar Desvi adalah:', max(data[2]))
print(f'Data terbesar Desvi adalah:', min(data[2]))
print(f'Rata-rata nilai Desvi adalah:', data[3])
