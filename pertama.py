#a
pertama={"keju","tepung","garam","gula","coklat"}
kedua={"garam","gula","coklat","kecap"}
print("hari pertama=",pertama)
print("hari kedua=",kedua)

#b 
kedua={"garam","gula","coklat","kecap"}
kedua.add("keju")
print("b=",kedua)

#c 
c=pertama&kedua
print("c=",c)

#d 
d=pertama-kedua
print("d=",d)

#e 
e=pertama.remove("garam")
print("e=",pertama)

#f 
f=kedua-pertama
print("f=",f)

#g 
g=pertama^kedua
print("g=",g)

#h 
tuple=("hari pertama",pertama)
for x in tuple:
	print(x)
	
#i 
tuple=("hari kedua",kedua)
for x in tuple:
	print(x)
	
	
for i in range (0,5):
	for j in range (0,i+1):
		if (i%2)==1:
			print("# ",end="")
		else:
			print("* ",end="")
	print()