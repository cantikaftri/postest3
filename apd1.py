import os  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def option():
    clear_screen()
    print("-----------------------------------------------")
    print("Selamat Datang di Toko Kue Sule")
    print("Rasanya Dijamin Bikin Nagih")
    print("-----------------------------------------------")
    print("Menu Pilihan :")
    print("[1] Kue Coklat")
    print("[2] Kue Keju")
    print("[0] Keluar")
    print("Masukkan Option")
    option = int(input("Option :"))
    if option==1:
        print("Kue Coklat ")
        a=int(input("Berapa Kue Coklat Yang Anda Ingin Beli : "))
        jumlah = a * 3500
        jumlah2 = a * 3500 * 7 / 100
        jumlah3 = jumlah - jumlah2
        jumlah4 = a * 3500 * 12 / 100
        jumlah5 = jumlah - jumlah4
        if a <= 4 :
            print("Total Biaya Pembelian Anda Rp.",jumlah)
            back_to_option()
        elif a >= 5 and a <= 20:
            print("Total Pesanan Kue Coklat Anda",str(a) +  "Selamat Anda Mendapat Potongan Harga Dari Toko Kami Sebesar Rp.",jumlah2)
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Total Biaya Pembelian Anda Rp.",jumlah3)
            back_to_option()
        elif a >= 21 and a <= 35:
            print("Total Pesanan Kue Coklat Anda",str(a) +  "Selamat Anda Mendapat Potongan Harga Dari Toko Kami Sebesar Rp.",jumlah4)
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Total Biaya Pembelian Anda Rp.",jumlah5)
            back_to_option()
        else:
            print("Maaf Stok Kue Coklat Tidak Tersedia")
            back_to_option()
    elif option==2:
        print("Kue Keju")
        a=int(input("Berapa Kue Keju Yang Anda Ingin Beli : "))
        jumlah = a * 6000
        jumlah2 = a * 6000 * 10 / 100
        jumlah3 = jumlah - jumlah2
        jumlah4 = a * 6000 * 15 / 100
        jumlah5 = jumlah - jumlah4
        if a <= 3 :
            print("Total Biaya Pembelian Anda Rp.",jumlah)
            back_to_option()
        elif a >= 4 and a <= 15:
            print("Total Pesanan Kue Keju Anda",str(a) +  "Selamat Anda Mendapat Potongan Harga Dari Toko Kami Sebesar Rp.",jumlah2)
            print("---------------------------------------------------------------------------------------------------------------")
            print("Total Biaya Pembelian Anda Rp.",jumlah3)
            back_to_option()
        elif a >= 16 and a <= 25:
            print("Total Pesanan Kue Keju Anda",str(a) +  "Selamat Anda Mendapat Potongan Harga Dari Toko Kami Sebesar Rp.",jumlah4)
            print("---------------------------------------------------------------------------------------------------------------")
            print("Total Biaya Pembelian Anda Rp.",jumlah5)
            back_to_option()
        else:
            print("Maaf Stok Kue Keju Tidak Tersedia")
            back_to_option()
def back_to_option():
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    option()
    
        
#HSJDHKJD
option()


    