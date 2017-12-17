print("=====konpro 04=====")
print ("Angka Binary diawali 0b, Hexa diawali 0x, Oktal diawali 0o")
print("1.desimal ke biner")
print ("2.biner ke desimal")
print ("3.Desimal ke Hexa")
print ("4.Desimal ke Octal")
i = int(input("masukan pilihan anda:"))
if i ==1:
	x = int(input("masukan angka desimal:"))
	print(bin(x))
elif i == 2:
    x = int(input("masukkan angka Binary: "),2)
    print (x)
elif i == 3:
    x = int(input("masukkan angka Desimal: "))
    print (hex(x))
elif i == 4:
    x = int(input("masukkan angka Desimal: "))
    print (oct(x))
else:
	print("good bye")


