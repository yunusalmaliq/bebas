try :
    print ('Konversi dari :')
    print ('1. Biner')
    print ('0. exit')

    masukan = int (input('masukan pilihan : '))
    print ('')

    while masukan > 2 or masukan < 0 : #pengecek inputan pemilihan menu
        print ('silahkan masukan angka yang ada pada menu.')
        masukan = int (input('masukan pilihan : '))
        print ('')
        
    while masukan != 0 :
        tampil = ''
        biner = 0
        hexa = 0
        pembalik = []
        cetak = []
        
        if masukan == 1: 
            print ('')
            print ('konvert ke')
            print ('1. Okta')
            print ('')
            menu = int (input('masukan pilihan : '))
            print ('')
            while menu > 2 or menu < 0 :
                print ('silahkan masukan angka yang ada pada menu.')
                menu = int (input('masukan pilihan : '))
                print ('')      
        elif masukan == 2:
            print ('konvert ke')
            print ('1. Okta')
            menu = int (input('masukan pilihan :'))
            print ('')

            while menu > 2 or menu < 0 :
                print ('silahkan masukan angka yang ada pada menu.')
                menu = int (input('masukan pilihan : '))
                print ('')
            
            if menu == 1:
                bin = input('masukan biner :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i]) #membalikkan biner
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)
                print('hasilnya adalah : ',biner)
                print ('')
            if menu == 2:
                bin = input('masukan biner :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)
                
                while biner != 0:
                    hasil = biner % 8
                    cetak.insert(0, str(hasil))
                    biner = biner//8
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('hasilnya adalah : ',tampil)
                print ('')
            if menu == 3:
                bin = input('masukan biner :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('hasilnya adalah : ',tampil)
                print ('')
        elif masukan == 3:
            print ('konvert ke')
            print ('1. Biner')  
            menu = int (input('masukan pilihan :'))
            print ('')
            
            while menu > 2 or menu < 0 :
                print ('silahkan masukan angka yang ada pada menu.')
                menu = int (input('masukan pilihan : '))
                print ('')
            
            if menu == 1:
                bin = input('masukan okta :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(8**i)
                print('hasilnya adalah : ', biner)
                print ('')
                
            if menu == 2:
                bin = input('masukan okta :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 2
                    cetak.insert(0, str(hasil))
                    biner = biner//2
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('hasilnya adalah : ',tampil)
                print ('')

            if menu == 3:
                bin = input('masukan okta :')
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range (len(cetak)):
                            tampil +=  cetak[i]
                print ('hasilnya adalah : ',tampil)
                print ('')
                
        elif masukan == 4:
            print ('konvert ke')
            print ('1. Okta')
            menu = int (input('masukan pilihan :'))
            print ('')

            if menu == 2:
                bin = input('masukan biner :')

                for i in range (len(bin)) :
                    if bin[i] != 'a' or bin[i] != 'b' or bin[i] != 'c' or bin[i] != 'd' or bin[i] != 'e' or bin[i] != 'f' :
                        a = False;
                    else :
                        a = True

                while a == False :
                    for i in range (len(inputan)) :
                        if inputan[i] != 'a' or inputan[i] != 'b' or inputan[i] != 'c' or inputan[i] != 'd' or inputan[i] != 'e' or inputan[i] != 'f' :
                            a = False;
                            break
                        else :
                            a = True
                        
                print ('')
                for i in range (len(bin)):
                    pembalik.insert(0, bin[i]) #membalikkan biner
                for i in range (len(pembalik)):
                    biner += int (pembalik[i])*(2**i)
        print('Konversi dari :')
        print ('1. Biner')
        print ('0. exit')
        masukan = int (input('masukan pilihan : '))
        print ('')
        
except :
    print ('anda memasukan inputan yang salah. dan maaf program terhenti')