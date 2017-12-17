def option():
		print("pilih salah satu dari tiga fungsionallitas berikut:")
		print("1. menyimpan kode biner")
		print("2. tampilkan semua kode biner")
		print("3. keluar program")
		pilihan=int(input("maasukan pilihan anda:"))
		return pilihan
def destobin (n):
	a=[]
	while n >=1:
		b = n % 2
		n = n / 2 
		a.append (b)
	print a[::-1]
		
pilihan = True		
while(pilihan<3):
	pilihan = option()
	if (pilihan==1):
		biner =str(input("masukan kode biner :"))
		file = open("biner.txt","a+")
		data=file.write("biner:%s\n"%(biner))
		print("=== Membaca secara keseluruhan ===")
	elif(pilihan==2):
		file = open("biner.txt","r")
		print("==menampilkan biner==")
		print(file.read())
	else:
		print(" good bye")