def option():
	print("")
	print("Angka Binary diawali 0b, Hexa diawali 0x, Oktal diawali 0o")
	print("---------------------------------------------------------\n")
	print("1.desimal ke biner")
	print("2.biner ke desimal")
	print("3.Desimal ke Hexa")
	print("4.Desimal ke Octal")
	print("5.Keluar")
	pilihan = int(input("masukan pilihan anda:"))
	return pilihan

pilihan = True
while(pilihan<5):
	pilihan = option()
	if pilihan ==1:
		print("---------------------------------------------------------")
		x = int(input("masukan angka desimal:"))
		print("Angka biner: ",bin(x))
		print("---------------------------------------------------------\n")
	elif pilihan == 2:
		print("---------------------------------------------------------")
		x = int(input("masukkan angka Binary: "),2)
		print (x)
		print("---------------------------------------------------------\n")
	elif pilihan == 3:
		print("---------------------------------------------------------")
		x = int(input("masukkan angka Desimal: "))
		print (hex(x))
		print("---------------------------------------------------------\n")
	elif pilihan == 4:
		print("---------------------------------------------------------")
		x = int(input("masukkan angka Desimal: "))
		print (oct(x))
		print("---------------------------------------------------------\n")
	else:
		print("---------------------------------------------------------")
		print("good bye")