import os
import time

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        #NIM: 2009106045 + 10 = 55
        angka = int(input("Masukkan angka: "))
        a = 1
        b = 1
        while a <= angka:
            print (b)
            b += 1
            if b == 10:
                b -= 9
            a += 1
        break
    except ValueError:
        print("Nomor Tidak Valid")
