#tugas: Buat password Berlapis 3
# jika salah: password salah, anda gagal pada halaman 1
# jika salah: password salah, anda gagal pada halaman 2
# jika salah: password salah, anda gagal pada halaman 3

# jika Benar pertama: Password Benar, Selamat Datang di halaman 1
# jika Benar ke-2: Password Benar, Selamat Datang di halaman 2
# jika Benar ke-3: Password Benar, Selamat Anda Berhasil Login

# Tiap halaman, memiliki kesempatan 3 kali masukkan password
    

def login():
    passwords = [
        "password1",   
        "password2",  
        "password3"   
    ]

    max_attempts = 3

    for i, password in enumerate(passwords, start=1):
        attempts_remaining = max_attempts

        while attempts_remaining > 0:
            attempt = input(f"Masukkan kata sandi untuk halaman {i}: ")

            if attempt == password:
                if i < len(passwords):
                    print(f"Password benar, selamat datang di halaman {i}")
                else:
                    print("Password benar, selamat Anda berhasil login")
                break
            else:
                attempts_remaining -= 1
                if attempts_remaining > 0:
                    print(f"Password salah, Anda gagal pada halaman {i}. Kesempatan mencoba tersisa: {attempts_remaining}")
                else:
                    print(f"Anda gagal pada halaman {i}. Akun diblokir.")
                    return

login()
