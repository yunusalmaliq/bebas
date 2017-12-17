def action(kondisi):
	if(kondisi=="lapar"):
		result="harus makan"
	else:
		result="jangan makan"
	return result
		
		
result =action("lapar")
print(result)		


phi = 3.14

def luas_lingkaran(r):
	luas = phi*(2**r)
	return luas 
	
	
def keliling_lingkaran (r):
	keliling =2*phi*r
	return keliling 
	
	
	
r=8
l=luas_lingkaran(r)
k=keliling_lingkaran(r) 
print("luas lingkaran adalah :%.2f"%(l))
print ("keliling lingkaran adalah :%.2f"%(k))


def option():
		print("pilih salah satu dari tiga fungsionalitas berikut:")
		print("1. mencari luas lingkaran")
		print("2. mencari keliling lingkaran")
		print("3. keluar dari program")
		pilihan=int(input("masukan pilihan anda:"))
		return pilihan
		
		
pilihan =true
while (pilihan <3):
	pilihan =option()
	if (pilihan ==1):
		l=luas_lingkaran (r)
		print("luas_lingkaran:%.2f"%(l))
	elif(pilih==2):
		k=keliling_lingkaran(r)
		print("keliling lingkaran:%.2f"%(k))