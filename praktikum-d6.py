a = True

while a:
    jawab = input('Apakah ingin lanjutkan? (y/n)')
    if jawab == 'y':
        print('Terima Kasih')
        a = True
    elif jawab == 'n':
        print('Sampai Jumpa :D')
        a = False
    else:
        print('Jangan Aneh deh:(')
        a = True 
