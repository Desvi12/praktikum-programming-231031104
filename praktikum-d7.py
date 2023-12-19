pwd_benar = 'si23d'
a = True
limit = 3
i = 0

while a:
    i += 1
    pwd = input('Masukkan Password:')
    if pwd == pwd_benar:
        print('Password benar! Selamat Anda Login')
        a = False
    else:
        print('Password Salah!')
        if i == limit:
            print('Kesempatan Anda Habis!')
            a = False
        else:
            print(f'Kesempatan Anda Tersisa',limit-i)


#tugas: Buat password Berlapis 3
# jika salah: password salah, anda gagal pada halaman 1
# jika salah: password salah, anda gagal pada halaman 2
# jika salah: password salah, anda gagal pada halaman 3

# jika Benar pertama: Password Benar, Selamat Datang di halaman 1
# jika Benar ke-2: Password Benar, Selamat Datang di halaman 2
# jika Benar ke-3: Password Benar, Selamat Anda Berhasil Login

# Tiap halaman, memiliki kesempatan 3 kali masukkan password
    

pwd_1 = 'Abc123'
pwd_2 = 'Abcde'
pwd_3 = 'Abc12345'
a = True
limit = 3
i = 0

while a:
    i += 1
    pwd = input('Masukkan Password:')
    if pwd == pwd_benar:
        print('Password Benar, Selamat Datang di halaman 1')
        a = False
    else:
        print('Password salah, anda gagal pada halaman 1')
        if i == limit:
            print('Kesempatan Anda Habis!')
            a = False
        else:
            print(f'Kesempatan Anda Tersisa',limit-i)




        


