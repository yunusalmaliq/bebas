
fibs = [1,1]
num = int(input (" masukan jumlah deret fibonaci "))

if num <3 :
	print ("minimal 3 deret")
else:
	for i in range (num-2):
		fibs.append(fibs[-2]+fibs[-1])
		print(fibs)
		

def rekursif(angka):
    if angka > 0 :
        print (angka)
        angka = angka - 1
        rekursif(angka)
    else :
        print(angka)
masukan = int(input("masukkan angka : "))
rekursif(masukan)