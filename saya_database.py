def option():
		print("pilih salah satu dari tiga fungsionallitas berikut:")
		print("1. menyimpan biodata")
		print("2. tampilkan semua biodata")
		print("3. keluar program")
		pilihan=int(input("maasukan pilihan anda:"))
		return pilihan
		

		
pilihan = True		
while(pilihan<3):
	pilihan = option()
	if (pilihan==1):
		nama =str(input("masukan nama :"))
		asal =str(input("masukan asal :"))
		tanggal =str(input("masukan tanggal lahir :"))
		file = open("modul8.txt","a+")
		data=file.write("nama:%s\n"%(nama))
		file = open("modul8.txt","a+")
		data=file.write("asal daerah:%s\n"%(asal))
		file = open("modul8.txt","a+")
		data=file.write("tanggal lahir:%s\n"%(tanggal))
		print("=== Membaca secara keseluruhan ===")
	elif(pilihan==2):
		file = open("modul8.txt","r")
		print("==menampilkan biodata==")
		print(file.read())
	else:
		print(" good bye")