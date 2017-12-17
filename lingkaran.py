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